# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/13 15:33
# @File: smoke_run.py
# @Software: PyCharm

from air_test.android.run import main, full_main


def android_run_main(device, uid):
    """
    手游运行入口：main为单个调试运行，full_main为全量运行
    """
    main(device, uid)
    # full_main(device, uid)


if __name__ == '__main__':
    android_run_main('10.86.21.138', 'ef49ac02-ab4f-11ed-a0fb-cc1531f44e9d')
