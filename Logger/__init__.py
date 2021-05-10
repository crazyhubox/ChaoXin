# -*- encoding:utf-8 -*-
import logging

def Logger(tp=None,filename=None):
    # create logger
    logger_name = "my_logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # create file handler
    handler = Handler(tp,filename=filename)
    # create formatter
    fmt = "%(asctime)-15s %(process)d [%(levelname)s]: %(message)s "
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    # add handler and formatter to logger
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def Handler(tp,filename):
    if tp == 'file':
         # create file handler
        log_path = f"./{filename}"
        handler = logging.FileHandler(log_path)
    else:
        handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    return handler

    
__all__ = ["Logger"]

# print log info
# logger.debug('debug message')
# logger = Logger()
# logger = Logger()
# print(logger)
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
