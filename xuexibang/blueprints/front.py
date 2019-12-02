#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 解决utf-8无法显示
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

__author__ = 'Jinyang Shao'

'''
这个负责网站主页前台的数据传送和获取
'''

from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response

from xuexibang.main.extensions import db
from xuexibang.main.forms import HomeForm, AnswerForm

front_bp = Blueprint('front', __name__)


class current_user:
    is_authenticated = False


@front_bp.route('/home', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        category = form.category.data
        return redirect(url_for('front.home'))
    ret = db.get_result({"function" : db.GET_RECOMMEND_QUESTION, "content": {"number": 5}})
    questions = ret["content"]
    return render_template('front/home.html', questions=questions, form=form)


@front_bp.route('/')
def index():
    return redirect(url_for('front.home'))

# 显示某一类的问题页面
@front_bp.route('/categoty/<int:category_id>')
def show_category(category_id):
    return render_template('front/category.html')

# 显示单个问题及其回答的页面
@front_bp.route('/question/<int:question_id>', methods=['GET', 'POST'])
def show_question(question_id):
    ret = db.get_result({"function" : db.GET_QUESTION_BY_ID, "content" : {"quid" : question_id}})
    question = ret["content"]  # dict对象
    ret = db.get_result({"function" : db.GET_ANSWER_BY_QUID, "content" : {"quid" : question_id}})
    answers = ret["content"]   # list对象
    return render_template('front/qna.html', question=question, answers=answers)


@front_bp.route('/myquestion/<int:user_id>', )
def myquestion(user_id):
    question = "data"
    return render_template('front/myquestion.html', question=question)
