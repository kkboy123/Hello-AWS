__author__ = 'ken_chang'

import time
import logging
from envs import r53_client


def create_hosted_private_zone(vpc_id, domain_name):
    logger = logging.getLogger(__name__)
    try:
        logger.info("create private zone : %s" % domain_name)
        r53_client.create_hosted_zone(Name=domain_name,
                                      VPC={"VPCRegion": "us-west-2",
                                           "VPCId": vpc_id},
                                      CallerReference="DNS_%s" % int(time.time()),
                                      HostedZoneConfig={"Comment": domain_name})
    except Exception, e:
        logger.error(e)


def create_a_record():
    a = {"kkboy_01.kkboy.nabu.aws.": "172.16.0.128",
         "kkboy_02.kkboy.nabu.aws.": "172.16.0.129"}
    changes = [{"Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": key,
                    "Type": "A",
                    "TTL": 900,
                    "ResourceRecords": [{"Value": value}]}}
               for key, value in a.items()]
    r53_client.change_resource_record_sets(HostedZoneId="Z394D1T3CJSTRY",
                                           ChangeBatch={
                                               "Changes": changes})
