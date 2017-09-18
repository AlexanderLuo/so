

class plugin(object):
    cr = None
    instance= None
    arr=[]



    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = plugin()
            return cls.instance
        else:
            return cls.instance

    def apply(self,arr):
        self.arr+=arr
        while self.arr:
           self.load(self.arr.pop())



    def load(self,str):
        self.mapper[str][0](self,self.mapper[str][1])

    def swagger(self,str):
        module = __import__(str)
        print(module)

    mapper = {
        "swagger": [swagger, "loader.swagger"]
    }



def getInstance():
    return plugin.getInstance()



