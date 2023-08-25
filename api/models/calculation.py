from db import db


class CalculationModel(db.Model):
    __tablename__ = "calculations"

    id = db.Column(db.Integer, primary_key=True)

    column_name = db.Column(db.String(120), nullable=False)
    benford_law_distribution = db.Column(db.JSON, nullable=False)
    rows_count = db.Column(db.Integer, nullable=False)
    skipped_rows_count = db.Column(db.Integer, nullable=False)
    # Relationship
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'datasets.id'), unique=False, nullable=False)
    dataset = db.relationship(
        'DatasetModel', backref=db.backref('calculations', lazy=True))
