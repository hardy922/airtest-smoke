# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/14 10:20
# @File: sql_config.py
# @Software: PyCharm


class SqlConfig(object):

    @classmethod
    def mobile_games_dict(cls, scene, vm, biz, area, gid, user, keyword, screen, res, times, uid, fid):
        insert = dict(
            scene=scene,
            vmid=vm,
            biz=biz,
            area=area,
            gid=gid,
            user=user,
            keyword=keyword,
            screen=screen,
            result=res,
            times=times,
            uid=uid,
            flow_id=fid
        )
        return insert
