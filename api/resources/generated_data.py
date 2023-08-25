from flask.views import MethodView
from faker import Faker
from flask_smorest import Blueprint, abort
import csv
import os
import uuid
from marshmallow import Schema, fields

blp = Blueprint("generated_data", __name__,
                description="Operations to generate data")


class GeneratedDataSchema(Schema):
    message = fields.Str(dump_only=True)


@blp.route('/generate-csv')
class GeneratedData(MethodView):
    @blp.response(201, GeneratedDataSchema)
    def post(self):
        num_rows = 10**6
        num_columns = 9
        fake = Faker()

        # create a filename
        filename = str(uuid.uuid4()) + "_generated_data.csv"
        file_path = os.path.join('static/_sample-data/generated', filename)

        # create file and writer
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # create header row
            header = [f'Column{i+1}' for i in range(num_columns)]
            writer.writerow(header)

            # create rows
            for _ in range(num_rows):
                row = [
                    fake.random_int(min=0, max=1000),
                    fake.random_number(digits=5),
                    fake.random_number(digits=6),
                    fake.random_number(digits=4),
                    fake.random_number(digits=3),
                    fake.random_number(digits=2),
                    fake.random_number(digits=7),
                    fake.name(),
                    fake.address().replace('\n', ', ')
                ]
                writer.writerow(row)

        return {"message": f"File saved at {file_path}, generated {num_rows} rows"}
