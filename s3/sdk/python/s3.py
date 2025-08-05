import logging
import boto3
from botocore.exceptions import ClientError
import sys

# https://builder.aws.com/content/2zYQkMbmrsxHPtT89s3teyKJh79/aws-tools-and-resources-python

def create_bucket(bucket_name, region):
    try:
        client = boto3.client('s3', region_name=region)
        client.create_bucket(Bucket=bucket_name,
                            CreateBucketConfiguration={
                                'LocationConstraint': region})
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

