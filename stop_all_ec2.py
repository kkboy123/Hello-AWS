__author__ = 'ken_chang'

from utils.auth import aws_access_key_id, aws_secret_access_key
import boto.vpc
from boto.ec2.instance import Reservation

ec2_conn = boto.ec2.connect_to_region("us-west-2",
                                      aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key)
reservations = ec2_conn.get_all_reservations()
instance_ids = [instance.id for instances in reservations for instance in instances.instances 
                if instance.state == "running"]
if len(instance_ids) > 0:
    ec2_conn.stop_instances(instance_ids=instance_ids)

