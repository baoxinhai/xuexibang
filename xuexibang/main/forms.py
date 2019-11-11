# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

from flask_ckeditor import CKEditorField  # 富文本编辑器
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


def passwdEqual(form, field, passwd):
    if passwd is None:
        raise ValidationError("please input password")
    if field.data != passwd:
        raise ValidationError("两次输入密码不一致!")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    reinputpasswd = PasswordField('RePassword', validators=[DataRequired(), Length(8, 128), passwdEqual(password)])
    submit = SubmitField('Register')
