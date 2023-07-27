# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/5/8 11:38
# @File: logger.py
# @Software: PyCharm

import os
import datetime
import logging
import coloredlogs
from settings import Config
from logging.handlers import TimedRotatingFileHandler


coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'hostname': {'color': 'magenta'},
                                    'levelname': {'color': 'green', 'bold': True}, 'request_id': {'color': 'yellow'},
                                    'name': {'color': 'blue'}, 'programname': {'color': 'cyan'},
                                    'threadName': {'color': 'yellow'}}


class Log(object):

    __instances = {}

    @classmethod
    def get_logger(cls, name=os.path.abspath(__name__)):
        if name not in cls.__instances:
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            if not os.path.exists(Config.LOG_DIR):
                os.makedirs(Config.LOG_DIR)
            log_file = os.path.join(Config.LOG_DIR, today + '.log')
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
    Log.get_logger().error('loging test')
    Log.get_logger().warning('loging test')
