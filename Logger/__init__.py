# -*- encoding:utf-8 -*-
import logging

def Logger(tp=None,filename=None):
    # create logger
    logger_name = "my_logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # create file handler
    handler = Handler(tp,file_path=filename)
    
    # add handler and formatter to logger
    logger.addHandler(handler)
    return logger


def Handler(tp,file_path):
    if tp == 'file':
         # create file handler
        handler = logging.FileHandler(file_path)
    else:
        handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # create formatter
    fmt = "%(asctime)-15s %(process)d [%(levelname)s]: %(message)s "
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)
    handler.setFormatter(formatter)

    return handler


# logger.debug('debug message')
# logger = Logger()
# logger = Logger()
# print(logger)
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
__all__ = ["Logger"]