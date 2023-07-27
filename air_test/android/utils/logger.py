# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 11:28
# @File: logger.py
# @Software: PyCharm

import os
import datetime
import logging
import coloredlogs
from air_settings import AirSettings
from logging.handlers import TimedRotatingFileHandler

coloredlogs.DEFAULT_FIELD_STYLES = {
    "asctime": {"color": "green"},
    "hostname": {"color": "magenta"},
    "levelname": {"color": "green", "bold": True},
    "request_id": {"color": "yellow"},
    "name": {"color": "blue"},
    "programname": {"color": "cyan"},
    "threadName": {"color": "yellow"},
}


class Log(object):

    __instances = {}

    @classmethod
    def get_logger(cls, uid, name=os.path.abspath(__name__)):
        if name not in cls.__instances:
            log_dir = AirSettings.LOG_DIR + '/'
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            log_file = os.path.join(log_dir, uid + '.log')
            logger = logging.getLogger(name)
            fmt = '%(asctime)s [%(module)s] [%(funcName)s:%(lineno)s] [%(levelname)s] [%(threadName)s] %(message)s'
            formater = logging.Formatter(fmt)

            ch = logging.StreamHandler()
            ch.setLevel(Log.__get_log_level())
            ch.setFormatter(formater)
            logger.addHandler(ch)

            coloredlogs.install(fmt=fmt, level=Log.__get_log_level(), logger=logger)
            fh = TimedRotatingFileHandler(log_file, when='D', interval=1, backupCount=7, encoding='utf-8')
            fh.setLevel(Log.__get_log_level())
            fh.setFormatter(formater)
            logger.setLevel(Log.__get_log_level())
            logger.addHandler(fh)
            cls.__instances[name] = logger
        return cls.__instances[name]

    @staticmethod
    def __get_log_level():
        return logging.INFO


if __name__ == '__main__':
    Log.get_logger('ef49ac02-ab4f-11ed-a0fb-cc1531f44e9d888').error('loging test')
