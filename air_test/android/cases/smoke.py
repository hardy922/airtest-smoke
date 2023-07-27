# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 15:29
# @File: test_smoke.py
# @Software: PyCharm

from air_test.android.driver.driver import Driver
from air_test.android.utils.logger import Log
from air_test.android.utils.common.control import BaseControl
from air_test.android.utils.pages.elements import LightPlayLogin, GameInfo
from air_test.android.utils.common.basics import BaseOperation

class CommonC(Driver):

    def test_1_common_h265(self):
        """
        common-c-h265拉起游戏
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case1', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.COMMON_C, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.FORCE_265, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                result, fid = BaseOperation.in_the_game(self.poco, datas, self.uid)
                BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case1", t, st, result, datas, self.uid, fid)

    def test_2_common_h264(self):
        """
        common-c-h264拉起游戏
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case2', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.COMMON_C, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.TRY_264, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                result, fid = BaseOperation.in_the_game(self.poco, datas, self.uid)
                BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case2", t, st, result, datas, self.uid, fid)

    def test_3_264_to_h265(self):
        """
        common-c h264切换 h265
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case3', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.COMMON_C, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.TRY_264, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                result, fid = BaseOperation.in_the_game_switch(self.driver, self.poco, datas, self.uid)
                BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case3", t, st, result, datas, self.uid, fid)

    def test_4_265_to_h264(self):
        """
        common-c h265切换 h264
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case4', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.COMMON_C, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.FORCE_265, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                result, fid = BaseOperation.in_the_game_switch(self.driver, self.poco, datas, self.uid)
                BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case4", t, st, result, datas, self.uid, fid)


class Rtc(Driver):

    def test_5_265_to_h264(self):
        """
        rtc h265切换 h264
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case5', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.WEB_RTC, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.FORCE_265, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                result, fid = BaseOperation.in_the_game_switch(self.driver, self.poco, datas, self.uid)
                BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case5", t, st, result, datas, self.uid, fid)

    def test_6_264_to_265(self):
        """
        rtc h264切换 h265
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case6', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.WEB_RTC, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.TRY_264, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                result, fid = BaseOperation.in_the_game_switch(self.driver, self.poco, datas, self.uid)
                BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case6", t, st, result, datas, self.uid, fid)


class ComCRecovery(Driver):

    def test_7_264_recover(self):
        """
        Common-c H264串流中恢复串流
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case7', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.COMMON_C, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.TRY_264, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                op, fid = BaseOperation.in_game_open_debug(self.poco, self.uid)
                if op:
                    BaseControl.wait_element_click(self.poco, GameInfo.Recovery, self.uid, timeout=2)
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                    useless, fid = BaseOperation.wait_stream_info(self.driver, self.poco, self.uid, datas)
                    res = BaseOperation.ocr_recognition(f'{t}.png', self.uid, thresh=0.6)
                else:
                    res = ''
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
                if datas[6] in str(res):
                    result = True
                else:
                    result = False
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case7", t, st, result, datas, self.uid, fid)

    def test_8_265_recover(self):
        """
        Common-c H265串流中恢复串流
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case8', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.COMMON_C, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.FORCE_265, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                op, fid = BaseOperation.in_game_open_debug(self.poco, self.uid)
                if op:
                    BaseControl.wait_element_click(self.poco, GameInfo.Recovery, self.uid, timeout=2)
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                    useless, fid = BaseOperation.wait_stream_info(self.driver, self.poco, self.uid, datas)
                    res = BaseOperation.ocr_recognition(f'{t}.png', self.uid, thresh=0.6)
                else:
                    res = ''
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
                if datas[6] in str(res):
                    result = True
                else:
                    result = False
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case8", t, st, result, datas, self.uid, fid)


class RtcRecovery(Driver):

    def test_9_h264_recover(self):
        """
        rtc-h264恢复串流
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case9', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.WEB_RTC, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.TRY_264, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                op, fid = BaseOperation.in_game_open_debug(self.poco, self.uid)
                if op:
                    BaseControl.wait_element_click(self.poco, GameInfo.Recovery, self.uid, timeout=2)
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                    useless, fid = BaseOperation.wait_stream_info(self.driver, self.poco, self.uid, datas)
                    res = BaseOperation.ocr_recognition(f'{t}.png', self.uid, thresh=0.6)
                else:
                    res = ''
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
                if datas[6] in str(res):
                    result = True
                else:
                    result = False
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case9", t, st, result, datas, self.uid, fid)

    def test_10_h265_recover(self):
        """
        rtc-h265恢复串流
        :return:
        """
        st, t, datas, inpt = BaseOperation.start_setup_test('case10', self.driver, self.poco, self.uid)
        if inpt is not False:
            BaseControl.wait_element_click(self.poco, LightPlayLogin.WEB_RTC, self.uid)
            BaseControl.wait_element_click(self.poco, LightPlayLogin.FORCE_265, self.uid)
            if BaseControl.wait_element_click(self.poco, LightPlayLogin.LOGIN, self.uid):
                Log.get_logger(self.uid).info(f'已登录游戏，开始判断启动状态')
                op, fid = BaseOperation.in_game_open_debug(self.poco, self.uid)
                if op:
                    BaseControl.wait_element_click(self.poco, GameInfo.Recovery, self.uid, timeout=2)
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                    useless, fid = BaseOperation.wait_stream_info(self.driver, self.poco, self.uid, datas)
                    res = BaseOperation.ocr_recognition(f'{t}.png', self.uid, thresh=0.6)
                else:
                    res = ''
                    BaseOperation.snapshot_game(self.device, self.uid, t)
                BaseOperation.stop_game(datas, self.uid)
                if datas[6] in str(res):
                    result = True
                else:
                    result = False
            else:
                Log.get_logger(self.uid).error(f'登录游戏失败')
                BaseOperation.snapshot_game(self.device, self.uid, t)
                result, fid = False, None
        else:
            result, fid = False, None
            BaseOperation.snapshot_game(self.device, self.uid, t)
        BaseOperation.stop_teardown_test("case10", t, st, result, datas, self.uid, fid)
