import codecs
import config
import json
import fn
import builder
import plugin
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
    if dic["language"]=="JAVA":

        if dic["frame"] == "springBoot":
            springBoot()





list=[]


def springBoot():
    cr = cach.getInstance()
    q = Queue()
    arrTree=config.PROTREE.SPRINGBOOT.value
    path = cach.getInstance().get("packagePath")
    node={ "arrTree":arrTree ,"path": path }
    q.put(node)
    parseQueue(q)
    # builder.getInstance().build(list)
    plugin.getInstance().apply(cr.get("plugin"))


def parseQueue(queue):
    if queue.empty():
        return
    node=queue.get()
    arrTree=node["arrTree"]
    path=node["path"]
    for fileObj in arrTree:
        for key in fileObj:
            list.append(key)
            if not os.path.exists(path + key):
                os.makedirs(path + key)
            if len(fileObj[key]) > 0:
                node={"arrTree":fileObj[key],"path":path+config.SEPARATION+key+config.SEPARATION}
                queue.put(node)
    parseQueue(queue)









