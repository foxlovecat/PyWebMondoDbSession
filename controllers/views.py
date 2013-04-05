#!/usr/bin/env python
# coding: utf-8
import web
from config.setting import render
#from code import session
session = web.ctx.session

class Login:
    def GET(self):
        return render.login()

class Success:
    def GET(self):
        if session.loginned == True:
            return render.success(session.username, web.cookies().get('test'))
        return render.login()
