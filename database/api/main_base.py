# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: main_base.py
# 本模块包含：
# 将数据库包装为对外安全易用的接口类Operator
# 控制数据库进行操作的若干常量

from database.models.model_manager import get_session
from database.models.model_manager import get_engine
from database.base.global_manager import database_init
from database.base.user_manager import delete_user_by_name
from database.base.user_manager import update_user_pwd
from database.base.user_manager import get_user_by_name
from database.base.user_manager import insert_user

# 建立数据库引擎
engine = get_engine()

# 初始化数据库
# 不需要content
DATABASE_INIT = 0

# 根据用户名获取用户信息
# content为含有key为name,value为用户名的dict
GET_UER_BY_NAME = 1

# 插入用户
# content为含有key为 name, password, email, value分别为用户名，密码和邮箱的dict
INSERT_USER = 2

# 根据用户名删除用户
# content为含有key为name,value为用户名的dict
DELETE_USER_BY_NAME = 3

# 根据用户名更新密码
# conten为含有key为name, password, value分别为用户名和密码的dict
UPDATE_USER_PWD = 4


class Operator:

    def __init__(self):
        self._session = get_session()

    def get_result(self, given):
        function = given.get("function")
        cont = given.get("content")
        dev = given.get("dev")

        if function == DATABASE_INIT and dev == True:
            res = database_init(engine=engine, session=self._session)
            return res
        elif function == GET_UER_BY_NAME:
            res = get_user_by_name(cont, self._session)
            return res
        elif function == INSERT_USER:
            res = insert_user(cont, self._session)
            return res
        elif function == DELETE_USER_BY_NAME:
            res = delete_user_by_name(cont, self._session)
            return res
        elif function == UPDATE_USER_PWD:
            res = update_user_pwd(cont, self._session)
            return res

    def destroy(self):
        self._session.close()
