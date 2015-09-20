__author__ = 'kkboy'

# from config.dal_conf import security_group_ids, subnet_id
#
# print security_group_ids
# print subnet_id


from envs import kk_instance

ids = kk_instance.create_instances("dal_conf")
