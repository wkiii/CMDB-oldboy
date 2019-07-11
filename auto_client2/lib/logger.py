import logging
from conf import settings


class Logger():
    def __init__(self, file_path, log_name, level=logging.DEBUG):
        file_handler = logging.FileHandler(file_path, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        file_handler.setFormatter(fmt)
        
        self.logger = logging.Logger(log_name, level=level)
        self.logger.addHandler(file_handler)
    
    def debug(self, msg):
        self.logger.debug(msg)
    
    def error(self, msg):
        self.logger.error(msg)


logger = Logger(settings.LOGGER_PATH, settings.LOGGER_NAME, settings.LOGGER_LEVEL)
