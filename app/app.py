# -*- coding: utf-8 -*-

__author__ = "Jinyang Shao"

import os
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

user = {
    'username': 'sjy',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


# 对于URL http://localhost:5000/
@app.route('/')
def index():
    return '<h1>Hello world</h1>'  # 返回一个html元素


# 对于URL http://localhost:5000/home
@app.route('/home')
def home():
    return render_template('home.html', data=['some', 'data', 'from', 'the', 'back', 'end'])


# 对于URL http://localhost:5000/watchlist
@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)  # 返回带数据的html文档
