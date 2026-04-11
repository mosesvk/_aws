from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3

class MyFirstStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        s3.Bucket(self, "MyFirstBucket")