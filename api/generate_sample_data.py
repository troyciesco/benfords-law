from faker import Faker
import uuid
import csv
import os

def generate_sample_data():
    num_rows = 10**6
    num_columns = 9
    fake = Faker()

    # create a filename
    filename = str(uuid.uuid4()) + "generated_data.csv"
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

    print(f"File saved at {file_path}, generated {num_rows} rows")

generate_sample_data()