#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

#  from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class LoginForm(FlaskForm):
    # 使用render_kw来为表单项增加属性placeholder
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': '请输入用户名'})
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 30)], render_kw={'placeholder': '不少于6位'})
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

