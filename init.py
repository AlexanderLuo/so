import codecs
import config
import json
import fn
import builder
import cach
import os
from queue import Queue



def initial():
    path=fn.thisPath("client.json")
    dic = json.load(codecs.open(path,encoding='utf8'))
    cr=cach.getInstance()
    cr.set("package",dic["package"])
    cr.set("packagePath",config.FILEPATH.THISPATH.value+dic["package"].replace(".",config.SEPARATION)+config.SEPARATION)
    cr.set("mysql",dic["mysql"])
    cr.set("plugin",dic["plugin"])
    fn.safeCopy(config.FILEPATH.NORMAL.value + ".gitignore", fn.thisPath(".gitignore"))
    if dic["frame"] == "springBoot":
        springBoot()






def springBoot():
    list=[]
    q = Queue()
    dic=config.PROTREE.SPRINGBOOT.value
    path = cach.getInstance().get("packagePath")



    list.append(key)
    builder.getInstance().build(list)


def parseQueue(queue,path):
    arr=queue.get()
    for fileObj in arr:
        for key,value in fileObj:
            if not os.path.exists(path + key):
                os.makedirs(path + key)
            if len(value) > 0:
                q.put()







