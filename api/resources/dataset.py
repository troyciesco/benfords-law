from flask import send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import DatasetModel
from resources.schemas import DatasetSchema


blp = Blueprint("datasets", __name__, description="Operations on datasets")


@blp.route("/datasets")
class DatasetList(MethodView):

    @blp.response(200, DatasetSchema(many=True))
    def get(self):
        return DatasetModel.query.all()

    @blp.arguments(DatasetSchema)
    @blp.response(201, DatasetSchema)
    def post(self, dataset_data):
        dataset = DatasetModel(**dataset_data)
        try:
            db.session.add(dataset)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A dataset with that title already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the dataset.")

        return dataset


@blp.route("/datasets/<string:dataset_id>")
class Dataset(MethodView):
    @blp.response(200, DatasetSchema)
    def get(self, dataset_id):
        dataset = DatasetModel.query.get_or_404(dataset_id)
        return dataset


@blp.route('/static/datasets/<path:filename>')
def serve_file(filename):
    return send_from_directory("static/datasets", filename)
