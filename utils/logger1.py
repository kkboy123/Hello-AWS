__author__ = 'kkboy'


import logging

logger = logging.getLogger("logger1")
logger.setLevel(logging.INFO)

# Produce formater first
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Setup Stream Handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
# Setup File Handler
log_file = logging.FileHandler('../logs/test.log')
log_file.setLevel(logging.INFO)
log_file.setFormatter(formatter)
# Setup Logger
logger.addHandler(console)
logger.addHandler(log_file)

logger.info("xxxx")
logger.info("ddddd")


