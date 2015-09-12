__author__ = 'kkboy'

from utils.auth import aws_access_key_id, aws_secret_access_key
from boto.ec2.securitygroup import SecurityGroup
from boto.ec2 import EC2Connection
import boto.vpc
from config.security_group_conf import SECURITY_GROUPS



# VPC connection
conn = boto.ec2.connect_to_region("us-west-2",
                               aws_access_key_id=aws_access_key_id,
                               aws_secret_access_key=aws_secret_access_key)

# name = "kk_sg1"
# description = "testing sg1"
# vpc_id = "vpc-f76e2b92"
for security_group in SECURITY_GROUPS:
    sg = conn.create_security_group(security_group.security_group_name,
                                    security_group.description,
                                    vpc_id="vpc-f76e2b92")
    print sg.id
    for rule in security_group.rules_in:
        sg.authorize(rule.ip_protocol,
                     rule.from_port,
                     rule.to_port,
                     rule.cidr_ip)
    print "rules_in is done"
    # remove default rule
    conn.revoke_security_group_egress(sg.id,
                                      u"-1",
                                      from_port=None,
                                      to_port=None,
                                      cidr_ip="0.0.0.0/0")
    for rule in security_group.rules_out:
        conn.authorize_security_group_egress(group_id=sg.id,
                                             ip_protocol=rule.ip_protocol,
                                             from_port=rule.from_port,
                                             to_port=rule.to_port,
                                             cidr_ip=rule.cidr_ip)
    print "%s is done" % security_group.security_group_name


# sg = conn.create_security_group(name, description, vpc_id = "vpc-f76e2b92")
# print sg
# print sg.authorize('tcp', 80, 80, '0.0.0.0/0')
# sg_id="sg-7e17961a"
# print conn.authorize_security_group_egress(group_id=sg_id,
#                                            ip_protocol="tcp",
#                                            from_port=80,
#                                            to_port=80,
#                                            cidr_ip="0.0.0.0/0")

# for security_group in SECURITY_GROUPS:
#     print security_group.security_group_name
#     print security_group.description
#     for rule in security_group.rules:
#         print "rule-------------"
#         print rule.cidr_ip
#         print rule.from_port
#         print rule.to_port
#         print rule.ip_protocol
#         print "rule-------------"
#     print "============"













# security attributes
#
# rs = conn.get_all_security_groups()
# sg = rs[1]
# print "name : %s" % sg.name
# print "owner_id : %s" % sg.owner_id
# print "id : %s" % sg.id
# print "description : %s" % sg.description
# print "vpc_id : %s" % sg.vpc_id
# print "rules : %s" % sg.rules
# #print "rules_egress : %s" % sg.rules_egress
# for rule in sg.rules_egress:
#     print type(u"-1")
#     print rule.from_port
#     print rule.to_port
#     print rule.grants[0].cidr_ip

