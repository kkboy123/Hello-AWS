__author__ = 'kkboy'

import boto
from boto.ec2 import EC2Connection
from boto.vpc import VPCConnection
from config import region
import ConfigParser
import boto3
import logging

credentials = ConfigParser.ConfigParser()
credentials.readfp(open('D:\\AWS\\automa\\boto.ini'))
aws_access_key_id = credentials.get('Credentials', 'aws_access_key_id')
aws_secret_access_key = credentials.get('Credentials', 'aws_secret_access_key')


def get_vpc_connection():
    connection = boto.vpc.connect_to_region(region,
                                            aws_access_key_id=aws_access_key_id,
                                            aws_secret_access_key=aws_secret_access_key)
    return connection


def get_ec2_connection():
    connection = boto.ec2.connect_to_region(region,
                                            aws_access_key_id=aws_access_key_id,
                                            aws_secret_access_key=aws_secret_access_key)
    return connection


def get_ec2_client():
    logger = logging.getLogger(__name__)
    logger.info("get ec2 client")
    client = boto3.client('ec2',
                          region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    return client


def get_ec2_resource():
    logger = logging.getLogger(__name__)
    logger.info("get ec2 resource")
    resource = boto3.resource('ec2',
                              region,
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)
    return resource


def get_route53_client():
    logger = logging.getLogger(__name__)
    logger.info("get route53 client")
    client = boto3.client('route53',
                          region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    return client
