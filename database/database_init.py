# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: database_init.py
# 本模块为数据库初始化模块
from database.api.main_base import Operator
from database.api.main_base import DATABASE_INIT

# 初始化建表，插入管理员admin
if __name__ == '__main__':
    o = Operator()
    res = o.get_result({"function": DATABASE_INIT, "content": "","dev":True})
    print (res)
    o.destroy()
