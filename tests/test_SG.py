__author__ = 'kkboy'

from utils.auth import aws_access_key_id, aws_secret_access_key
from boto.ec2.securitygroup import SecurityGroup
from boto.ec2 import EC2Connection
import boto.vpc
from boto.vpc import VPCConnection
import collections


# # VPC connection
# conn = boto.vpc.connect_to_region("us-west-2",
#                                aws_access_key_id=aws_access_key_id,
#                                aws_secret_access_key=aws_secret_access_key)
#
#
# #def create_security_group():
# name = "kk_sg1"
# description = "testing sg1"
# vpc_id = "vpc-f76e2b92"
# sg = conn.create_security_group(name, description, vpc_id = "vpc-f76e2b92")
# print sg
# print sg.authorize('tcp', 80, 80, '0.0.0.0/0')


# security attributes
# rs = conn.get_all_security_groups()
# sg = rs[1]
# print "name : %s" % sg.name
# print "owner_id : %s" % sg.owner_id
# print "id : %s" % sg.id
# print "description : %s" % sg.description
# print "vpc_id : %s" % sg.vpc_id
# print "rules : %s" % sg.rules
# print "rules_egress : %s" % sg.rules_egress

SecurityGroupRule = collections.namedtuple("SecurityGroupRule", ["ip_protocol", "from_port", "to_port", "cidr_ip", "src_group_name"])

CASSANDRA_RULES = [
    SecurityGroupRule("tcp", "22", "22", "0.0.0.0/0", None),
    SecurityGroupRule("tcp", "1024", "65535", "0.0.0.0/0", "Cassandra Cluster"),
    SecurityGroupRule("tcp", "7000", "7000", "0.0.0.0/0", "Cassandra Cluster"),
    SecurityGroupRule("tcp", "61620", "61621", "0.0.0.0/0", "Cassandra Cluster"),
    SecurityGroupRule("tcp", "7199", "7199", "0.0.0.0/0", None),
    SecurityGroupRule("tcp", "8888", "8888", "0.0.0.0/0", None),
    SecurityGroupRule("tcp", "8983", "8983", "0.0.0.0/0", None),
    SecurityGroupRule("tcp", "9160", "9160", "0.0.0.0/0", None),
]

TEST_RULES = [
    # ssh makes life possible
    SecurityGroupRule("tcp", "22", "22", "0.0.0.0/0", None),
]

SECURITY_GROUPS = [("Cassandra Cluster", CASSANDRA_RULES),
                   ("Test", TEST_RULES)
                   ]
# for group_name, rules in SECURITY_GROUPS:
#     print group_name
#     for rule in rules:
#         print "rule-------------"
#         print rule.cidr_ip
#         print rule.from_port
#         print rule.to_port
#         print rule.ip_protocol
#         print rule.src_group_name
#         print "rule-------------"
#     print "============"