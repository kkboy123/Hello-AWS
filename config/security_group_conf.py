__author__ = 'kkboy'

import collections
from config.vpc_conf import vpc_conf
from config import prefix, postfix

''' security group rule data structure'''
SecurityGroupRule = collections.namedtuple("SecurityGroupRule", ["ip_protocol", "from_port", "to_port", "cidr_ip"])

''' security group data structure'''
SecurityGroup = collections.namedtuple("SecurityGroup", ["security_group_name", "description", "rules_in", "rules_out"])

'''gateway inbound rule'''
GW_inrules =[SecurityGroupRule("tcp", 22, 22, "0.0.0.0/0"),
             SecurityGroupRule("tcp", 53, 53, vpc_conf.cidr),
             SecurityGroupRule("udp", 53, 53, vpc_conf.cidr),
             SecurityGroupRule("tcp", 80, 80, vpc_conf.cidr),
             SecurityGroupRule("tcp", 443, 443, vpc_conf.cidr),
             SecurityGroupRule("icmp", -1, -1, vpc_conf.cidr)]

'''gateway outbound rule'''
GW_outrules =[SecurityGroupRule("icmp", -1, -1, "0.0.0.0/0"),
              SecurityGroupRule("tcp", 53, 53, "0.0.0.0/0"),
              SecurityGroupRule("udp", 53, 53, "0.0.0.0/0"),
              SecurityGroupRule("tcp", 80, 80, "0.0.0.0/0"),
              SecurityGroupRule("http", 443, 443, "0.0.0.0/0"),
              SecurityGroupRule("-1", -1, -1, vpc_conf.cidr)]

'''public ELB inbound rule'''
PUBLIC_ELB_inrule = [SecurityGroupRule("tcp", 80, 80, "0.0.0.0/0"),
                     SecurityGroupRule("tcp", 443, 443, "0.0.0.0/0")]

'''public ELB outbound rule'''
PUBLIC_ELB_outrule = None

'''other inbound rule'''
OTHERS_inrule = [SecurityGroupRule("-1", -1, -1, vpc_conf.cidr)]

'''other outbound rule'''
OTHERS_outrule = None

'''security groups to be initialized'''
SECURITY_GROUPS = [SecurityGroup("%s_GW" % prefix, "GW desc", GW_inrules, GW_outrules),
                   SecurityGroup("%s_PS" % prefix, "PS desc", OTHERS_inrule, OTHERS_inrule),
                   SecurityGroup("%s_SCO" % prefix, "SCO desc", OTHERS_inrule, OTHERS_inrule),
                   SecurityGroup("%s_DAL" % prefix, "DAL desc", OTHERS_inrule, OTHERS_inrule),
                   SecurityGroup("%s_Public_ELB" % prefix, "PS desc", PUBLIC_ELB_inrule, PUBLIC_ELB_outrule)]
