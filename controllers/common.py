#!/usr/bin/env python
# coding: utf-8
import web
from config import setting
#import code

db = setting.db
render = setting.render
session = web.ctx.session

class LoginCheck:
    def POST(self):
        name, pwd = web.input().name, web.input().pwd
        if name != None and pwd != None:
            myvar = dict(name=name)
            result = db.select('tuser', myvar, what='pwd')
            if result != None and pwd == result[0].pwd:
                web.setcookie('test', 'cookice_test', 60)
                session.loginned = True
                session.username = name
                return render.success(name, 'cookie test')
        raise web.seeother('/login')

