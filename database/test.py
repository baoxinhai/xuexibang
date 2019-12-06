# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: test.py
# 本模块为接口测试模块
from database.api.main_base import Operator
from database.models.model import UserInfo, QuestionInfo
import datetime
from faker import Faker

fake = Faker('zh_CN')


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

    ret = o.get_result({"function": o.GET_ALL_CATEGORY})["content"]
    print ret

    #ret = o.get_result({"function": o.GET_RECOMMEND_QUESTION, "content": {"number": 5}})
    #for ques in ret["content"]:
    #   print ques["qutitle"], ques["quid"]  #   ques是一个dict对象

    # u = UserInfo(name="哈哈", password="123", email="test@163.com", admin=False)
    # print o.get_result({"function":o.INSERT_USER,
                       #  "content": u.to_dict()})

    # q = QuestionInfo(qucontent="我的第一个问题内容", qutitle="问题标题", qutime=fake.date_time_this_year(), uid=1)

    # ret = o.get_result({"function": o.INSERT_QUESTION,
    #                      "content": q.to_dict()})
    # print ret
'''
    ret = o.get_result({"function":o.GET_ALL_CATEGORY})

    for k, v in ret["content"].iteritems():
        print k, v
    if ret["content"]:  # 查询结果为空返回None
        print "find it !"
    else:
        print "no data"

    print (o.get_result(({"function":o.INSERT_USER,
                          "content":{
                              "name":"test",
                              "password":"test",
                              "email":"test",
                              "admin":False
                          }})))
 
'''
