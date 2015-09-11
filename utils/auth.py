__author__ = 'kkboy'

import csv
# get key pair from files
with open('D:/AWS/automa/credentials.csv', 'rb') as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in spamReader:
        aws_access_key_id = row[0]
        aws_secret_access_key = row[1]