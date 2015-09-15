__author__ = 'kkboy'


from util.auth import aws_access_key_id, aws_secret_access_key
import boto.ec2

# connect to us-west-2 with key pairs which is stored in local
conn = boto.ec2.connect_to_region("us-west-2",
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)

conn.run_instances('ami-d5c5d1e5',
                   key_name='kkboy_ec2',
                   instance_type='t2.micro',
                   security_groups=['kkboy_sg'])
