__author__ = 'kkboy'


import csv
import boto.ec2

with open('D:/AWS/automa/credentials.csv', 'rb') as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in spamReader:
        aws_access_key_id = row[0]
        aws_secret_access_key = row[1]

conn = boto.ec2.connect_to_region("us-west-2", aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)

