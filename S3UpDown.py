import boto3

def upload_object(bucket_name, local_file_path, s3_file_path):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file_path, bucket_name, s3_file_path)
        print(f"File '{local_file_path}' uploaded to '{s3_file_path}' in bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def search_object(bucket_name, object_key):
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' found in bucket '{bucket_name}'.")
    except:
        print(f"Object '{object_key}' not found in bucket '{bucket_name}'.")

def download_object(bucket_name, object_key, local_file_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, object_key, local_file_path)
        print(f"File '{object_key}' from bucket '{bucket_name}' downloaded to '{local_file_path}'.")
    except Exception as e:
        print(f"Error downloading file from S3: {e}")

def delete_object(bucket_name, object_key):
    s3 = boto3.client('s3')
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' deleted from bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error deleting object from S3: {e}")

# Example usage:
bucket_name = 'your_bucket'
local_file_path = 'local_file_path/file.txt'
s3_file_path = 's3_path/file.txt'
object_key = 'object_path_and_name'

# Upload the file
upload_object(bucket_name, local_file_path, s3_file_path)

# Search for the object
search_object(bucket_name, object_key)

# Download the object
download_object(bucket_name, object_key, local_file_path)

# Delete the object
delete_object(bucket_name, object_key)
