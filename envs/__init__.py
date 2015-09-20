__author__ = 'kkboy'

import logging.config
from util.auth import get_ec2_client, get_ec2_resource, get_route53_client

logging.config.fileConfig("./config/logging.conf")

client = get_ec2_client()
resource = get_ec2_resource()
r53_client = get_route53_client()