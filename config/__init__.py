__author__ = 'kkboy'

import collections

''' global configs '''
prefix = "kkboy"
postfix = "aws"
key_name = "kkboy_ec2"
region = "us-west-2"

''' config format of instances in the same subnet with the same security_groups
    subnet_id : subnet id in which instances are allocated in
    security_group_ids : security group ids which are going to apply on instances
    key_name : key which is used to access instance (authentication)
    instances : attributes of instances whose data type is InstancesConf'''
InstancesGroup = collections.namedtuple("InstancesGroup", ["subnet_id", "security_group_ids", "key_name", "instances"])


''' config of instances in the same server role
    name : name of instance
    count : the amount to be launched with same attributes
    ami_id : AMI id which is ued to launch instance
    type : type of instance e.g. t2.micro
    disks : disks which is going to mount on the instance
    kargs : preserved parameter whose data type is dictionary
    please refer to following url for additional parameter
    http://boto3.readthedocs.org/en/latest/reference/services/ec2.html#EC2.Client.run_instances'''
InstancesConf = collections.namedtuple("InstancesConf", ["name",
                                                         "count",
                                                         "ami_id",
                                                         "type",
                                                         "disks",
                                                         "kargs"])
