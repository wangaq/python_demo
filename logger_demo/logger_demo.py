import logging

# init
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# fileHandler
file_handler = logging.FileHandler(filename='logger.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Log
logger.info('start')
#logger.warn('this is a warn')
logger.warning('this is a warnning')

try:
    10/0
except Exception:
    logger.error('this is a error', exc_info=True)
logger.info('finish')

