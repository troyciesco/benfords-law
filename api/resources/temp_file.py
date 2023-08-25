import os
import uuid
import pandas as pd
from flask import request, current_app
from flask.views import MethodView
from flask_smorest import Blueprint
from werkzeug.utils import secure_filename

blp = Blueprint('file', __name__, url_prefix='/file',
                description='File operations')


@blp.route('/upload-temp-file', methods=['POST'])
class UploadTempFile(MethodView):
    def post(self):
        if 'file' not in request.files:
            return {'message': 'No file in the request'}, 400

        file = request.files['file']

        if file.filename == '':
            return {'message': 'No selected file'}, 400

        if file:
            filename = secure_filename(file.filename)
            unique_filename = str(uuid.uuid4()) + '_' + filename
            file.save(os.path.join(
                current_app.config['TEMP_UPLOAD_FOLDER'], unique_filename))

        delimiter = ','
        _, file_extension = os.path.splitext(filename)

        if file_extension == '.tsv':
            delimiter = '\t'

        df = pd.read_csv(os.path.join(
            current_app.config['TEMP_UPLOAD_FOLDER'], unique_filename), delimiter=delimiter)
        df = df.fillna("")
        columns = df.columns.tolist()
        total_rows = df.shape[0]

        # If less or equal than 15 rows, return all
        if total_rows <= 15:
            data = df.values.tolist()
        else:  # If more than 15 rows, return first, middle and last 5
            top_5 = df.head(5).values.tolist()
            middle_5 = df.iloc[total_rows//2 -
                               2: total_rows//2 + 3].values.tolist()
            last_5 = df.tail(5).values.tolist()
            data = top_5 + middle_5 + last_5

        return {"columns": columns, "rows": data, "file_name": unique_filename}
