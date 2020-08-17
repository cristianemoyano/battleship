import logging
from colorlog import ColoredFormatter

LOGFORMAT = "%(log_color)s %(levelname)s %(reset)s | %(log_color)s %(message)s %(reset)s"


class Singleton(object):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

class Logger(Singleton):

    def __init__(self):
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
        console_formatter = ColoredFormatter(LOGFORMAT)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        self.logger = logger


LOGGER = Logger().logger


def get_logger():
    return LOGGER
