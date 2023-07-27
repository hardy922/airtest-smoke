# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 14:25
# @File: __init__.py.py
# @Software: PyCharm

import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# adb = ADB()
# device = adb.devices()
# print(device)


def init_devices(device):
    """
    连接设备
    :param device:
    :return:
    """
    driver = connect_device(f"android://127.0.0.1:5037/{device}")
    # time.sleep(2)
    poco = AndroidUiautomationPoco(device=driver, use_airtest_input=False)
    return driver, poco


def default_device():
    """
    默认连接当前设备
    :return:
    """
    driver = connect_device("android:///")
    poco = AndroidUiautomationPoco(device=driver, use_airtest_input=True)
    return driver, poco


if __name__ == '__main__':
    a, b = init_device('10.86.21.79:5555')
    print(a, b)
