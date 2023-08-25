from db import db


class DatasetModel(db.Model):
    __tablename__ = "datasets"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    file_name = db.Column(db.String(120), nullable=False)
    file_columns = db.Column(db.ARRAY(db.String(120)), nullable=False)
