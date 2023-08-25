from marshmallow import Schema, fields


# Base Schemas
class BaseCalculationSchema(Schema):
    id = fields.Str(dump_only=True)
    dataset_id = fields.Str(required=True)
    column_name = fields.Str(required=True)
    benford_law_distribution = fields.Dict(required=True)
    rows_count = fields.Int(required=True)
    skipped_rows_count = fields.Int(required=True)


class BaseDatasetSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    file_name = fields.Str(required=True)
    file_columns = fields.List(fields.Str(), required=True)


# Extended Schemas
class CalculationSchema(BaseCalculationSchema):
    dataset_id = fields.Str(required=True, load_only=True)
    dataset = fields.Nested(BaseDatasetSchema(), dump_only=True)


class DatasetSchema(BaseDatasetSchema):
    calculations = fields.List(fields.Nested(
        BaseCalculationSchema()), dump_only=True)


# Create Schemas
class CalculationCreateSchema(Schema):
    column_name = fields.Str(required=True)
