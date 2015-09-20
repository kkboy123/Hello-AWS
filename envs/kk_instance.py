__author__ = 'kkboy'

import os
import sys
import time
import logging
import importlib
from envs import client, resource


def create_instances(conf_name):
    logger = logging.getLogger(__name__)
    #try:
    ''' dynamic loading configs based on input '''
    sys.path.append(os.path.join(os.path.dirname(__file__), "../config"))
    _module = importlib.import_module(conf_name)
    logger.info("config file %s loaded" % conf_name)
    logger.info("retrieve group info")
    subnet_id = _module.GROUP.subnet_id
    logger.info("subnet id : %s" % subnet_id)
    security_group_ids = _module.GROUP.security_group_ids
    logger.info("security group ids : %s" % security_group_ids)
    key_name = _module.GROUP.key_name
    logger.info("key name  : %s" % key_name)
    logger.info("retrieve instances info")
    instance_ids = []
    _dns_mapping = {}
    for instance in _module.GROUP.instances:
        ami_id = instance.ami_id
        logger.info("ami id : %s" % ami_id)
        instance_type = instance.type
        logger.info("instance type : %s" % instance_type)
        disks = instance.disks
        logger.info("disks info : %s" % disks)
        name = instance.name
        count = instance.count
        from_name = name % 1
        to_name = name % count
        logger.info("launching instances %s to %s " % (from_name, to_name))
        kargs = instance.kargs
        result = client.run_instances(ImageId=ami_id,
                                      MinCount=count,
                                      MaxCount=count,
                                      KeyName=key_name,
                                      SecurityGroupIds=security_group_ids,
                                      InstanceType=instance_type,
                                      SubnetId=subnet_id,
                                      BlockDeviceMappings=disks,
                                      **kargs)
        instance_ids.extend([Instance.get("InstanceId") for Instance in result.get("Instances")])
        private_ips = [Instance.get("PrivateIpAddress") for Instance in result.get("Instances")]
        logger.info("instance ids : %s" % instance_ids)
        logger.info("private ips : %s" % private_ips)
        for serial in range(0, count):
            _dns_mapping[name % (serial+1)] = private_ips[serial]
            logger.info("create tag Name of instance: %s" % instance_ids[serial])
            client.create_tags(Resources=[instance_ids[serial]],
                               Tags=[{"Key": "Name",
                                      "Value": name % (serial+1)}])
    ''' to do add records to r53'''
    logger.info(_dns_mapping)
    return instance_ids
    # except Exception, e:
    #     logger.error(e)
