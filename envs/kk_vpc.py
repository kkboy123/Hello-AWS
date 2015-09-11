__author__ = 'kkboy'


import logging
from utils.auth import aws_access_key_id, aws_secret_access_key
import boto.vpc
from boto.vpc import VPCConnection


def create_vpc(vpc_cidr, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        if len(vpc_cidr) == 0:
            logger.error("VPC CIDR should not be empty")
            return
        logger.info("create VPC connection")
        c = boto.vpc.connect_to_region("us-west-2",
                                          aws_access_key_id=aws_access_key_id,
                                          aws_secret_access_key=aws_secret_access_key)
        vpc = c.create_vpc('10.0.0.0/24')
        logger.info("vpc id : %s" % vpc.id)
        logger.info("modify DNS setting")
        c.modify_vpc_attribute(vpc_id=vpc.id,
                               enable_dns_hostnames=True)
        if tag_name is not None:
            logger.info("create tag Name : %s" %tag_name)
            c.create_tags(vpc.id,
                          {"Name": tag_name})
        logger.info("close VPC connection")
        c.close()
    except Exception, e:
        logger.error(e)

