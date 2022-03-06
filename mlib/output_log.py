from logging import getLogger

logger = getLogger(__name__)


def func():
    logger.debug('This is debug.')
    logger.info('This is info.')
    logger.warning('This is warning.')
    logger.error('This is error.')


def worker():
    logger.info('from worker')
