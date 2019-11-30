# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

from flask_ckeditor import CKEditorField  # 富文本编辑器
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class LoginForm(FlaskForm):
    # 使用render_kw来为表单项增加属性placeholder
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'username'})
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 30)], render_kw={'placeholder': '>=6'})
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    reinputpasswd = PasswordField('RePassword', validators=[DataRequired(), Length(8, 128)])  # 未添加验证
    submit = SubmitField('Register')


class PostQuestionForm(FlaskForm):
    title = StringField('QTitle', validators=[DataRequired()], render_kw={'placeholder': 'question category'})
    content = StringField('Content', validators=[DataRequired()], render_kw={'placeholder': 'question description'})
    category = SelectField('Category', coerce=int, default=1) # 分类字段
    submit = SubmitField('issue')


class PostAnswerForm(FlaskForm):
    answer = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('issue')
