__author__ = 'kkboy'

from utils.auth import aws_access_key_id, aws_secret_access_key
import boto.vpc
from boto.vpc import VPCConnection
import logging.config
from envs import kk_vpc

kk_vpc.create_vpc("10.0.0.0/24", "kkboy_vpc")





# c = boto.vpc.connect_to_region("us-west-2",
#                                   aws_access_key_id=aws_access_key_id,
#                                   aws_secret_access_key=aws_secret_access_key)



# vpcs = c.get_all_vpcs()
# for vpc in vpcs:
#     print vpc.id

