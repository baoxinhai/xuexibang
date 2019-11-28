# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: test.py
# 本模块为接口测试模块
from database.api.main_base import Operator
from database.models.model import UserInfo
import datetime

def tmp():
    res = {}
    try:
        res["success"] = True
        res["status"] = 0
        res["message"] = ""
        res["content"] = None
        return res

    except Exception as e:
        res["success"] = False
        res["status"] = 1000
        res["message"] = e.message
        res["content"] = None
        return res

if __name__ == '__main__':


    o = Operator()


    print (o.get_result({"function":o.GET_ALL_CATEGORY,
                         "content":{
                             "catname":"math",
                             "name":"admin",
                             #"anscontent":"test",
                             #"anstime":datetime.datetime.now(),
                             "qucontent":"test",
                             "qutitle":"test",
                             "uid":2,
                             #"quid":1,
                             "qutime":datetime.datetime.now(),
                             "catid":1,
                             "number":3
                         }}))

    '''
    print (o.get_result(({"function":o.INSERT_USER,
                          "content":{
                              "name":"test",
                              "password":"test",
                              "email":"test",
                              "admin":False
                          }})))
 
'''


