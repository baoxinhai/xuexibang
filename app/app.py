# -*- coding: utf-8 -*-

__author__ = "Jinyang Shao"

import os
from flask import Flask, render_template, flash, redirect, url_for

from forms import LoginForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'our secret')
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
def hello():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html', data=['some', 'data', 'from', 'the', 'back', 'end'])


# 对于URL http://localhost:5000/watchlist
@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)  # 返回带数据的html文档


@app.route('/register')
def register():
    form = LoginForm()
    return render_template('register.html', data=['data'], form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html', data=['data'])


@app.route('/myquestion')
def myquestion():
    return render_template('myquestion.html', data=['data'])


@app.route('/qna')
def qna():
    return render_template('qna.html', data=['data'])

