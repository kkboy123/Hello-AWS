__author__ = 'kkboy'

import logging
from config.security_group_conf import SECURITY_GROUPS
from envs import client, resource


def create_security_group(vpc_id):
    logger = logging.getLogger(__name__)
    _security_group = {}
    try:
        # create security groups base on config file
        for security_group in SECURITY_GROUPS:
            result = client.create_security_group(GroupName=security_group.security_group_name,
                                                  Description=security_group.description,
                                                  VpcId=vpc_id)
            sg_id = result.get("GroupId")
            logger.info("%s security group id : %s" % (security_group.security_group_name, sg_id))
            logger.info("create tag Name : %s" % security_group.security_group_name)
            client.create_tags(Resources=[sg_id],
                               Tags=[{"Key": "Name",
                                      "Value": security_group.security_group_name}])
            sg = resource.SecurityGroup(sg_id)
            # setup inbound rule
            for rule in security_group.rules_in:
                sg.authorize_ingress(GroupId=sg_id,
                                     IpProtocol=rule.ip_protocol,
                                     FromPort=rule.from_port,
                                     ToPort=rule.to_port,
                                     CidrIp=rule.cidr_ip)
            logger.debug("%s rules_in is done" % security_group.security_group_name)
            # ----AWS bug egress rule can't be setup
            # # remove default outbound rule
            # client.revoke_security_group_egress(GroupId=sg_id,
            #                                     IpProtocol=u"-1",
            #                                     CidrIp=u"0.0.0.0/0")
            # # setup outbound rule
            # for rule in security_group.rules_out:
            #     sg.authorize_egress(GroupId=sg_id,
            #                         IpProtocol=rule.ip_protocol,
            #                         FromPort=rule.from_port,
            #                         ToPort=rule.to_port,
            #                         CidrIp=rule.cidr_ip)
            # logger.debug("%s rules_in is done" % security_group.security_group_name)
            _security_group[security_group.security_group_name] = sg_id
        return _security_group
    except Exception, e:
        logger.error(e)
