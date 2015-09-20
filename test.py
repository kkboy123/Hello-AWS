__author__ = 'kkboy'

# from config.dal_conf import security_group_ids, subnet_id
#
# print security_group_ids
# print subnet_id


from envs import kk_instance, kk_r53

#ids = kk_instance.create_instances("dal_conf")
results = kk_r53.create_a_record()
print results