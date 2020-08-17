import logging


def get_logger():
    logger = logging.getLogger('battleship')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    file_handler = logging.FileHandler('battleship.log')
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
