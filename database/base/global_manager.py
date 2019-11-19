# -*-coding:utf-8-*-
# python: 2.7
# author: Wang Zhe
# filename: global_manager.py
# 本模块包含：
# 不对外可见的数据库操作函数
from database.models.model import BaseModel
from database.models.model import UserInfo
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import InternalError


# 初始化数据库
def database_init(engine, session):
    res = {}

    try:
        # 删除所有表
        BaseModel.metadata.drop_all(engine)
        # 创建由BaseModel生成的所有表类
        BaseModel.metadata.create_all(engine)

        # 创建管理员
        admin = UserInfo(name='admin', password='123123', email='1059150030@qq.com')

        # 插入管理员
        session.add(admin)
        session.commit()
    # 异常检测
    except Exception as e:
        if isinstance(e, OperationalError):
            print e
            res["success"] = False
            res["status"] = 1000
            res["message"] = "Database connect failed，please check database services"
            res["content"] = ""
            return res
        elif isinstance(e, InternalError):
            res["success"] = False
            res["status"] = 1000
            res["message"] = "Database connect failed，please check database Schema's name"
            res["content"] = ""
            print e
            return res
        elif isinstance(e, RuntimeError):
            res["success"] = False
            res["status"] = 1000
            res["message"] = "Database connect failed,please check username and password"
            res["content"] = ""
            return res
        else:
            res["success"] = False
            res["status"] = 1000
            res["message"] = "Unknown error"
            res["content"] = ""
            return res

    if session.query(UserInfo).filter_by(name="admin").first() is None:
        res["success"] = False
        res["status"] = 1000
        res["message"] = "Database initiate failed,please check code"
        res["content"] = ""
    else:
        res["success"] = True
        res["status"] = 0
        res["message"] = "Database initiate successfully!!!"
        res["content"] = ""
    session.close()
    return res
