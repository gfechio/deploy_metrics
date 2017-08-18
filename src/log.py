import logging
import config
import os

if not os.path.isdir(config.log['dir']):
    os.makedirs(config.log['dir'])

output_file = config.log['file']
logger = logging.getLogger('deploy_manager')
hndlr = logging.FileHandler(output_file)
formatter = logging.Formatter('%(asctime)s %(message)s')
hndlr.setFormatter(formatter)
logger.addHandler(hndlr)
logger.setLevel(logging.INFO)
