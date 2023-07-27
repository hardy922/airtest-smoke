# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/13 15:22
# @File: air_settings.py
# @Software: PyCharm

import os
import time


class AirSettings(object):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    AIR_BASE = os.path.join(BASE_DIR, 'air_test')

    # 手游配置
    AIR_ANDROID = os.path.join(AIR_BASE, 'android')
    LOG_DIR = os.path.join(AIR_ANDROID, 'logs')
    SRC_DIR = os.path.join(AIR_ANDROID, 'src')
    CASE_DATA = os.path.join(SRC_DIR, 'case_data')
    CASE = os.path.join(AIR_ANDROID, 'cases')
    ANDROID_RESULT = os.path.join(AIR_ANDROID, 'result')

    ADB_PORT = 5555

    PACKAGE = 'com.demo'
    ACTIVITY = 'com.demo.GameStartActivity'

    OCR = 'http://10.86.1.38/api/v1/ocr'

    STOP_GAME = 'http://api-xxx.com/v1/servo/stop'

    @classmethod
    def ocr_body(cls, base, thresh):
        bd = {
            "image": base,
            "thresh": thresh
        }
        return bd

    @classmethod
    def time_now(cls):
        return time.strftime('%Y%m%d%H%M%S')

    @classmethod
    def stop_game_body(cls, user, gid, biz):
        bd = {
            "app_userid": user,
            "gid": gid,
            "app_biz_type": int(biz)
        }
        return bd
