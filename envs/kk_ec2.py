__author__ = 'ken_chang'

import time
import logging
from envs import client, resource


def create_vpc(vpc_cidr, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        result = client.create_vpc(CidrBlock=vpc_cidr)
        vpc_id = result.get("Vpc").get("VpcId")
        logger.info("vpc id : %s" % vpc_id)
        logger.info("modify DNS setting")
        client.modify_vpc_attribute(VpcId=vpc_id,
                                    EnableDnsHostnames={'Value': True})
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            client.create_tags(Resources=[vpc_id],
                               Tags=[{"Key": "Name",
                                      "Value": tag_name}])
        logger.info("create internet gateway")
        result = client.create_internet_gateway()
        ig_id = result.get("InternetGateway").get("InternetGatewayId")
        logger.info("attach ig %s to VPC" % ig_id)
        client.attach_internet_gateway(InternetGatewayId=ig_id,
                                       VpcId=vpc_id)
        if tag_name is not None:
            logger.info("create tag Name : %s_GW" % tag_name)
            client.create_tags(Resources=[ig_id],
                               Tags=[{"Key": "Name",
                                      "Value": "%s_GW" % tag_name}])
        return vpc_id, ig_id
    except Exception, e:
        logger.error(e)


def create_subnet(vpc_id, subnet_cidr, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        result = client.create_subnet(VpcId=vpc_id,
                                      CidrBlock=subnet_cidr)
        subnet_id = result.get("Subnet").get("SubnetId")
        logger.info("subnet id : %s" % subnet_id)
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            client.create_tags(Resources=[subnet_id],
                               Tags=[{"Key": "Name",
                                      "Value": tag_name}])
        return subnet_id
    except Exception, e:
        logger.error(e)


def create_nat(ami_id, key_name, instance_type, security_group_ids, subnet_id, tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        logger.info("creating NAT instance")
        result = client.run_instances(ImageId=ami_id,
                                      MinCount=1,
                                      MaxCount=1,
                                      KeyName=key_name,
                                      SecurityGroupIds=security_group_ids,
                                      InstanceType=instance_type,
                                      SubnetId=subnet_id)
        nat_id = result.get("Instances")[0].get("InstanceId")
        logger.info("instance id : %s" % nat_id)
        if tag_name is not None:
            logger.info("create tag Name : %s" % tag_name)
            client.create_tags(Resources=[nat_id],
                               Tags=[{"Key": "Name",
                                      "Value": tag_name}])
        logger.debug("set sourceDestCheck false")
        client.modify_instance_attribute(InstanceId=nat_id,
                                         SourceDestCheck={'Value': False})
        # allocate Elastic IP
        logger.debug("allocate new EIP")
        result = client.allocate_address()
        eip = result.get("PublicIp")
        logger.debug("associate EIP")
        nat = resource.Instance(nat_id)
        while nat.state.get("Name") == "pending":
            logger.info(nat.state)
            time.sleep(5)
            nat = resource.Instance(nat_id)
        client.associate_address(InstanceId=nat_id,
                                 PublicIp=eip)
        logger.info("EIP of this NAT : %s" % eip)
        return nat_id
    except Exception, e:
        logger.error(e)


# setup default route and create customer route
def setup_route(vpc_id, nat_id, ig_id, gw_subnet_id, vpc_tag_name=None):
    logger = logging.getLogger(__name__)
    try:
        logger.info("get default route table")
        vpc = resource.Vpc(vpc_id)
        for default_rt in vpc.route_tables.all():
            default_rt.create_route(DestinationCidrBlock="0.0.0.0/0",
                                    InstanceId=nat_id)
        if vpc_tag_name is not None:
            logger.info("create tag Name : 'main_%s_route_table' of default gateway" % vpc_tag_name)
            default_rt.create_tags(Tags=[{"Key": "Name",
                                          "Value": "main_%s_route_table" % vpc_tag_name}])
        logger.info("create customer route table")
        result = client.create_route_table(VpcId=vpc_id)
        customer_rt_id = result.get("RouteTable").get("RouteTableId")
        logger.info("customer route table id : %s" % customer_rt_id)
        logger.info("create route to internet")
        client.create_route(RouteTableId=customer_rt_id,
                            DestinationCidrBlock="0.0.0.0/0",
                            GatewayId=ig_id)
        if vpc_tag_name is not None:
            logger.info("create tag Name : 'GW_%s_route_table' of customer gateway" % vpc_tag_name)
            client.create_tags(Resources=[customer_rt_id],
                               Tags=[{"Key": "Name",
                                      "Value": "GW_%s_route_table" % vpc_tag_name}])
        logger.info("associate route table to GW subnet")
        client.associate_route_table(SubnetId=gw_subnet_id,
                                     RouteTableId=customer_rt_id)
    except Exception, e:
        logger.error(e)