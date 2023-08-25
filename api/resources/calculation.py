import csv
import os
import shutil
from flask import current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import CalculationModel, DatasetModel
from resources.schemas import CalculationSchema, CalculationCreateSchema

blp = Blueprint("calculations", __name__,
                description="Operations on calculations")


def process_file(file_path, column_name, delimiter):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        rows_count = 0
        skipped_rows_count = 0
        benford_law_distribution = {1: 0, 2: 0,
                                    3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for row in reader:
            value = row[column_name]
            if value is not None and value[0].isdigit() and int(value[0]) > 0:
                first_digit = int(value[0])
                benford_law_distribution[first_digit] += 1
                rows_count += 1
            else:
                skipped_rows_count += 1
        return rows_count, skipped_rows_count, benford_law_distribution


@blp.route("/datasets/<string:dataset_id>/calculations")
class CalculationsList(MethodView):

    @blp.response(200, CalculationSchema(many=True))
    def get(self):
        return CalculationModel.query.all()

    @blp.arguments(CalculationCreateSchema, location="json", as_kwargs=True)
    @blp.response(201, CalculationSchema)
    def post(self, dataset_id, **calculation_data):
        dataset = DatasetModel.query.get_or_404(dataset_id)

        dataset_file_path = os.path.join(
            current_app.config['STATIC_DATASETS_FOLDER'], dataset.file_name)
        temp_file_path = os.path.join(
            current_app.config['TEMP_UPLOAD_FOLDER'], dataset.file_name)

        # Check if the file exists in the datasets folder
        if not os.path.isfile(dataset_file_path):
            # If not, check if it exists in the temp folder
            if os.path.isfile(temp_file_path):
                # If it does, move it to the datasets folder
                shutil.move(temp_file_path, dataset_file_path)
            else:
                # If it doesn't exist in either folder, return an error
                abort(400, description="File not found")

        delimiter = ','
        _, file_extension = os.path.splitext(dataset.file_name)

        if file_extension == '.tsv':
            delimiter = '\t'

        rows_count, skipped_rows_count, benford_law_distribution = process_file(
            dataset_file_path, calculation_data["column_name"], delimiter=delimiter)
        calculated_data = {"rows_count": rows_count,
                           "skipped_rows_count": skipped_rows_count,
                           "benford_law_distribution": benford_law_distribution,
                           "dataset_id": dataset_id,
                           "column_name": calculation_data["column_name"]}
        calculation = CalculationModel(**calculated_data)
        try:
            db.session.add(calculation)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the calculation.")
        return calculation
