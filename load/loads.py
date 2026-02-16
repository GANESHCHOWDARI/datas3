import json
import csv
import boto3
from io import StringIO
from logs.logs import logger as logs

def load_data(data):
    # Load config
    with open('./source_and_target/config.json') as config_file:
        config = json.load(config_file)

    bucket_name = config['bucket']
    s3_key = config['destination_key']

    # Assume `data` is already a list of rows (from transforms)
    rows = data

    # Log each row
    for row in rows:
        logs.debug(f"Row: {row}")

    # Convert rows to CSV string
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerows(rows)

    # Upload to S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=csv_buffer.getvalue())

    logs.info(f"Data uploaded to s3://{bucket_name}/{s3_key}")