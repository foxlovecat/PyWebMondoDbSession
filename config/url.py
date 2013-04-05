#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'
user_fix='views.'
urls = (
    '/',                pre_fix + 'views.Login',
    '/login',           pre_fix + 'views.Login',
    '/login_check',     pre_fix + 'common.LoginCheck',
    '/success',         pre_fix + 'views.Success',
    '/user/login',      user_fix+'Users.Login',
    '/user/getmy',      user_fix+'Users.GetMy'
)
roles = (
    '/',                False,
    '/login',           False,
    '/login_check',     False,
    '/success',         False,
    '/user/login',      False,
    '/user/getmy',      True
)
