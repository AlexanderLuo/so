import pymysql
import cach



class dataBase(dict):
    db=None
    def __new__(cls,*args):
        if not hasattr(cls,'_instance'):
            cls._instance = dict.__new__(cls)
        else:
            raise Exception('SimpleCache already initialized')
        return cls._instance
    @classmethod
    def getInstance(cls):
        if not hasattr(cls,'_instance'):
            cls._instance = dict.__new__(cls)
        return cls._instance
    def getDb(self):
        if self.db is not None:
            return self.db
        try:
            cfi=cach.getInstance().get("mysql")
            cfi["cursorclass"]=pymysql.cursors.DictCursor
            self.db=pymysql.connect(**cach.getInstance().get("mysql"))
            return self.db
        except Exception as err:
            print(err)


    def set(self,name,value):
        levels = name.split('.')
        arr = self
        for name in levels[:-1]:
            if not arr.has_key(name):
                arr[name] = {}
            arr = arr[name]
        arr[levels[-1]] = value


def getInstance():
    return dataBase.getInstance()