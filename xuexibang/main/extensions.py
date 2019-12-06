#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

'''
一些全局变量：数据库、富文本编辑器、时间戳
'''
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_moment import Moment
from database.api.main_base import *
from flask_login import LoginManager

bootstrap = Bootstrap()
db = Operator()
mail = Mail()
ckeditor = CKEditor()
moment = Moment()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from database.models.model import UserInfo
    ret = db.get_result({"function" : db.GET_USER_BY_ID, "content" : {
        "uid" : int(user_id)
    }})
    userinfo = ret["content"]
    user = UserInfo(uid=userinfo['uid'], name=userinfo['name'], email=userinfo['email'], admin=userinfo['admin'],
                    password_hash=userinfo['password_hash'])
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = '来提出你的问题吧！'
login_manager.login_message_category = 'warning'