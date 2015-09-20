__author__ = 'ken_chang'

import importlib
import sys
import os

print sys.path


def test_f():
    sys.path.append(os.path.join(os.path.dirname(__file__), "../config"))
    print sys.path
    my_module = importlib.import_module('vpc_conf')
    print my_module.vpc_conf.cidr
    # modules = map(__import__, ["vpc_conf"])
    # print modules.count()


