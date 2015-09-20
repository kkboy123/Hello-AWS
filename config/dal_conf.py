__author__ = 'ken_chang'

''' load common configs
    you can overwrite it'''
from config import prefix, postfix, key_name,InstancesGroup, InstancesConf

common_ami_id = ""
subnet_name = "%s_DAL" % prefix
security_group_names = ["%s_DAL" % prefix]

CFG_disk = {}
CFG = InstancesConf("DAL-CFG%(serial)02d-Beta", 1, common_ami_id, "m3.medium", CFG_disk, None)



GROUP = InstancesGroup()
