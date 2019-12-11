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
from database.models.model import UserInfo, Category


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
    flash("change the password success", "success")
    return render_template('dashboard/settings.html', form=form)


@dashboard_bp.route('/question/manage')
@login_required
def manage_questions():
    page = request.args.get('page', 1, type=int) # 测试完front里面的分页功能，再来增加这个
    questions = db.get_result({"function" : db.GET_RECOMMEND_QUESTION, "content" : {
        "number": 8,
        "start": 8 * (page - 1)
    }})
    return render_template('dashboard/manage_questions.html', questions=questions)


@dashboard_bp.route('/category/new', methods=['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        newcate = Category()
    return render_template('dashboard/edit_category.html')


@dashboard_bp.route('/category/manage', methods=['GET', 'POST'])
@login_required
def manage_category():
    return render_template('dashboard/manage_category.html')


@dashboard_bp.route('/users/manage', methods=['GET', 'POST'])
@login_required
def manage_users():
    return render_template('dashboard/manage_users.html')


@dashboard_bp.route('/answers/manage', methods=['GET', 'POST'])
@login_required
def manage_answers():
    return render_template('dashboard/manage_answers.html')