import logging

logger = logging.getLogger('logConfig.core')


def run():
    logger.info('this is a logger test info')
    logger.debug('this is a logger test debug')
    logger.warning('this is a logger test warning')


def test():
    logger.info('ssssssssss')