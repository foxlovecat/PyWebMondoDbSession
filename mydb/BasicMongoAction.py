from config.setting import *
from bson.objectid import *
class BasicMongoAction:
    tableName=''
    def __init__(self,tableName):
        self.tableName=tableName
        pass
    def getTb(self):
        return db[self.tableName]
    def getOfid(self,_id):
        return self.getTb().find_one({'_id':ObjectId(_id)})
    def getOfFiledValue(self,idName,value):
        return _self.getTb().find_one({idName:value})
    def delOfid(self,_id):
        self.getTb().remove({'_id':ObjectId(_id)})
        pass
    def save(self,maps):#return OjbectId()
        return self.getTb().save(maps)
    def saveList(self,maps):#return set(OjbectId)
        res=set()
        for tmp in maps:
            res.add(self.save(tmp))
            pass
        return res
    def getCount(self):
        return self.getTb().count()
    

            

            
