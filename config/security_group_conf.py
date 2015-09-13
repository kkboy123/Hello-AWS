__author__ = 'kkboy'

import collections

SecurityGroupRule = collections.namedtuple("SecurityGroupRule", ["ip_protocol", "from_port", "to_port", "cidr_ip"])

CASSANDRA_RULES = [
    SecurityGroupRule("tcp", "22", "22", "0.0.0.0/0"),
    SecurityGroupRule("tcp", "1024", "65535", "0.0.0.0/0"),
    SecurityGroupRule("tcp", "7000", "7000", "0.0.0.0/0",),
    SecurityGroupRule("tcp", "61620", "61621", "0.0.0.0/0"),
    SecurityGroupRule("tcp", "7199", "7199", "0.0.0.0/0",),
    SecurityGroupRule("tcp", "8888", "8888", "0.0.0.0/0",),
    SecurityGroupRule("tcp", "8983", "8983", "0.0.0.0/0",),
    SecurityGroupRule("tcp", "9160", "9160", "0.0.0.0/0",),
]

TEST_RULES = [
    SecurityGroupRule("tcp", "22", "22", "0.0.0.0/0"),
]

SecurityGroup = collections.namedtuple("SecurityGroup", ["security_group_name", "description", "rules_in", "rules_out"])

SECURITY_GROUPS = [
    # gw
    SecurityGroup("Test", "Test description", TEST_RULES, TEST_RULES),
    # others
    SecurityGroup("Cassandra Cluster", "Cassandra Cluster description", CASSANDRA_RULES, CASSANDRA_RULES),
]
