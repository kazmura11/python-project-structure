# coding: utf-8
import logging
from logging.handlers import TimedRotatingFileHandler

log_format = logging.Formatter(
    '%(asctime)s %(levelname)-8s [%(module)s#%(funcName)s %(lineno)d] %(message)s')


def log_init_console(name, loglevel):
    return log_init(name, loglevel, True, False, None)


def log_init_console_file(name, loglevel, logpath):
    return log_init(name, loglevel, True, True, logpath)


def log_init(name, loglevel, use_console, use_file, logpath):
    logger = logging.getLogger(name)
    logger.setLevel(loglevel)

    if use_console:
        sh = logging.StreamHandler()
        sh.setLevel(loglevel)
        sh.setFormatter(log_format)
        logger.addHandler(sh)

    if use_file:
        fh = TimedRotatingFileHandler(logpath, when="D", interval=1, backupCount=7)
        fh.setLevel(loglevel)
        fh.setFormatter(log_format)
        logger.addHandler(fh)
    
    return logger
