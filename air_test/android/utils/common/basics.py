# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 16:57
# @File: basics.py
# @Software: PyCharm

import os
import time
import requests
from datetime import datetime
from settings import Config
from configs.sql_config import SqlConfig
# from utils.sqlalchemy_utils import MySqlDB
from air_settings import AirSettings
from air_test.android.utils.logger import Log
from air_test.android.utils.common.func import PublicFunc
from air_test.android.utils.common.control import BaseControl
from air_test.android.utils.pages.elements import LightPlayLogin, GameInfo
# case_file = AirSettings.CASE_DATA + '/smoke.ini'


class BaseOperation(object):

    @classmethod
    def start_setup_test(cls, case, driver, poco, uid):
        """
        预处理开始
        :return:
        """
        st = datetime.now()
        t = AirSettings.time_now()
        case_file = Config.SRC_CASE + f'/{uid}/smoke.ini'
        datas = PublicFunc.read_case_ini(case_file, case)
        Log.get_logger(uid).info(f'开始执行{case},数据{datas}...')
        inpt = cls.login_input(driver, poco, datas, uid)
        return st, t, datas, inpt

    @classmethod
    def stop_teardown_test(cls, case, t, st, result, datas, uid, fid):
        """
        结束处理数据
        :param fid:
        :param case:
        :param t: 开始时间戳
        :param st:
        :param result:
        :param uid:
        :param datas:
        :return:
        """
        et = datetime.now()
        cls.report(result, datas, f'{t}.png', str(et - st), uid, fid)
        Log.get_logger(uid).info(f'执行用例{case}用时：{et - st}，测试结果：{result}')

    @classmethod
    def login_input(cls, driver, poco, data, uid):
        """
        登录输入参数
        :return:
        """
        # vm
        try:
            vm_st = BaseControl.wait_element(poco, LightPlayLogin.VM_ID, uid, timeout=10)
            if vm_st is True:
                vm = poco(name=LightPlayLogin.VM_ID)
                vm.click()
                vm.set_text('')
                vm.set_text(data[1])
                Log.get_logger(uid).info(f'输入vmid:{data[1]}')
                # biz
                biz = poco(name=LightPlayLogin.BIZ)
                biz.click()
                biz.set_text('')
                biz.set_text(data[2])
                Log.get_logger(uid).info(f'输入biz:{data[2]}')
                # area
                area = poco(name=LightPlayLogin.DEBUG_AREA)
                area.click()
                area.set_text('')
                area.set_text(data[3])
                Log.get_logger(uid).info(f'输入area:{data[3]}')
                # gid
                gid = poco(name=LightPlayLogin.GID)
                gid.click()
                gid.set_text('')
                gid.set_text(data[4])
                Log.get_logger(uid).info(f'输入gid:{data[4]}')
                # user
                user = poco(name=LightPlayLogin.USER)
                user.click()
                user.set_text('')
                user.set_text(data[5])
                Log.get_logger(uid).info(f'输入user:{data[5]}')
                # 向下滑动
                time.sleep(0.5)
                Log.get_logger(uid).info(f'开始向下滑动屏幕操作')
                poco(LightPlayLogin.LAYOUT_MAIN).swipe([0, -50])  # 到底部
                BaseControl.swipe_device(driver, poco, 'up', 1, uid)
                try:
                    # 判断手游是否可见
                    if BaseControl.wait_element(poco, LightPlayLogin.MOBILE_TYPE, uid, timeout=5) is False:
                        Log.get_logger(uid).warning(f'下滑失败，二次重新下滑')
                        poco(LightPlayLogin.LAYOUT_MAIN).swipe([0, -50])  # 到底部
                        BaseControl.swipe_device(driver, poco, 'up', 1, uid)
                finally:
                    if BaseControl.wait_element(poco, LightPlayLogin.MOBILE_TYPE, uid, timeout=5) is False:
                        Log.get_logger(uid).warning(f'下滑失败，三次重新下滑')
                        poco(LightPlayLogin.LAYOUT_MAIN).swipe([0, -50])  # 到底部
                        BaseControl.swipe_device(driver, poco, 'up', 1, uid)
                BaseControl.wait_element_click(poco, LightPlayLogin.MOBILE_TYPE, uid, timeout=5)
            else:
                return False
        except Exception as e:
            Log.get_logger(uid).error(f'基础参数输入出错-->{str(e)}')
            return False

    @classmethod
    def in_the_game(cls, poco, data, uid):
        """
        进入游戏中
        :param uid:
        :param poco:
        :param data:
        :return:
        """
        fid = None
        wait = BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5)
        if wait is False:
            Log.get_logger(uid).info(f'当前程序进入到游戏界面处理')
            try:
                left = BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=15)
                if left is True:
                    info = poco(name=GameInfo.LEFT_INFO).get_text()
                    Log.get_logger(uid).info(f'当前串流信息如下：\n{info}')
                    fid = PublicFunc.filter_flow_id(info)
                else:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=10):
                        fail_info = poco(name=GameInfo.RUN_FAIL).get_text()
                        Log.get_logger(uid).error(f'检测到游戏启动失败，错误信息如下:\n{fail_info}')
                        fid = PublicFunc.filter_flow_id(fail_info, fail=True)
                    info = ''
                    Log.get_logger(uid).error(f'未获取到串流信息,串流控件检查状态：{left}')
            except Exception as e:
                try:
                    if BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=5):
                        info = poco(name=GameInfo.LEFT_INFO).get_text()
                        fid = PublicFunc.filter_flow_id(info)
                finally:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5):
                        fail = poco(name=GameInfo.RUN_FAIL).get_text()
                        fid = PublicFunc.filter_flow_id(fail, fail=True)
                info = ''
                Log.get_logger(uid).error(f'获取串流信息出错-->{str(e)}')
            if data[6] in info and data[7] in info:
                return True, fid
            else:
                return False, fid
        else:
            fail = poco(name=GameInfo.RUN_FAIL).get_text()
            fid = PublicFunc.filter_flow_id(fail, fail=True)
            Log.get_logger(uid).error(f'游戏启动失败,失败信息：{fail}')
            return False, fid

    @classmethod
    def in_the_game_switch(cls, driver, poco, data, uid):
        """
        游戏中切换按钮
        :param driver:
        :param poco:
        :param data:
        :param uid:
        :return:
        """
        fid = None
        wait = BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5)
        if wait is False:
            Log.get_logger(uid).info(f'当前程序进入到游戏界面处理')
            try:
                debug = BaseControl.wait_element_click(poco, GameInfo.DEBUG, uid, timeout=15)  # 点击debug
                if debug is True:
                    BaseControl.wait_element_click(poco, GameInfo.DECODE, uid, timeout=5)  # 切换编码
                    driver.keyevent('BACK')  # 返回蒙板
                    info = BaseControl.wait_element_get_text(poco, GameInfo.LEFT_INFO, uid, timeout=15)
                    Log.get_logger(uid).info(f'当前串流信息如下：\n{info}')
                    fid = PublicFunc.filter_flow_id(info)
                else:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=10):
                        fail_info = poco(name=GameInfo.RUN_FAIL).get_text()
                        Log.get_logger(uid).error(f'检测到游戏启动失败，错误信息如下:\n{fail_info}')
                        fid = PublicFunc.filter_flow_id(fail_info, fail=True)
                    if BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=10):
                        left_info = poco(name=GameInfo.LEFT_INFO).get_text()
                        fid = PublicFunc.filter_flow_id(left_info)
                    info = ''
                    Log.get_logger(uid).error(f'切换编码失败')
            except Exception as e:
                try:
                    if BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=5):
                        left = poco(name=GameInfo.LEFT_INFO).get_text()
                        fid = PublicFunc.filter_flow_id(left)
                finally:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5):
                        fail = poco(name=GameInfo.RUN_FAIL).get_text()
                        fid = PublicFunc.filter_flow_id(fail, fail=True)
                info = ''
                Log.get_logger(uid).error(f'获取串流信息出错-->{str(e)}')
            if data[6] in str(info) and data[7] in str(info):
                return True, fid
            else:
                return False, fid
        else:
            fail = poco(name=GameInfo.RUN_FAIL).get_text()
            fid = PublicFunc.filter_flow_id(fail, fail=True)
            Log.get_logger(uid).error(f'游戏启动失败,失败信息：{fail}')
            return False, fid

    @classmethod
    def in_game_open_debug(cls, poco, uid):
        """
        游戏中打开调试界面
        :param poco:
        :param uid:
        :return:
        """
        fid = None
        wait = BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5)
        if wait is False:
            Log.get_logger(uid).info(f'当前程序进入到游戏界面处理')
            try:
                debug = BaseControl.wait_element_click(poco, GameInfo.DEBUG, uid, timeout=15)  # 点击debug
                if debug is True:
                    return True, fid
                else:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=10):
                        fail_info = poco(name=GameInfo.RUN_FAIL).get_text()
                        fid = PublicFunc.filter_flow_id(fail_info, fail=True)
                        Log.get_logger(uid).error(f'检测到游戏启动失败，错误信息如下:\n{fail_info}')
                    return False, fid
            except Exception as e:
                try:
                    if BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=5):
                        left = poco(name=GameInfo.LEFT_INFO).get_text()
                        fid = PublicFunc.filter_flow_id(left)
                finally:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5):
                        fail = poco(name=GameInfo.RUN_FAIL).get_text()
                        fid = PublicFunc.filter_flow_id(fail, fail=True)
                Log.get_logger(uid).error(f'打开调试界面出错-->{str(e)}')
                return False, fid
        else:
            fail = poco(name=GameInfo.RUN_FAIL).get_text()
            fid = PublicFunc.filter_flow_id(fail, fail=True)
            Log.get_logger(uid).error(f'游戏启动失败,失败信息：{fail}')
            return False, fid

    @classmethod
    def snapshot_game(cls, device, uid, filename):
        """
        截图画面
        :param device:
        :param uid:
        :param filename:
        :return:
        """
        ph = Config.SRC_SCREEN + f'/{uid}'
        if not os.path.exists(ph):
            os.makedirs(ph)
        BaseControl.snapshots(device, filename, uid, ph)

    @classmethod
    def stop_game(cls, datas, uid):
        """
        停止游戏
        :param uid:
        :param datas:
        :return:
        """
        try:
            bd = AirSettings.stop_game_body(datas[5], datas[4], datas[2])
            res = requests.post(url=AirSettings.STOP_GAME, json=bd)
            if res.status_code == 200:
                code = res.json().get('ret').get('code')
                if code == 0:
                    Log.get_logger(uid).info(f'用户:{datas[5]} gid:{datas[4]} biz:{datas[2]} 游戏停止成功')
                else:
                    Log.get_logger(uid).error(f'用户:{datas[5]} gid:{datas[4]} biz:{datas[2]} 游戏停止失败')
            else:
                Log.get_logger(uid).error(f'用户:{datas[5]} gid:{datas[4]} biz:{datas[2]} 游戏停止失败')
        except Exception as e:
            Log.get_logger(uid).error(f'用户:{datas[5]} gid:{datas[4]} biz:{datas[2]} 游戏停止出错-->{str(e)}')

    @classmethod
    def report(cls, result, datas, screen, tm, uid, fid):
        """
        结果上报
        :param fid:
        :param uid:
        :param tm:
        :param screen: 截图文件名,不带路径
        :param result:
        :param datas:
        :return:
        """
        if result is True:
            res = 1
        elif result is False:
            res = 2
        else:
            res = 0
        key = [datas[6], datas[7]]
        insert = SqlConfig.mobile_games_dict(
            datas[0], datas[1], datas[2], datas[3],
            datas[4], datas[5], ','.join(key), screen,
            str(res), tm, uid, str(fid)
        )
        Log.get_logger(uid).info(f'待上报数据处理完成：{insert}')
        # MySqlDB.insert_data('mobile_games_data', **insert)
        Log.get_logger(uid).info(f'上报数据结果完成！')

    @classmethod
    def ocr_recognition(cls, image, uid, thresh=0.6):
        """
        图片识别
        :param image:
        :param uid:
        :param thresh:
        :return:
        """
        img = Config.SRC_SCREEN + f'/{uid}/{image}'
        base = PublicFunc.image_to_base64(img)
        bd = AirSettings.ocr_body(base, thresh)
        res = requests.post(url=AirSettings.OCR, json=bd)
        if res.status_code == 200:
            data = res.json().get('data')
            Log.get_logger(uid).info(f'图片:{image} 识别数据：{data}')
            return data
        else:
            Log.get_logger(uid).info(f'图片:{image} 识别失败, post-->{res.status_code}')
            return None

    @classmethod
    def wait_stream_info(cls, driver, poco, uid, data, timeout=3):
        """
        关闭调试面板，获取串流信息
        :param data:
        :param driver:
        :param poco:
        :param uid:
        :param timeout:
        :return:
        """
        try:
            fid = None
            driver.keyevent('BACK')  # 返回蒙板
            left = BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=timeout)
            if left is True:
                info = poco(name=GameInfo.LEFT_INFO).get_text()
                Log.get_logger(uid).info(f'当前串流信息如下：\n{info}')
                fid = PublicFunc.filter_flow_id(info)
            else:
                info = ''
                Log.get_logger(uid).error(f'未获取到串流信息,串流控件检查状态：{left}')
            if data[6] in info and data[7] in info:
                return True, fid
            else:
                return False, fid
        except Exception as e:
            Log.get_logger(uid).error(f'获取串流信息出错-->{str(e)}')
            return False, None

    @classmethod
    def stream_info(cls, driver, poco, uid, data, switch=False):
        """
        游戏中右上角串流信息
        :param driver:
        :param poco:
        :param uid:
        :param data:
        :param switch: False:不打开调试面板，True：打开调试面板
        :return:
        """
        try:
            if switch is False:
                left, fid = cls.in_the_game(poco, data, uid)
            else:
                left, fid = cls.wait_stream_info(driver, poco, uid, data)
            stream = BaseControl.wait_element_get_text(poco, GameInfo.STREAM_INFO, uid)
            Log.get_logger(uid).info(f'当前游戏串流信息：\n{stream}')
            if left is True and data[8] in str(stream):
                return True, fid
            else:
                return False, fid
        except Exception as e:
            Log.get_logger(uid).error(f'获取游戏串流信息出错-->{str(e)}')
            return False, None

    @classmethod
    def check_game_login(cls, poco, uid):
        """
        检查游戏是否启动成功
        :param poco:
        :param uid:
        :return:
        """
        pass

    @classmethod
    def get_game_info(cls, poco, uid):
        """
        进入游戏获取串流信息并返回
        :param poco:
        :param uid:
        :return:
        """
        info, fid = '', None
        wait = BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5)
        if wait is False:
            Log.get_logger(uid).info(f'当前程序进入到游戏界面处理')
            try:
                left = BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=15)
                if left is True:
                    info = poco(name=GameInfo.LEFT_INFO).get_text()
                    Log.get_logger(uid).info(f'当前串流信息如下：\n{info}')
                    fid = PublicFunc.filter_flow_id(info)
                else:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=10):
                        fail_info = poco(name=GameInfo.RUN_FAIL).get_text()
                        Log.get_logger(uid).error(f'检测到游戏启动失败，错误信息如下:\n{fail_info}')
                        fid = PublicFunc.filter_flow_id(fail_info, fail=True)
                    Log.get_logger(uid).error(f'未获取到串流信息,串流控件检查状态：{left}')
            except Exception as e:
                try:
                    if BaseControl.wait_element(poco, GameInfo.LEFT_INFO, uid, timeout=5):
                        info = poco(name=GameInfo.LEFT_INFO).get_text()
                        fid = PublicFunc.filter_flow_id(info)
                finally:
                    if BaseControl.wait_element(poco, GameInfo.RUN_FAIL, uid, timeout=5):
                        fail = poco(name=GameInfo.RUN_FAIL).get_text()
                        fid = PublicFunc.filter_flow_id(fail, fail=True)
                Log.get_logger(uid).error(f'获取串流信息出错-->{str(e)}')
        else:
            fail = poco(name=GameInfo.RUN_FAIL).get_text()
            fid = PublicFunc.filter_flow_id(fail, fail=True)
            Log.get_logger(uid).error(f'游戏启动失败,失败信息：{fail}')
        return info, fid


if __name__ == '__main__':
    BaseOperation.snapshot_game('123', 'GHH123', 'test')

