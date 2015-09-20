__author__ = 'ken_chang'

import boto3
from boto3.session import Session
from util.auth import aws_access_key_id, aws_secret_access_key

client = boto3.client('ec2',
                      "us-west-2",
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
vpc = client.create_vpc(CidrBlock='172.16.0.0/16')
print vpc