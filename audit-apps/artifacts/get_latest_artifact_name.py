#!/usr/bin/env python3


import os
import sys
from google.cloud import storage


def usage():
    message = f"""
Usage: {os.path.basename(sys.argv[0])} folder filename

The following environment variables must be set:

    APP_CODE_BUCKET_NAME: name of the GCS bucket with artifacts
    APP_CODE_BRANCH: root folder inside bucket
"""
    print(message, file=sys.stderr)
    sys.exit(-1)


def get_latest_blob_by_name(bucket_name, prefix, file_name):
    """Get latest blob by name function"""

    storage_client = storage.Client()

    latest_blob = None
    bucket = storage_client.bucket(bucket_name)
    blobs = storage_client.list_blobs(bucket_name,
                                      prefix=prefix, delimiter='/')

    for blob in blobs:
        if blob.name.startswith(f"{prefix}{file_name}"):
            blob_data = bucket.get_blob(blob.name)
            if debug:
                print(f"name: {blob.name} updated: {blob_data.updated}")
            if not latest_blob:
                latest_blob = blob_data
                next
            if latest_blob.updated < blob_data.updated:
                latest_blob = blob_data

    return latest_blob.name


def main():
    """This script takes folder and file name as arguments
    and returns the latest version of found artifact"""
    global debug
    debug = bool(os.environ.get('DEBUG', False))
    bucket_name = os.environ.get('APP_CODE_BUCKET_NAME')
    branch = os.environ.get('APP_CODE_BRANCH')

    if len(sys.argv) < 3:
        print("Missing required arguments!")
        usage()
    elif not all([bool(s) for s in [bucket_name, branch]]):
        print("Missing environment variables!")
        usage()
    folder = sys.argv[1]
    file_name = sys.argv[2]
    prefix = f"{branch}/{folder}/"

    artifact = get_latest_blob_by_name(bucket_name, prefix, file_name)
    if artifact:
        print(artifact)
    else:
        print(f"No artifacts starting with name '{file_name}' "
              f"found inside 'gs://{bucket_name}/{prefix}'")


if __name__ == '__main__':
    main()
