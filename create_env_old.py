__author__ = 'kkboy'


from envs import kk_network
from envs import kk_security_group

# vpc_id = kk_network.old_create_vpc("10.0.0.0/24", "kkboy_vpc")

vpc_id = "vpc-f76e2b92"
# subnet_ids = []
# #public subnet
# subnet_ids.append(kk_network.old_create_subnet(vpc_id, "10.0.0.0/25", "kkboy_sn001"))
# # private subnet
# subnet_ids.append(kk_network.old_create_subnet(vpc_id, "10.0.0.128/25", "kkboy_sn002"))

subnet_ids = ["subnet-2aeea54f", "subnet-35eea550"]

#security_group_ids = kk_security_group.old_create_security(vpc_id)

security_group_ids = ["sg-73a92917", "sg-73a92917"]

# ami_id = "ami-290f4119"
# key_name = 'kkboy_ec2'
# nat_instance_type = 't2.micro'
# nat_private_ip_address = '10.0.0.25'
# nat_tag_name = "nat_test"
# nat_id = kk_network.old_create_nat_instance(ami_id,
#                                         key_name=key_name,
#                                         instance_type=nat_instance_type,
#                                         security_group_ids=[security_group_ids[0]],
#                                         subnet_id=subnet_ids[0],
#                                         private_ip_address=nat_private_ip_address,
#                                         tag_name=nat_tag_name)
nat_id = "i-53745296"

# ig_id = kk_network.olr_create_internet_gateway("kkboy_ig_testing")
ig_id = "igw-45da5620"
# kk_network.old_attach_internet_gateway_to_vpc(ig_id, vpc_id)


# result = kk_network.old_associate_new_eip_to_nat(nat_id)
# print result