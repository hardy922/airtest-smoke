# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 15:52
# @File: func.py
# @Software: PyCharm

import re
import base64
import requests
import configparser
from utils.logger import Log
from air_settings import AirSettings


class PublicFunc(object):

    @classmethod
    def read_case_ini(cls, case_file, index):
        """
        读取case数据
        :param case_file: 带路径文件
        :param index:
        :return:
        """
        try:
            config = configparser.ConfigParser()
            config.read(case_file, encoding='utf-8')
            desc = config.get(index, 'describe')
            vm = config.get(index, 'vmid')
            biz = config.get(index, 'biz')
            area = config.get(index, 'area')
            gid = config.get(index, 'gid')
            user = config.get(index, 'user')
            keyword1 = config.get(index, 'keyWords1')
            keyword2 = config.get(index, 'keyWords2')
            keyword3 = config.get(index, 'Keywords3')
            config_list = [desc, vm, biz, area, gid, user, keyword1, keyword2, keyword3]
            return config_list
        except Exception as e:
            Log.get_logger().error(f'读取手游驱动文件{case_file}出错——>{str(e)}')
            return False

    @classmethod
    def image_to_base64(cls, image):
        """
        图片转base64 string
        :param image:
        :return:
        """
        with open(image, 'rb') as img:
            encoded = base64.b64encode(img.read())
            return encoded.decode()

    @classmethod
    def cv_detection(cls, base, thresh=0.6):
        """
        cv目标检测
        :param base:
        :param thresh:
        :return:
        """
        bd = AirSettings.ocr_body(base, thresh)
        res = requests.post(url=AirSettings.OCR, json=bd)
        if res.status_code == 200:
            data = res.json().get('data')
            return data
        else:
            return None

    @classmethod
    def filter_flow_id(cls, text, fail=False):
        """
        过滤flow_id
        :param text:
        :param fail: 默认读取串流成功的fid
        :return:
        """
        try:
            if fail is False:
                fld = re.findall(r'flowId:(.*?)\n', str(text))
                fid = ''.join(fld)
                return fid
            else:
                fld = re.findall(r'flow_id:(.*)', text)
                fid = ''.join(fld)
                return fid
        except Exception as e:
            print(f'过滤flow_id出错：{str(e)}')
            return None
