__author__ = 'ken_chang'

import collections
from config import prefix, postfix

NetworkConf = collections.namedtuple("NetworkConf", ["cidr", "tag_name"])

''' VPC config'''
vpc_conf = NetworkConf("172.16.0.0/16", "%s_VPC" % prefix)
'''
subnet config
first subnet should be public
'''

subnets_conf = {"%s_GW" % prefix: NetworkConf("172.16.0.0/24", "%s_GW" % prefix),
                "%s_PS" % prefix: NetworkConf("172.16.1.0/24", "%s_PS" % prefix),
                "%s_SCO" % prefix: NetworkConf("172.16.2.0/24", "%s_SCO" % prefix),
                "%s_DAL" % prefix: NetworkConf("172.16.3.0/24", "%s_DAL" % prefix)}


NatConf = collections.namedtuple("NatConf", ["ami_id",
                                             "key_name",
                                             "instance_type",
                                             "security_group_names",
                                             "subnet_names",
                                             "tag_name"])
''' NAT config '''
nat_config = NatConf("ami-290f4119",
                     "kkboy_ec2",
                     "t2.micro",
                     "%s_GW" % prefix,
                     "%s_GW" % prefix,
                     "%s_nat" % prefix,)

''' customer route config '''
customer_rt_cong = {"subnet_name": "%s_GW" % prefix}