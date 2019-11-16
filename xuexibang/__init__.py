# -*- coding: utf-8 -*-

from flask import Flask

from database.api.main_base import *

from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('xuexibang')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# db = APP
moment = Moment(app)  # 时间戳
bootstrap = Bootstrap(app)  # 开发模板

from main import views, errors, commands

'''
# success!
o = Operator()
res = o.get_result({"function": DATABASE_INIT, "content": "","dev":True})
print (res)
o.destroy()
'''