__author__ = 'kkboy'

import logging
from util.auth import get_vpc_connection
from config.security_group_conf import SECURITY_GROUPS


def create_security(vpv_id):
    logger = logging.getLogger(__name__)
    security_group_ids = []
    try:
        logger.debug("create VPC connection")
        c = get_vpc_connection()
        # create security groups base on config file
        for security_group in SECURITY_GROUPS:
            sg = c.create_security_group(security_group.security_group_name,
                                         security_group.description,
                                         vpc_id=vpv_id)
            logger.info("%s security group id : %s" % (security_group.security_group_name, sg.id))
            # setup inbound rule
            for rule in security_group.rules_in:
                sg.authorize(rule.ip_protocol,
                             rule.from_port,
                             rule.to_port,
                             rule.cidr_ip)
            logger.debug("%s rules_in is done" % security_group.security_group_name)
            # remove default outbound rule
            c.revoke_security_group_egress(sg.id,
                                           u"-1",
                                           from_port=None,
                                           to_port=None,
                                           cidr_ip="0.0.0.0/0")
            # setup outbound rule
            for rule in security_group.rules_out:
                c.authorize_security_group_egress(group_id=sg.id,
                                                  ip_protocol=rule.ip_protocol,
                                                  from_port=rule.from_port,
                                                  to_port=rule.to_port,
                                                  cidr_ip=rule.cidr_ip)
            logger.debug("%s rules_out is done" % security_group.security_group_name)
            logger.info("create tag Name : %s" % security_group.security_group_name)
            c.create_tags(sg.id,
                          {"Name": security_group.security_group_name})
            logger.info("%s is done" % security_group.security_group_name)
            security_group_ids.append(sg.id)
        logger.debug("close VPC connection")
        c.close()
    except Exception, e:
        logger.error(e)
    return security_group_ids


