# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 11:28
# @File: android.py
# @Software: PyCharm

import re
import os
import subprocess
from airtest.core.android.adb import ADB
from utils.logger import Log


class Android(object):

    @classmethod
    def kill_adb_server(cls):
        """
        杀掉adb服务
        :return:
        """
        try:
            cmd = ['adb', 'kill-server']
            subprocess.check_call(cmd)
            Log.get_logger().info(f'杀掉adb server')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'杀掉adb server出错-->{str(e)}')

    @classmethod
    def start_adb_server(cls):
        """
        启动adb服务
        :return:
        """
        try:
            cmd = ['adb', 'start-server']
            subprocess.check_call(cmd)
            Log.get_logger().info(f'启动adb server')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'启动adb server出错-->{str(e)}')

    @classmethod
    def get_devices(cls):
        """
        获取设备
        :return:
        """
        try:
            cmd = ['adb', 'devices']
            out = subprocess.check_output(cmd).strip().decode('utf-8')
            device = re.findall("(.*?)device", out.strip())
            devices = [dev.replace('\t', '') for dev in device]
            Log.get_logger().info(f'获取当前设备：\n{out}')
            return devices
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'获取设备出错-->{str(e)}')

    @classmethod
    def install_app(cls, device, app):
        """
        安装app
        :param device:
        :param app: 带路径
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'install', '-r', app]
            subprocess.check_call(cmd)
            Log.get_logger().info(f'安装应用{app}至设备{device} 成功')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'安装应用{app}至设备{device} 出错-->{str(e)}')

    @classmethod
    def uninstall_app(cls, device, package):
        """
        卸载应用
        :param device:
        :param package:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'uninstall', package]
            output = subprocess.check_output(cmd)
            Log.get_logger().info(f'卸载应用 {package} 成功:{output}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'卸载应用：{package} 出错-->{str(e)}')

    @classmethod
    def view_packages(cls, device):
        """
        获取设备应用包名
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'pm', 'list', 'packages']
            out = subprocess.check_output(cmd).decode("utf-8")
            Log.get_logger().info(f'获取设备{device}应用包名：\n{out.split()}')
            return out.split()
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'获取设备{device} 应用包名出错-->{str(e)}')
            return None

    @classmethod
    def get_system_version(cls, device):
        """
        获取系统版本
        :param device:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'getprop', 'ro.build.version.release']
            out = subprocess.check_output(cmd).strip().decode('utf-8')
            return out
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'获取当前设备{device}系统版本出错-->{str(e)}')
            return None

    @classmethod
    def get_phone_name(cls, device):
        """
        获取设备名称
        :param device:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'getprop', 'ro.product.model']
            out = subprocess.check_output(cmd).decode('utf-8')
            Log.get_logger().info(f'获取当前设备{device}名称：{out}')
            return out
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'获取当前设备{device}名称出错-->{str(e)}')
            return None

    @classmethod
    def get_phone_product(cls, device):
        """
        获取设备产品系列
        :param device:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'getprop', 'ro.product.brand']
            out = subprocess.check_output(cmd).decode('utf-8')
            Log.get_logger().info(f'获取当前设备{device}产品系列：{out}')
            return out
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'获取当前设备{device}产品系列出错-->{str(e)}')
            return None

    @classmethod
    def send_text(cls, device, text):
        """
        发送文本,需配合adb输入法使用
        :param device:
        :param text:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'am broadcast -a ADB_INPUT_TEXT --es msg', text]
            out = subprocess.check_output(cmd)
            Log.get_logger().info(f'向设备{device}发送文本：{text} 成功 {out}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'发送文本：{text}出错-->{str(e)}')

    @classmethod
    def screenshot_as_file(cls, device, filename, local):
        """
        截屏保存文件,不能保存本地磁盘根目录，如：D:/
        :param device:
        :param filename:
        :param local:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', '/system/bin/screencap', '-p', f'/sdcard/{filename}.png']
            subprocess.check_output(cmd).decode('utf-8')
            Log.get_logger().info(f'截屏设备{device}，保存到手机根目录/sdcard/{filename}.png')
            pull = ['adb', '-s', device, 'pull', f'/sdcard/{filename}.png', local + f'/{filename}.png']
            subprocess.check_output(pull)
            Log.get_logger().info(f'设备{device}上文件{filename}.png 被导出到本地：{local}')
            return f'{filename}.png'
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'截图,导出文件{filename}.png出错-->{str(e)}')
            return None

    @classmethod
    def delete_device_file(cls, device, filename):
        """
        :param device:
        :param filename: 带路径的文件
        删除设备文件
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'rm', filename]
            subprocess.check_output(cmd)
            Log.get_logger().info(f'已删除设备{device}文件{filename}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'删除设备{device}文件{filename}出错-->{str(e)}')

    @classmethod
    def start_run_app(cls, device, package, activity):
        """
        启动app
        :param package:
        :param device:
        :param activity:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'am', 'start', f'{package}/{activity}']
            subprocess.check_call(cmd)
            Log.get_logger().info(f'启动设备{device}，driver:{package}/{activity}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'启动设备{device},driver:{package}/{activity}出错-->{str(e)}')

    @classmethod
    def close_app(cls, device, package):
        """
        关闭app
        :param device:
        :param package:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'am', 'force-stop', package]
            subprocess.check_call(cmd)
            Log.get_logger().info(f'关闭设备{device},包：{package}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'关闭设备{device},包:{package}出错-->{str(e)}')

    @classmethod
    def coordinate_click(cls, device, x, y):
        """
        通过坐标点击
        :param device:
        :param x:
        :param y:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'input', 'tap', str(x), str(y)]
            subprocess.check_output(cmd).decode('utf-8')
            Log.get_logger().info(f'点击设备{device}坐标x{x},y{y}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'点击设备{device}坐标x:{x},y:{y}出错-->{str(e)}')

    @classmethod
    def craw_lxml(cls, device, local):
        """
        导出屏幕快照ui资源
        :param device:
        :param local:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'uiautomator', 'dump', '/sdcard/ui.xml']
            subprocess.check_output(cmd, shell=True)
            pull = ['adb', '-s', device, 'pull', '/sdcard/ui.xml', local]
            subprocess.check_output(pull)
            Log.get_logger().info(f'导出设备{device}快照资源到本地:{local}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'导出设备{device}快照资源出错-->{str(e)}')

    @classmethod
    def craw_xlm_string(cls, device):
        """
        获取屏幕xml资源
        :param device:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'uiautomator', 'dump', '/sdcard/string_xml.xml']
            subprocess.check_output(cmd, shell=True)
            string = ['adb', '-s', device, 'shell', 'cat', '/sdcard/string_xml.xml']
            out = subprocess.check_output(string)
            Log.get_logger().info(f'获取当前设备{device}屏幕xml资源成功')
            return out
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'获取设备{device}屏幕xml资源出错：{str(e)}')

    @classmethod
    def input_text(cls, device, text):
        """
        输入文本，不支持中文
        :param device:
        :param text:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'input', 'text', text]
            subprocess.check_call(cmd)
            Log.get_logger().info(f'向设备{device}输入文本：{text}')
        except subprocess.CalledProcessError as e:
            Log.get_logger().error(f'向设备{device}输入文本:{text}出错-->{str(e)}')

    @classmethod
    def connection_device(cls, ip):
        """
        连接远程设备
        :param ip:
        :return:
        """
        try:
            cmd = ['adb', 'connect', ip]
            out = subprocess.check_output(cmd).decode('utf-8')
            if 'already connected' in out:
                return 'exist'
            elif 'connected to' in out:
                return 'success'
            else:
                return 'unknown'
        except Exception as e:
            Log.get_logger().error(f'连接设备：{ip}出错-->{str(e)}')
            return 'unknown'

    @classmethod
    def disconnect_device(cls, ip):
        """
        断开设备连接
        :param ip:
        :return:
        """
        try:
            cmd = ['adb', 'disconnect', ip]
            out = subprocess.check_output(cmd).strip().decode('utf-8')
            if 'disconnected' in out:
                return 'finish'
            else:
                return 'unknown'
        except Exception as e:
            Log.get_logger().error(f'断开设备：{ip}出错-->{str(e)}')
            return 'unknown'

    @classmethod
    def airtest_device(cls):
        """
        通过airtest获取设备
        :return:
        """
        try:
            adb = ADB()
            devices = adb.devices()
            print(devices)
        except Exception as e:
            Log.get_logger().error(f'airtest获取设备出错-->{str(e)}')

    @classmethod
    def input_key_event(cls, device, event):
        """
        adb命令shell input事件
        :param event:
        :param device:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'input', 'keyevent', event]
            Log.get_logger().info(f'向设备{device}发送点击事件:{event}')
            subprocess.check_output(cmd)
            return True
        except Exception as e:
            Log.get_logger().error(f'设备:{device}输入事件：{event}出错-->{str(e)}')
            return False

    @classmethod
    def swipe_point(cls, device, x1, y1, x2, y2):
        """
        滑动坐标
        :param device:
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'input', 'swipe', x1, y1, x2, y2]
            subprocess.check_output(cmd)
            Log.get_logger().info(f'滑动设备{device}坐标方向：{x1},{y1},{x2},{y2}')
            return True
        except Exception as e:
            Log.get_logger().error(f'滑动设备{device}出错-->{str(e)}')
            return False

    @classmethod
    def kill_app(cls, device, package):
        """
        杀掉应用
        :param device:
        :param package:
        :return:
        """
        try:
            cmd = ['adb', '-s', device, 'shell', 'am', 'force-stop', package]
            subprocess.check_output(cmd)
            Log.get_logger().info(f'已杀掉应用:{package}')
            return True
        except Exception as e:
            Log.get_logger().error(f'杀掉应用：{package}失败-->{str(e)}')
            return False


if __name__ == '__main__':
    # print(Android.airtest_device())
    # Android.kill_adb_server()
    # Android.start_adb_server()
    # rs = Android.get_system_version('65ij79lrypbmqogq')
    # print(rs)
    # Android.uninstall_app('65ij79lrypbmqogq', r'com.tencent.mobileqq')
    # Android.view_packages('65ij79lrypbmqogq')
    # a = Android.get_phone_product('65ij79lrypbmqogq')
    # print(a)
    # b = Android.screenshot_as_file('65ij79lrypbmqogq', 'hh', 'D:/截图')
    # c = Android.delete_device_file('65ij79lrypbmqogq', '/sdcard/hh.png')
    # Android.coordinate_click('65ij79lrypbmqogq', 677, 1089)
    # Android.craw_xlm_string('65ij79lrypbmqogq')
    # Android.input_text('65ij79lrypbmqogq', 'fff')
    # Android.start_app('65ij79lrypbmqogq', 'com.tencent.mobileqq/.activity.SplashActivity')
    # Android.send_text('65ij79lrypbmqogq', '12')
    Android.kill_app('10.86.21.163', 'com.demo')
