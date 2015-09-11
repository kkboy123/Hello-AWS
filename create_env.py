__author__ = 'kkboy'


from envs import kk_network

#kk_network.create_vpc("10.0.0.0/24", "kkboy_vpc")






vpc_id = "vpc-f76e2b92"
kk_network.create_subnet(vpc_id, "10.0.0.0/25", "sn001")
