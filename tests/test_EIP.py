__author__ = 'kkboy'

import boto
import boto.ec2
import boto.ec2.address
from util.auth import get_ec2_connection
from boto.ec2 import EC2Connection
from util.auth import aws_access_key_id, aws_secret_access_key

conn = boto.ec2.connect_to_region("us-west-2",
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)

nat_id = "i-53745296"
eip = conn.allocate_address()
eip.associate(nat_id)

from boto.ec2.address import Address