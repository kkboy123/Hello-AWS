__author__ = 'ken_chang'

from envs import kk_ec2, kk_security, kk_r53
from config.domain_conf import vpc_domain_name
from config.vpc_conf import vpc_conf, subnets_conf, nat_config, customer_rt_cong


''' create VPC'''
vpc_id, ig_id = kk_ec2.create_vpc(vpc_conf.cidr, vpc_conf.tag_name)

'''create subnets based on config and save id of subnets'''
my_subnets_conf = {}
for subnet_name, subnet_conf in subnets_conf.items():
    subnet_id = kk_ec2.create_subnet(vpc_id,
                                     subnet_conf.cidr,
                                     subnet_conf.tag_name)
    my_subnets_conf[subnet_name] = subnet_id

''' create security group based on config'''
my_security_group = kk_security.create_security_group(vpc_id)

'''create a NAT instance'''
nat_id = kk_ec2.create_nat(nat_config.ami_id,
                           nat_config.key_name,
                           nat_config.instance_type,
                           [my_security_group.get(nat_config.security_group_names)],
                           my_subnets_conf.get(nat_config.subnet_names),
                           nat_config.tag_name)

'''setup routes'''
kk_ec2.setup_route(vpc_id, nat_id, ig_id, my_subnets_conf.get(customer_rt_cong.get("subnet_name")), vpc_conf.tag_name)

''' create hosted private zone '''
kk_r53.create_hosted_private_zone(vpc_id, vpc_domain_name)
