__author__ = 'kkboy'

import collections

''' global configs '''
prefix = "kkboy"
postfix = "aws"
key_name = "kkboy_ec2"
region = "us-west-2"

''' config format of instances in the same subnet with the same security_groups '''
InstancesGroup = collections.namedtuple("InstancesGroup", ["subnet", "security_groups", "instances"])

''' config of instances in the same server role'''
InstancesConf = collections.namedtuple("InstancesConf", ["name",
                                                         "count",
                                                         "ami_id",
                                                         "type",
                                                         "disks",
                                                         "kargs"])
