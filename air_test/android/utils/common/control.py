# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 14:45
# @File: elements.py
# @Software: PyCharm

import os
import time
import subprocess
from air_settings import AirSettings
from airtest.core.api import *
from poco.exceptions import *
from air_test.android.utils.logger import Log
from air_test.android.utils.common.android import Android


class BaseControl(object):

    @classmethod
    def get_screen_size(cls, poco, uid):
        """
        获取设备宽高
        :param uid:
        :param poco:
        :return:
        """
        try:
            width, height = poco.get_screen_size()
            Log.get_logger(uid).info(f'获取设备尺寸宽高：{width},{height}')
            return width, height
        except InvalidOperationException as e:
            Log.get_logger(uid).error(f'获取设备尺寸宽高出错-->{str(e)}')

    @classmethod
    def swipe_device(cls, driver, poco, direction, loop_num, uid):
        """
        滑动屏幕
        :param uid:
        :param driver:
        :param poco:
        :param direction:
        :param loop_num:
        :return:
        """
        try:
            width, height = cls.get_screen_size(poco, uid)
            x = width * 0.8
            y = height * 0.8
            x1 = width * 0.3
            x2 = width * 0.8
            y1 = height * 0.6
            y2 = height * 0.8
            if direction == 'up':
                for i in range(int(loop_num)):
                    driver.swipe((x, y1), (x, y2))
                    time.sleep(0.8)
                    Log.get_logger(uid).info(f'向上滑动：{(x, y1), (x, y2)}')
            elif direction == 'down':
                for i in range(int(loop_num)):
                    driver.swipe([x, y2], [x, y1])
                    time.sleep(0.8)
                    Log.get_logger(uid).info(f'向下滑动：{(x, y2), (x, y1)}')
            elif direction == 'left':
                for i in range(int(loop_num)):
                    driver.swipe((x2, y), (x1, y))
                    time.sleep(0.8)
                    Log.get_logger(uid).info(f'向左滑动：{(x2, y), (x1, y)}')
            elif direction == 'right':
                for i in range(int(loop_num)):
                    driver.swipe((x1, y), (x2, y))
                    time.sleep(0.8)
                    Log.get_logger(uid).info(f'向右滑动：{(x1, y), (x2, y)}')
        except Exception as e:
            Log.get_logger(uid).error(f'向{direction}滑动出错-->{str(e)}')

    @classmethod
    def check_exists(cls, poco, page, uid):
        """
        检测元素是否存在
        :param uid:
        :param poco:
        :param page: id
        :return:
        """
        try:
            el = poco(name=page)
            if el.exists():
                Log.get_logger(uid).info(f'查询到元素：{page}')
                return True
            else:
                Log.get_logger(uid).error(f'未查询到元素：{page}')
                return False
        except InvalidOperationException as e:
            Log.get_logger(uid).error(f'查询元素:{page} 出错-->{str(e)}')
            return False

    @classmethod
    def touch_pinch(cls, poco, direction, uid):
        """
        两指操作
        :param uid:
        :param direction:
        :param poco:
        :return:
        """
        try:
            if direction == 'in':
                poco.pinch(direction=direction, percent=0.6, duration=2.0, dead_zone=0.1)
                Log.get_logger(uid).info(f'两指向内挤压收缩操作')
            elif direction == 'out':
                poco.pinch(direction=direction, percent=0.6, duration=2.0, dead_zone=0.1)
                Log.get_logger(uid).info(f'两指向外挤压收缩操作')
            else:
                Log.get_logger(uid).warning(f'该方向：{direction} 不支持')
        except InvalidOperationException as e:
            Log.get_logger(uid).error(f'两指操作方向：{direction} 出错-->{str(e)}')

    @classmethod
    def wait_element(cls, poco, page, uid, timeout=10):
        """
        等待元素是否出现
        :param uid:
        :param poco:
        :param page:
        :param timeout:
        :return:
        """
        try:
            poco(name=page).wait_for_appearance(timeout=timeout)
            Log.get_logger(uid).info(f'查询到元素：{page}')
            return True
        except PocoTargetTimeout as e:
            Log.get_logger(uid).error(f'未查询到元素：{page}，超时：{timeout}，-->{str(e)}')
            return False

    @classmethod
    def wait_element_click(cls, poco, page, uid, timeout=5):
        """
        等待元素出现点击
        :param poco:
        :param page:
        :param uid:
        :param timeout:
        :return:
        """
        try:
            poco(name=page).wait_for_appearance(timeout=timeout)
            Log.get_logger(uid).info(f'查询到元素：{page},并点击')
            poco(name=page).click()
            return True
        except PocoTargetTimeout as e:
            Log.get_logger(uid).error(f'等待查询元素{page}超时:{timeout},点击出错-->{str(e)}')
            return False

    @classmethod
    def wait_element_get_text(cls, poco, page, uid, timeout=5):
        """
        等待元素出现获取文本
        :param poco:
        :param page:
        :param uid:
        :param timeout:
        :return:
        """
        try:
            status = cls.wait_element(poco, page, uid, timeout=timeout)
            if status is True:
                txt = poco(name=page).get_text()
                return txt
            else:
                return None
        except Exception as e:
            Log.get_logger(uid).error(f'等待元素：{page}超时:{timeout},获取文本失败-->{str(e)}')
            return None

    @classmethod
    def wait_element_disappear(cls, poco, page, uid, timeout=10):
        """
        等待元素消失
        :param uid:
        :param poco:
        :param page:
        :param timeout:
        :return:
        """
        try:
            poco(name=page).wait_for_disappearance(timeout=timeout)
            Log.get_logger(uid).info(f'元素{page}消失成功')
            return True
        except InvalidOperationException as e:
            Log.get_logger(uid).error(f'等待元素{page}消失超时:{timeout}, 失败-->{str(e)}')
            return False

    @classmethod
    def long_clicks(cls, poco, page, uid, duration=2):
        """
        长按
        :param uid:
        :param poco:
        :param page:
        :param duration:
        :return:
        """
        try:
            poco(name=page).long_click(duration=duration)
            Log.get_logger(uid).info(f'长按元素：{page}，时长：{duration}')
        except InvalidOperationException as e:
            Log.get_logger(uid).error(f'长按元素：{page}出错-->{str(e)}')

    @classmethod
    def drag(cls, poco, start_page, end_page, uid):
        """
        拖动元素
        :param uid:
        :param poco:
        :param start_page:
        :param end_page:
        :return:
        """
        try:
            poco(name=start_page).drag_to(poco(name=end_page))
            Log.get_logger(uid).info(f'将元素：{start_page} 拖动到：{end_page}')
        except InvalidOperationException as e:
            Log.get_logger(uid).error(f'将元素{start_page}拖动到{end_page}出错-->{str(e)}')

    @classmethod
    def snapshots(cls, device, filename, uid, local):
        """
        截图保存
        :param local:
        :param uid:
        :param device:
        :param filename: 不带路径
        :return:
        """
        # try:
        #     driver.snapshot(filename=filename)
        #     Log.get_logger(uid).info(f'当前截图已保存：{os.path.basename(filename)}')
        # except Exception as e:
        #     Log.get_logger(uid).error(f'截图：{os.path.basename(filename)}出错-->{str(e)}')
        try:
            cmd = ['adb', '-s', device, 'shell', 'screencap', '-p', f'/sdcard/{str(filename)}.png']
            subprocess.check_output(cmd).decode('utf-8')
            Log.get_logger(uid).info(f'当前截图已保存：{str(filename)}.png')
        except Exception as e:
            Log.get_logger(uid).error(f'截图：{str(filename)}.png出错-->{str(e)}')
        try:
            pull = ['adb', '-s', device, 'pull', f'/sdcard/{str(filename)}.png', local]
            subprocess.check_output(pull).decode('utf-8')
        except Exception as e:
            Log.get_logger(uid).error(f'导出截图:{str(filename)}.png 出错-->{str(e)}')
        try:
            rm = ['adb', '-s', device, 'shell', 'rm', f'/sdcard/{str(filename)}.png']
            subprocess.check_output(rm).decode('utf-8')
        except Exception as e:
            Log.get_logger(uid).error(f'删除设备截图:{str(filename)}.png 出错-->{str(e)}')

    @classmethod
    def xiaomi_swipe_down(cls, uid):
        """
        小米note8专用滑屏
        :param uid:
        :return:
        """
        try:
            swipe(Template(AirSettings.SRC_DIR + "/tpl1676606340826.png", record_pos=(0.445, 0.902),
                           resolution=(1080, 2340)), vector=[-0.0037, -0.8484])
            swipe(Template(AirSettings.SRC_DIR + "/tpl1676606346085.png", record_pos=(0.449, 0.92),
                           resolution=(1080, 2340)), vector=[-0.0294, -0.823])
            swipe(Template(AirSettings.SRC_DIR + "/tpl1676606353490.png", record_pos=(0.423, 0.836),
                           resolution=(1080, 2340)), vector=[-0.0257, -0.2426])
            Log.get_logger(uid).info(f'定制滑屏连续向下滑动3次')
        except Exception as e:
            Log.get_logger(uid).error(f'定制滑屏向下滑屏出错-->{str(e)}')

    @classmethod
    def get_toast_tips(cls, poco, uid, timeout=5):
        """
        获取toast提示
        :param poco:
        :param uid:
        :param timeout:
        :return:
        """
        try:
            # toast = poco.wait_for_any(poco("android.widget.Toast"), timeout=timeout)
            froze = poco.freeze()
            hierarchy = froze.hierarchy.dump()
            # Log.get_logger(uid).info(f'获取当前toast提示：{toast}')
            Log.get_logger(uid).info(f'获取当前UI数提示：{hierarchy}')
            return hierarchy
        except Exception as e:
            Log.get_logger(uid).error(f'获取当前toast出错-->{str(e)}')
            return None

    @classmethod
    def xpath_select_click(cls, poco, page, uid):
        """
        通过xpath定位,最新版不支持该功能，弃用
        :return:
        """
        try:
            poco.XPath.click(page)
            Log.get_logger(uid).info(f'通过xpath点击：{page}')
            return True
        except Exception as e:
            Log.get_logger(uid).error(f'通过xpath点击:{page}出错-->{str(e)}')
            return None

    @classmethod
    def get_text_click(cls, poco, txt, uid):
        """
        通过文本内容点击
        :param poco:
        :param txt:
        :param uid:
        :return:
        """
        try:
            poco(text=txt).click()
            Log.get_logger(uid).info(f'查找文本:{txt} 点击成功')
        except Exception as e:
            Log.get_logger(uid).error(f'查找文本:{txt}点击出错-->{str(e)}')

    @classmethod
    def unlock_screen(cls, device, poco, uid):
        """
        滑动解锁屏幕(设备没有设置解锁密码)
        :param poco:
        :param device:
        :param uid:
        :return:
        """
        try:
            if Android.input_key_event(device, '224') is True:
                width, height = cls.get_screen_size(poco, uid)
                x = int(width * 0.5)
                y1 = int(height * 0.5)
                y2 = int(height * 0.8)
                Android.swipe_point(device, str(x), str(y2), str(x), str(y1))
                Log.get_logger(uid).info(f'解锁屏幕操作：{(x, y2), (x, y1)}')
        except Exception as e:
            Log.get_logger(uid).error(f'解锁设备出错-->{str(e)}')



