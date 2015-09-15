__author__ = 'kkboy'

import logging
from util.auth import get_vpc_connection
from util.auth import get_ec2_connection


def create_vpc(vpc_cidr, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        logger.debug("create VPC connection")
        c = get_vpc_connection()
        vpc = c.create_vpc(vpc_cidr)
        logger.info("vpc id : %s" % vpc.id)
        logger.info("modify DNS setting")
        c.modify_vpc_attribute(vpc_id=vpc.id,
                               enable_dns_hostnames=True)
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            c.create_tags(vpc.id,
                          {"Name": tag_name})
        logger.debug("close VPC connection")
        c.close()
        return vpc.id
    except Exception, e:
        logger.error(e)


def create_subnet(vpc_id, subnet_cidr, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        logger.debug("create VPC connection")
        c = get_vpc_connection()
        subnet = c.create_subnet(vpc_id, subnet_cidr)
        logger.info("subnet id : %s" % subnet.id)
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            c.create_tags(subnet.id,
                          {"Name": tag_name})
        logger.debug("close VPC connection")
        c.close()
        return subnet.id
    except Exception, e:
        logger.error(e)


def create_nat_instance(ami_id, key_name, instance_type, security_group_ids,
                        subnet_id, private_ip_address, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        logger.debug("create EC2 connection")
        c = get_ec2_connection()
        reservation = c.run_instances(ami_id,
                                      key_name=key_name,
                                      instance_type=instance_type,
                                      security_group_ids=security_group_ids,
                                      subnet_id=subnet_id,
                                      private_ip_address=private_ip_address)
        instance_id = reservation.instances[0].id
        logger.info("NAT instance id is : %s" % instance_id)
        logger.debug("set sourceDestCheck false")
        c.modify_instance_attribute(instance_id,
                                    "sourceDestCheck",
                                    False)
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            c.create_tags(instance_id,
                          tags={"Name": "nat_testing"})
        logger.debug("close EC2 connection")
        c.close()
        return instance_id
    except Exception, e:
        logger.error(e)


def create_internet_gateway(tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        logger.debug("create VPC connection")
        c = get_vpc_connection()
        ig = c.create_internet_gateway()
        logger.info("ig id : %s" % ig.id)
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            c.create_tags(ig.id,
                          {"Name": tag_name})
        logger.debug("close VPC connection")
        c.close()
        return ig.id
    except Exception, e:
        logger.error(e)


def attach_internet_gateway_to_vpc(ig_id, vpc_id):
    logger = logging.getLogger(__name__)
    try:
        logger.debug("create VPC connection")
        c = get_vpc_connection()
        logger.info("attaching ig %s to vpc %s " % (ig_id, vpc_id))
        c.attach_internet_gateway(ig_id, vpc_id)
        logger.debug("close VPC connection")
        c.close()
    except Exception, e:
        logger.error(e)
