__author__ = 'ken_chang'

import json
''' load common configs
    you can overwrite it'''
from config import prefix, postfix, key_name,InstancesGroup, InstancesConf


''' read vpc configs from specific file for further retrieval '''
with open('config/kkboy_vpc_conf.json') as data_file:
    ec2_conf = json.load(data_file)


''' default AMI id used to launch instances '''
common_ami_id = "ami-d5c5d1e5"


''' default subnet name which is used to retrieve default subnet_id '''
subnet_name = "%s_DAL" % prefix
subnet_id = ec2_conf.get("subnets").get(subnet_name)


''' default security groups which are used to retrieve default security_group_ids '''
security_group_names = ["%s_DAL" % prefix]
security_group_ids = [ec2_conf.get("security_groups").get(name) for name in security_group_names]


''' following are instance configs '''

# CFG_disk = [{"DeviceName": "/dev/sdb", "Ebs": {"VolumeSize": 10}}]
CFG_disk = [{"DeviceName": "/dev/xvda", "Ebs": {"VolumeSize": 10, "VolumeType": "gp2"}}]
CFG = InstancesConf("DAL-CFG%02d-Beta", 1, common_ami_id, "t2.micro", CFG_disk, {})

AP_disk = [{"DeviceName": "/dev/xvda", "Ebs": {"VolumeSize": 10, "VolumeType": "gp2"}}]
AP = InstancesConf("DAL-AP%02d-Beta", 6, common_ami_id, "t2.micro", CFG_disk, {})


''' the parameter name should be "GROUP" !!!!! '''
GROUP = InstancesGroup(subnet_id, security_group_ids, key_name, [CFG, AP])
