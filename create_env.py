__author__ = 'kkboy'

from utils.auth import aws_access_key_id, aws_secret_access_key
import boto.vpc
from boto.vpc import VPCConnection


c = boto.vpc.connect_to_region("us-west-2",
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)

# print "create VPC"
# vpc = c.create_vpc('10.0.0.0/24')
# print "vpc id : %s" % vpc.id
# print "modify DNS setting"
# c.modify_vpc_attribute(vpc_id=vpc.id,
#                        enable_dns_hostnames=True)

vip_id = "vpc-bc581dd9"
c.create_tags(vip_id,
              {"Name": "kkboy_VPC"})
# vpcs = c.get_all_vpcs()
# for vpc in vpcs:
#     print vpc.id
