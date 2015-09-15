__author__ = 'kkboy'
import boto
import boto.ec2
from util.auth import get_ec2_connection
from boto.ec2 import EC2Connection
from util.auth import aws_access_key_id, aws_secret_access_key


ami_id = "ami-290f4119"
#conn = get_ec2_connection()
conn = boto.ec2.connect_to_region("us-west-2",
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)
#sg_name = ["Test"]
subnet_id = "subnet-2aeea54f"
reservation = conn.run_instances(ami_id,
                                 key_name='kkboy_ec2',
                                 instance_type='t2.micro',
                                 security_group_ids=['sg-73a92917'],
                                 subnet_id='subnet-2aeea54f',
                                 private_ip_address='10.0.0.25')
instance_id = reservation.instances[0].id
conn.modify_instance_attribute(instance_id,
                               "sourceDestCheck",
                               False)
conn.create_tags(instance_id,
                 tags={"Name": "nat_testing"})