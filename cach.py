
class SimpleCache(dict):

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

    def get(self,name,default=None):
        if not name:
            return default
        levels = name.split('.')
        data = self
        for level in levels:
            try:
                data = data[level]
            except:
                return default

        return data

    def set(self,name,value):
        levels = name.split('.')
        arr = self
        for name in levels[:-1]:
            if not arr.has_key(name):
                arr[name] = {}
            arr = arr[name]
        arr[levels[-1]] = value

    def getset(self,name,value):
        g = self.get(name)
        if not g:
            g = value
            self.set(name,g)
        return g

def scache(func):
    def wrapper(*args, **kwargs):
        cache = SimpleCache.getInstance()
        fn = "scache." + func.__module__ + func.__class__.__name__ + \
             func.__name__ + str(args) + str(kwargs)
        val = cache.get(fn)
        if not val:
            res = func(*args, **kwargs)
            cache.set(fn,res)
            return res
        return val
    return wrapper


def getInstance():
    return SimpleCache.getInstance()