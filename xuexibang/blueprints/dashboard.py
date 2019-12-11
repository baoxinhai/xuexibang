#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

'''
后台管理，主要负责 后台负责删除已经发布的问题，管理注册的用户
'''

from flask import render_template, Blueprint, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user

from xuexibang.main.forms import CategoryForm, AdminForm
from xuexibang.main.extensions import db
from xuexibang.main.utils import redirect_back
from database.models.model import UserInfo


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = AdminForm
    if form.validate_on_submit():
        password = form.password.data
        new_admin = UserInfo()
        new_admin.set_password(password)
        db.get_result({"function" : db.UPDATE_USER_PWD, "content" : {
            "password_hash" : new_admin.password_hash
        }})
    return render_template('dashboard/settings.html', form=form)