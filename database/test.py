# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: test.py
# 本模块为接口测试模块
from database.api.main_base import Operator
from database.models.model import UserInfo

if __name__ == '__main__':
    o = Operator()

    '''
    print(u"查询admin结果:")
    print (o.get_result({"function": GET_UER_BY_NAME, "content": {"name": "admin"}}))

    print (u"删除admin结果:")
    print (o.get_result({"function": DELETE_USER_BY_NAME, "content": {"name": "admin"}}))

    print(u"查询admin结果:")
    print (o.get_result({"function": GET_UER_BY_NAME, "content": {"name": "admin"}}))

    print (u"插入admin结果:")
    print (o.get_result({"function": INSERT_USER, "content": {"name": "admin", "password": "12312313", "email": "1059150030@qq.com"}}))

    print(u"查询admin结果:")
    print (o.get_result({"function": GET_UER_BY_NAME, "content": {"name": "admin"}}))

    print(u"修改admin密码结果:")
    print (o.get_result({"function": UPDATE_USER_PWD, "content": {"name": "admin", "password": "12312313"}}))

    print(u"查询admin结果:")
    print (o.get_result({"function": GET_UER_BY_NAME, "content": {"name": "admin"}}))
    '''
    session=o.get_session()
    user_info = session.query(UserInfo).all()
    print user_info[0].to_dict()

    o.destroy()
