# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: test.py
# 本模块为接口测试模块
from database.api.main_base import Operator
from database.models.model import UserInfo
import datetime
if __name__ == '__main__':
    o = Operator()

    print (o.get_result({"function":o.DELETE_FOLLOW,
                         "content":{
                             "qucontent":"test",
                             "qutitle":"test",
                             "uid":5,
                             "quid":5,
                             "qutime":datetime.datetime.now()
                         }}))



