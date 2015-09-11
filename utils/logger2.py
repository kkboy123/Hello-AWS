__author__ = 'kkboy'


import logging
import logging.config

logging.config.fileConfig("../config/logging.conf")
logger = logging.getLogger("kkboyAWS")
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger.info('Protocol problem: %s', 'connection reset', extra=d)
#http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python
