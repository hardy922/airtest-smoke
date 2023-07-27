# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 11:26
# @File: run.py
# @Software: PyCharm

import unittest
from air_test.android.utils.logger import Log
from air_test.android.driver.driver import Driver
from air_test.android.driver import init_devices
from air_test.android.cases.smoke import CommonC
from air_test.android.cases.smoke import Rtc
from air_test.android.cases.smoke import ComCRecovery
from air_test.android.cases.smoke import RtcRecovery


import logging
logger = logging.getLogger('airtest')
logger.setLevel(logging.ERROR)

func_list = [CommonC, Rtc, ComCRecovery, RtcRecovery]


def main(devices, uid):
    device, poco = init_devices(devices)
    test = Driver
    test.driver = device
    test.poco = poco
    test.uid = uid
    test.device = devices
    suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(test)
    suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(Rtc)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner().run(suite)


def full_main(devices, uid):
    Log.get_logger(uid).info(f'******************************手游任务:{uid}, 测试开始******************************')
    device, poco = init_devices(devices)
    test = Driver
    test.driver = device
    test.poco = poco
    test.uid = uid
    test.device = devices
    # 全量运行
    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromTestCase(test)
    suites_list = [suite1]
    for func in func_list:
        suite = loader.loadTestsFromTestCase(func)
        suites_list.append(suite)
    suites = unittest.TestSuite(suites_list)
    unittest.TextTestRunner().run(suites)
    Log.get_logger(uid).info(f'<!----------------------当前测试任务：{uid}, 测试结束----------------------!>')
