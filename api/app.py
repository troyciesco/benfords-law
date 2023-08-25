import os
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from resources.dataset import blp as DatasetBlueprint
from resources.calculation import blp as CalculationBlueprint
from resources.generated_data import blp as GeneratedDataBlueprint
from resources.temp_file import blp as TempFileBlueprint
from flask_cors import CORS

from db import db


def create_app(db_url=None):
    app = Flask(__name__)
    CORS(app, origins=os.getenv("CORS_ORIGINS"))
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Dataset REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['TEMP_UPLOAD_FOLDER'] = 'static/temp'
    app.config['STATIC_DATASETS_FOLDER'] = 'static/datasets'
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(DatasetBlueprint)
    api.register_blueprint(CalculationBlueprint)
    api.register_blueprint(GeneratedDataBlueprint)
    api.register_blueprint(TempFileBlueprint)
    return app
