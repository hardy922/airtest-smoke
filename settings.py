# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2022/11/21 18:13
# @File: settings.py
# @Software: PyCharm


import os.path


class Config(object):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    TEMP = os.path.join(STATIC_DIR, 'temp')

    # AIR
    AIR_BASE = os.path.join(BASE_DIR, 'air_test')
    AIR_ANDROID = os.path.join(AIR_BASE, 'android')
    ANDROID_LOG = os.path.join(AIR_ANDROID, 'logs')

    AIR_WINDOWS = os.path.join(AIR_BASE, 'windows')

    # 截图信息
    ANDROID_SRC = os.path.join(STATIC_DIR, 'src')
    # 截图路径
    SRC_SCREEN = os.path.join(ANDROID_SRC, 'png')
    # 临时用例
    SRC_CASE = os.path.join(ANDROID_SRC, 'case')

