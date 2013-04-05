#!usr/bin/env python
# coding: utf-8
import web
from config.url import urls
import config.MongoStore

import config.setting
app = web.application(urls, globals())
db=config.setting.db
session = web.session.Session(app, config.MongoStore.MongoStore(db,'sessions'),
initializer={'login':"", 'user_name':'guest'})

def session_hook():
    web.ctx.session = session
    
app.add_processor(web.loadhook(session_hook))

#if web.config.get('_session') is None:
#    session = web.session.Session(app, web.session.DiskStore('sessions'))
#    web.config._session = session
#else:
#    session = web.config._session


if __name__ == "__main__":
    app.run()
