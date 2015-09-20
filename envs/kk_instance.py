__author__ = 'kkboy'

import os
import sys
import time
import logging
import importlib
from envs import client, resource


def create_nat(conf_name):
    logger = logging.getLogger(__name__)
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), "../config"))
        print sys.path
        _module = importlib.import_module(conf_name)
        logger.info("creating DAL instances")
        result = client.run_instances(ImageId=ami_id,
                                      MinCount=1,
                                      MaxCount=1,
                                      KeyName=key_name,
                                      SecurityGroupIds=security_group_ids,
                                      InstanceType=instance_type,
                                      SubnetId=subnet_id)
        nat_id = result.get("Instances")[0].get("InstanceId")
        logger.info("instance id : %s" % nat_id)
        # if tag_name is not None:
        #     logger.info("create tag Name : %s" % tag_name)
        #     client.create_tags(Resources=[nat_id],
        #                        Tags=[{"Key": "Name",
        #                               "Value": tag_name}])

        return nat_id
    except Exception, e:
        logger.error(e)
