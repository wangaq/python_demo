# init
import logging

import core

logger = logging.getLogger('logConfig')
logger.setLevel(level=logging.DEBUG)

# formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# fileHandler
file_handler = logging.FileHandler(filename='result.log')
file_handler.setFormatter(formatter)

# StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

core.run()