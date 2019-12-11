#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 解决utf-8无法显示
import sys
import datetime

from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from flask_login import current_user

from xuexibang.main.extensions import db
from xuexibang.main.forms import HomeForm, AnswerForm
from database.models.model import QuestionInfo, AnswerInfo

from xuexibang.main.utils import Page  # 用于分页的记录

import click  # for debug

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

front_bp = Blueprint('front', __name__)


@front_bp.route('/home', defaults={'page': 1}, methods=['GET', 'POST'])
@front_bp.route('/home/page/<int:page>')
def home(page):
    form = HomeForm()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            category = form.category.data
            userid = current_user.uid
            click.echo('%s, %s,user: %d' % (title, description, userid))
            question = QuestionInfo(
                qucontent=description,
                qutitle=title,
                uid=userid,  # 提问者id
                qutime=datetime.datetime.now(),
                catid=category,
                ansnumber=0
            )
            db.get_result({"function" : db.INSERT_QUESTION, "content" : question.to_dict()})
            flash("提交问题成功！", "success")
            return redirect(url_for('front.home'))
    else:
        if form.validate_on_submit():
            flash("请先登录!", "warning")

    per_page = current_app.config['QUESTIONS_PER_PAGE']  # 每页显示的数量
    ret = db.get_result({"function" : db.GET_RECOMMEND_QUESTION, "content": {"number": per_page, "start" : per_page * (page - 1)}})
    if ret["content"]:
        page_record=Page(page, per_page)
        if page <= 1:
            page_record.has_prev = False
        else:
            page_record.has_prev = True
        if len(ret["content"]) < per_page:
            page_record.is_last = True
    else:
        page_record=Page(page, per_page, True)
        page_record.has_prev = True
    questions = ret["content"]
    return render_template('front/home.html', questions=questions, form=form, page=page_record)


@front_bp.route('/')
def index():
    return redirect(url_for('front.home'))


# 显示某一类的问题页面
@front_bp.route('/category/<int:category_id>', defaults={'page': 1})
@front_bp.route('/category/<int:category_id>/page/<int:page>')
def show_category(category_id, page):
    # number is the total amount of questions displayed
    catid = category_id
    '''need change'''
    # ret = db.get_result({"function" : db.GET_QUESTION_BY_CAT, "content" :
    # {"number": 5, "start": 0, "catid": category_id}})
    per_page = current_app.config['QUESTIONS_PER_PAGE']  # 每页显示的数量
    ret = db.get_result(
        {"function": db.GET_QUESTION_BY_CAT, "content": {"number": per_page, "start": per_page * (page - 1), "catid": category_id}})
    if ret["content"]:
        page_record = Page(page, per_page)
        if page <= 1:
            page_record.has_prev = False
        else:
            page_record.has_prev = True
        if len(ret["content"]) < per_page:
            page_record.is_last = True
    else:
        page_record = Page(page, per_page, True)
        page_record.has_prev = True
    questions = ret["content"]  # 一个list对象
    return render_template('front/category.html', questions=questions, catid=catid, page=page_record)


# 显示单个问题及其回答的页面
@front_bp.route('/question/<int:question_id>', methods=['GET', 'POST'])
def show_question(question_id):
    form = AnswerForm()
    ret = db.get_result({"function" : db.GET_QUESTION_BY_ID, "content" : {"quid" : question_id}})
    question = ret["content"]  # dict对象
    ret = db.get_result({"function" : db.GET_ANSWER_BY_QUID, "content" : {"quid" : question_id}})
    answers = ret["content"]   # list对象

    if form.validate_on_submit():
        if current_user.is_authenticated:
            anscontent = form.answer.data
            quid = question_id
            uid = 2  # current_user.uid
            anstime = datetime.datetime.now()
            answer = AnswerInfo(
                anscontent=anscontent,
                anstime=anstime,
                uid=uid, # 回答者id
                quid=quid
            )
            db.get_result({"function" : db.INSERT_ANSWER, "content" : answer.to_dict()})
            flash('Answer published!')
            return redirect(url_for('front.show_question', question_id=question_id))
        else:
            return redirect(url_for('auth.login', next=request.full_path))
    return render_template('front/qna.html', question=question, answers=answers, form=form)


# 显示某个用户提出的问题
@front_bp.route('/myquestion/<int:user_id>', )
def myquestion(user_id):
    ret = db.get_result({"function" : db.GET_QUESTION_BY_UID, "content" : {
        "uid" : user_id
    }})
    questions = ret["content"]
    return render_template('front/myquestion.html', questions=questions)
