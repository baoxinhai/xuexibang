# -*-coding:utf-8-*-
# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: user_manager.py
# 本模块包含：
# 不对外可见的数据库操作函数
from database.models.model import UserInfo
from database.models.model import Follow


# 根据用户名查找用户
def get_user_by_name(user, session):
    user_info = session.query(UserInfo).filter_by(name=user["name"]).first()
    res = {}
    user_list = []
    if isinstance(user_info, UserInfo):
        user_list.append(user_info.to_dict())
        res["success"] = True
        res["status"] = 0
        res["message"] = "User: %s fond successfully" % user["name"]
        res["content"] = user_list
    else:
        res["success"] = True
        res["status"] = 1000
        res["message"] = "User: %s not fond" % user["name"]
        res["content"] = None

    return res


# 插入新用户
def insert_user(user, session):
    res = {}

    user_info = get_user_by_name(user, session)
    if isinstance(user_info, UserInfo):
        res["success"] = False
        res["status"] = 1002
        res["message"] = "User: %s already exits!!!" % user["name"]
        res["content"] = " "
    else:
        user_info = UserInfo()
        user_info.name = user["name"]
        user_info.password = user["password"]
        user_info.email = user["email"]
        session.add(user_info)
        session.commit()
        res["success"] = True
        res["status"] = 0
        res["message"] = "User: %s insert successfully" % user["name"]
        res["content"] = " "
    return res


# 根据用户名删除用户
def delete_user_by_name(name, session):
    res = {}
    # 检查数据库中是否存在用户
    user_info = session.query(UserInfo).filter_by(name=name["name"]).first()

    # 若用户不存在
    if not isinstance(user_info, UserInfo):
        res["success"] = False
        res["status"] = 1000
        res["message"] = "User: %s not fond" % name["name"]
        res["content"] = " "

    else:
        session.delete(user_info)
        session.commit()
        res["success"] = True
        res["status"] = 0
        res["message"] = "User: %s deleted successfully!" % name["name"]
        res["content"] = " "

    return res


# 修改用户密码
def update_user_pwd(user, session):
    res = {}
    # 检查数据库中是否存在用户
    user_info = session.query(UserInfo).filter_by(name=user["name"]).first()

    # 若用户不存在
    if not isinstance(user_info, UserInfo):
        res["success"] = False
        res["status"] = 1000
        res["message"] = "User: %s not fond" % user["name"]
        res["content"] = " "
    else:
        user_info.password = user["password"]
        res["success"] = True
        res["status"] = 0
        res["message"] = "User: %s password update successfully!!" % user["name"]
        res["content"] = user_info.to_dict()
        session.commit()

    return res


def get_user_follow(user, session):
    res = {}
    user_info = session.query(UserInfo).filter_by(name=user["name"]).first()
    follow_list = []
    # 若用户不存在
    if not isinstance(user_info, UserInfo):
        res["success"] = False
        res["status"] = 1000
        res["message"] = "User: %s not fond" % user["name"]
        res["content"] = None
    else:
        follow_info_list = session.query(Follow).filter_by(uid=user_info.uid).all()
        for follow_info in follow_info_list:
            follow_list.append(follow_info.ansid)

        res["success"] = True
        res["status"] = 0
        res["message"] = "User: %s's follow fond" % user["name"]
        res["content"] = follow_list

    return res

