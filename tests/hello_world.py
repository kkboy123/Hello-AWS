__author__ = 'ken_chang'

from util.auth import aws_access_key_id, aws_secret_access_key
import boto.ec2
from boto.vpc import VPCConnection


vpc_conn = boto.vpc.connect_to_region("us-west-2",
                                      aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key)

vpc = vpc_conn.create_vpc('172.34.0.0/16')
print vpc.id
print vpc.state
print vpc.dhcp_options_id

subnet = vpc_conn.create_subnet(vpc.id, '172.34.0.0/24', 'us-west-2a')
print subnet.id
print subnet.state
print subnet.cidr_block
print subnet.availability_zone

subnet = vpc_conn.create_subnet(vpc.id, '172.34.1.0/24', 'us-west-2b')
print subnet.id
print subnet.state
print subnet.cidr_block
print subnet.availability_zone

subnet = vpc_conn.create_subnet(vpc.id, '172.34.2.0/24', 'us-west-2c')
print subnet.id
print subnet.state
print subnet.cidr_block
print subnet.availability_zone
