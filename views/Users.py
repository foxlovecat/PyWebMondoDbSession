#!/usr/bin/env python
# coding: utf-8
import web
from config.setting import render
import json
import controllers.AbsHttpAction
#from code import session
#session = web.ctx.session

class Login(controllers.AbsHttpAction.AbsHttpAction):
    
    def doPostGet(self,request,values):       
        if values == None:
            self.ssc['errorCode']=104
            return         
        
        if values.get('id')==None:
            self.ssc['errorCode']=102
            return 
        if values.get('pw')==None:
            self.ssc['errorCode']=103
            return
        self.setValue(u'执行陈功了啊')
        return

class GetMy(controllers.AbsHttpAction.AbsHttpAction):
    
    def doPostGet(self,request,values):       
        if values == None:
            self.ssc['errorCode']=104
            return         
        
        if values.get('id')==None:
            self.ssc['errorCode']=102
            return 
        if values.get('pw')==None:
            self.ssc['errorCode']=103
            return
        self.setValue(u'执行陈功了啊')
        return 
