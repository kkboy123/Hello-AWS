__author__ = 'ken_chang'

from config import prefix, postfix, key_name,InstancesGroup, InstancesConf

ami_id = ""
subnet_name = "%s_DAL" % prefix
security_group_names = ["%s_DAL" % prefix]

CFG_disk = {}
CFG = InstancesConf("DAL-CFG%(serial)02d-Beta", 1, ami_id, "m1.medium", CFG_disk, None)



DAL_GROUP = InstancesGroup()
