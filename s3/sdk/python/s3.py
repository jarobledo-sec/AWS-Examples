import logging
import boto3
from botocore.exceptions import ClientError
import sys
import random
import uuid

# https://builder.aws.com/content/2zYQkMbmrsxHPtT89s3teyKJh79/aws-tools-and-resources-python

def create_bucket(bucket_name, region):
    try:
        global client 
        client = boto3.client('s3', region_name=region)
        client.create_bucket(Bucket=bucket_name,
                            CreateBucketConfiguration={
                                'LocationConstraint': region})
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_file(file_name, bucket, object_name):

    try:
        response = client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if len(sys.argv) != 2:
    print("Include the name of the bucket eg. "+sys.argv[0]+" bucket_name")
    sys.exit(0)  
else:
    bucket_name = sys.argv[1]
    region = 'eu-west-3'
    if not (create_bucket(bucket_name, region)):
        print("Bucket was not created")
    else:
        print("Bucket'"+bucket_name+"' was created")

    number_of_files = random.randint(1,10)
    print(str(number_of_files)+" files created")

    for i in range(number_of_files):
        filename = "file_"+str(i)+".txt"
        output_path = "/tmp/"+filename
        
        # create a unique UUID
        unique_id = str(uuid.uuid4())
        with open(output_path, "w") as f:
            f.write(unique_id)

        if not(upload_file(output_path, bucket_name, filename)):
            print(filename+" has not been uploaded")
        else:
            print(filename+" has been uploaded")