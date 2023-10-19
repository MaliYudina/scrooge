import logging
from logging.config import fileConfig
import os


def setup_logger():
    logfilename = "investor_log.log"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # print(current_dir)
    config_file = 'log_config.ini'
    config_file_path = os.path.join(current_dir, config_file)
    logging.config.fileConfig(config_file_path, defaults={'logfilename': logfilename},
                              disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    return logger


if __name__ == '__main__':
    logger = setup_logger()
    logger.info('logger setup success')


