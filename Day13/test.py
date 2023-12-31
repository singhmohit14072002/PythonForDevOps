
import boto3


client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='mohit-demo-bucket-test',
)

print(response)