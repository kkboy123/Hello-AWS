__author__ = 'kkboy'

import csv
import boto
# get key pair from files
with open('D:/AWS/automa/credentials.csv', 'rb') as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in spamReader:
        aws_access_key_id = row[0]
        aws_secret_access_key = row[1]


def get_vpc_connection():
    connection = boto.vpc.connect_to_region("us-west-2",
                                            aws_access_key_id=aws_access_key_id,
                                            aws_secret_access_key=aws_secret_access_key)
    return connection


def get_ec2_connection():
    connection = boto.ec2.connect_to_region("us-west-2",
                                            aws_access_key_id=aws_access_key_id,
                                            aws_secret_access_key=aws_secret_access_key)
    return connection
