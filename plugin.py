from xml.dom.minidom import parse
import xml.dom.minidom
import config


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
            name=self.arr.pop()
            self.pomRel(name)
            self.load(name)


    def load(self,name):
        self.mapper[name][0](self,self.mapper[name][1])

    def swagger(self,name):
        module = __import__(name)


    def shiro(self,name):
        module = __import__(name)

    def pomRel(self,name):
        path=self.mapper[name][2]
        if path:
            doc = xml.dom.minidom.parse(path).documentElement
            print(doc)
            # 使用minidom解析器打开 XML 文档
            DOMTree = xml.dom.minidom.parse("pom.xml")
            collection = DOMTree.documentElement
            dependencies = collection.getElementsByTagName("dependencies")
            dependencies[0].appendChild(doc)
            f = open("pom.xml", "wb")
            f.write(DOMTree.toprettyxml("", "", encoding="utf-8"))
            f.close()




    mapper = {
        "swagger": [swagger, "loader.swagger",config.FILEPATH.SWAGGER.value + "pom"],
        "shiro"  : [shiro,"loader.shiro",""]
    }



def getInstance():
    return plugin.getInstance()



