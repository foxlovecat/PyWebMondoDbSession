#!/usr/bin/env python
# coding: utf-8
import web
import pymongo
import gridfs
#db = web.database(dbn='mysql', db='py', user='root', pw='noans')
connection=pymongo.Connection('localhost',27017)
db=connection.pymongo
fs=gridfs.GridFS(db)
render = web.template.render('templetor/', cache=False)

web.config.debug = False

#if web.config.get('_session') is None:
#    session = web.session.Session(app, web.session.DiskStore('sessions'))
#    web.config._session = session
#else:
#    session = web.config._session

config = web.storage(
    email = 'foxlovecat@gmail.com',
    site_name = 'Jikei.LIu',
    site_des = '',
    static = '/static'
)

