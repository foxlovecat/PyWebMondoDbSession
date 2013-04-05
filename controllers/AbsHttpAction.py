#!/usr/bin/env python
# coding: utf-8
import web
from config.setting import render
import config.setting
import json
from datetime import date,datetime
from config.url import roles

#from code import session

#json time encode
def _jsonDatetime(obj):
    if isinstance(obj,datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj,date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)

class AbsHttpAction:
    ssc={}
    ssc['isrequest']=True
    ssc['errorCode']=0
    ssc['errorNote']=''

    session = web.ctx.session
    db = config.setting.db

    def GET(self):
        '''this is http do get!'''
        try:
            urls=web.ctx.path
            index=roles.index(urls)
            print (urls+"indexOf:"+str(index))
            
            if index >=0:
                getrole=roles[index+1]
                print (getrole)
                if getrole==True:
                    print(self.session.get('user'))
                    #print(type())
                    if self.session.get('user')==None or self.session.get('user').strip()=='':
                        print('no login')
                        self.setError(555,u'没有登录')                        
                        return self.toJson(self.ssc).encode('gbk')
            request=web.input()
            values={}
            try:                
                tmpvalue=request.value
                print(tmpvalue)
                values=self.formJson(tmpvalue)
            except:
                pass
            self.doPostGet(request,values)
        except Exception,error:
            self.setError(101,u'执行错误')
            print (erroe)
            pass
        finally:
            return self.toJson(self.ssc).encode('gbk')
        
    def POST(self):
        '''this is http do post!'''
        return self.GET()
        
    def setError(self,code1,err):
        print("set ssc vlaue:code="+str(code1)+";err="+err)
        self.ssc['errorCode']=code1
        self.ssc['errorNote']=err
        pass
    
    def setValue(self,val):
        print(val)
        self.ssc['value']=val
        pass
    def setOther(self,val):
        self.ssc['other']=val
        pass
    def toJson(self,val):
        return json.dumps(val,default=_jsonDatetime,ensure_ascii=False)
    def formJson(self,val):
        return json.loads(val)
    def doPostGet(self,request,values):
        pass


