__author__ = 'kkboy'


from envs import kk_network
from envs import kk_security_group

# vpc_id = kk_network.create_vpc("10.0.0.0/24", "kkboy_vpc")

vpc_id = "vpc-f76e2b92"
# subnet_ids = []
# subnet_ids.append(kk_network.create_subnet(vpc_id, "10.0.0.0/25", "kkboy_sn001"))
# subnet_ids.append(kk_network.create_subnet(vpc_id, "10.0.0.128/25", "kkboy_sn002"))

subnet_ids = ["subnet-2aeea54f", "subnet-35eea550"]

security_group_ids = kk_security_group.create_security(vpc_id)
