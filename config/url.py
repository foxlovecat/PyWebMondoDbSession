#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                pre_fix + 'views.Login',
    '/login',           pre_fix + 'views.Login',
    '/login_check',     pre_fix + 'common.LoginCheck',
    '/success',         pre_fix + 'views.Success'
)
