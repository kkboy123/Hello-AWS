__author__ = 'kkboy'

import boto
import boto.vpc
from utils.auth import get_ec2_connection
from boto.vpc import VPCConnection
from utils.auth import aws_access_key_id, aws_secret_access_key

conn = boto.vpc.connect_to_region("us-west-2",
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)

from boto.vpc.internetgateway import InternetGateway

vpc_id = "vpc-f76e2b92"
ig = conn.create_internet_gateway()
conn.attach_internet_gateway(ig.id,vpc_id)
