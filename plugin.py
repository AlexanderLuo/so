

class plugin(object):
    cr = None
    instance= None
    arr=[]


    def __init__(self, arr=None):
        if arr is None:
            arr = {}
        self.arr = arr

    @classmethod
    def getInstance(cls, arr=[]):
        if cls.instance is None:
            cls.instance = plugin(arr)
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



def getInstance(arr):
    return plugin.getInstance(arr)



