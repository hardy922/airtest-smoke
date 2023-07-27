# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 14:25
# @File: driver.py
# @Software: PyCharm


import unittest
from air_settings import AirSettings
from air_test.android.utils.logger import Log
from air_test.android.utils.common.android import Android


class Driver(unittest.TestCase):

    driver = None
    poco = None
    uid = None
    device = None

    @classmethod
    def setUp(cls) -> None:
        Log.get_logger(cls.uid).info(".........初始化设备.........")
        Android.start_run_app(cls.device, AirSettings.PACKAGE, AirSettings.ACTIVITY)

    @classmethod
    def tearDown(cls) -> None:
        Log.get_logger(cls.uid).info("<---------关闭应用--------->")
        Android.close_app(cls.device, AirSettings.PACKAGE)
