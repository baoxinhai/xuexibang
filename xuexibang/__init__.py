# -*- coding: utf-8 -*-

from flask import Flask
# from wangzhedeDB import DB
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('xuexibang')
app.config.from_pyfile('../config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# db = APP
moment = Moment(app)  # 时间戳
bootstrap = Bootstrap(app)  # 开发模板

from main import views, errors, commands