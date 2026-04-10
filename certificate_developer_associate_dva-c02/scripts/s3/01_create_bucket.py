import boto3
 
s3_client = boto3.client('s3', region_name='us-east-1')
bucket_name = "sdk-bucket-moses-2026"
   
try:
    response = s3_client.create_bucket(
        Bucket=bucket_name
    )
    print(f"Bucket created successfully.")
except Exception as e:
    print(f"Error creating bucket: {e}")