# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: main_base.py
# 本模块包含：
# 将数据库包装为对外安全易用的接口类Operator
# 控制数据库进行操作的若干常量

from database.models.model_manager import get_session
from database.models.model_manager import get_engine
from database.base.global_manager import *
from database.base.user_manager import *
from database.base.logger_manager import *

from database.base.question_manager import *
from database.base.answer_manager import *
from database.base.category_manager import *

# 建立数据库引擎
engine = get_engine()


class Operator:

    def __init__(self):
        # 初始化数据库
        self.DATABASE_INIT = 0

        # 根据用户名获取用户信息
        self.GET_UER_BY_NAME = 1

        # 插入用户
        self.INSERT_USER = 2

        # 根据用户名删除用户
        self.DELETE_USER_BY_NAME = 3

        # 根据用户名更新密码
        self.UPDATE_USER_PWD = 4

        # 获取推荐问题列表
        self.GET_RECOMMEND_QUESTION = 5

        # 获取用户关注的问题列表
        self.GET_USER_FOLLOW = 6

        # 插入问题
        self.INSERT_QUESTION = 7

        # 获取问题
        self.GET_QUESTION_BY_ID = 8

        # 插入答案
        self.INSERT_ANSWER = 9

        # 根据答案id获取答案详细内容
        self.GET_ANSWER_BY_ID = 10

        # 根据问题id获取问题所有答案
        self.GET_ANSWER_BY_QUID = 11

        # 根据用户id获取用户提出的所有问题
        self.GET_QUESTION_BY_UID = 12

        # 根据用户id获取用户的所有答案
        self.GET_ANSWER_BY_UID = 13

        # 根据答案id删除答案
        self.DELETE_ANSWER_BY_ID = 14

        # 根据问题id删除问题
        self.DELETE_QUESTION_BY_ID = 15

        # 添加关注
        self.INSERT_FOLLOW = 16

        # 删除关注
        self.DELETE_FOLLOW = 17

        # 插入分类
        self.INSERT_CATEGORY = 18

        # 删除分类
        self.DELETE_CATEGORY = 19

        # 获取所有分类
        self.GET_ALL_CATEGORY = 20

        # 根据分类查询问题
        self.GET_QUESTION_BY_CAT = 21

        # 根据用户id获取用户信息
        self.GET_USER_BY_ID = 22

    def get_result(self, given):
        """
        数据库操作函数
        :param given:一个dict对象，参数为
                'function':操作数，指定数据库操作行为
                'content':数据库操作所需数据（若有）
        :return: 一个dict对象，参数为
                'success'：数据库操作是否成功
                'message':传送的信息
                'content':从数据库获取的数据（若没有则为NONE）
                'status':此次操作状态（暂未完善）
        :raises:None
        """
        session = get_session()
        function = given.get("function")
        cont = given.get("content")
        dev = given.get("dev")
        res = {}
        if function == self.DATABASE_INIT and dev is True:
            res = database_init(engine=engine, session=session)

        elif function == self.GET_UER_BY_NAME:
            res = get_user_by_name(cont, session)

        elif function == self.INSERT_USER:
            res = insert_user(cont, session)

        elif function == self.DELETE_USER_BY_NAME:
            res = delete_user_by_name(cont, session)

        elif function == self.UPDATE_USER_PWD:
            res = update_user_pwd(cont, session)

        elif function == self.INSERT_QUESTION:
            res = insert_question(cont, session)

        elif function == self.GET_RECOMMEND_QUESTION:
            res = get_recommend_question(cont,session)

        elif function == self.GET_QUESTION_BY_ID:
            res = get_question(cont, session)

        elif function == self.INSERT_ANSWER:
            res = insert_answer(cont, session)

        elif function == self.GET_ANSWER_BY_ID:
            res = get_answer_by_id(cont, session)

        elif function == self.GET_ANSWER_BY_QUID:
            res = get_answer_by_quid(cont, session)

        elif function == self.GET_QUESTION_BY_UID:
            res = get_question_by_uid(cont, session)

        elif function == self.GET_ANSWER_BY_UID:
            res = get_answer_by_uid(cont, session)

        elif function == self.DELETE_ANSWER_BY_ID:
            res = delete_answer_by_id(cont, session)

        elif function == self.DELETE_QUESTION_BY_ID:
            res = delete_question_by_id(cont, session)

        elif function == self.INSERT_FOLLOW:
            res = insert_follow(cont, session)

        elif function == self.DELETE_FOLLOW:
            res = delete_follow(cont, session)

        elif function == self.INSERT_CATEGORY:
            res = insert_category(cont, session)

        elif function == self.DELETE_CATEGORY:
            res = delete_category(cont, session)

        elif function == self.GET_ALL_CATEGORY:
            res = get_all_category(session)

        elif function == self.GET_QUESTION_BY_CAT:
            res = get_question_by_cat(cont, session)

        elif function == self.GET_USER_FOLLOW:
            res = get_user_follow(cont, session)

        elif function == self.GET_USER_BY_ID:
            res = get_user_by_id(cont,session)

        session.close()
        if res["success"] is True:
            Logger.info(res["message"])
        else:
            Logger.error(res["message"])
        return res


if __name__ == '__main__':
    Logger.info("test")
