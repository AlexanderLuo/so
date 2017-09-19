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
    jsonFilePath=fn.thisPath("client.json")
    rootPath=config.FILEPATH.THISPATH.value
    dic = json.load(codecs.open(jsonFilePath,encoding='utf8'))
    cr=cach.getInstance()
    cr.set("package",dic["package"])
    cr.set("packagePath",rootPath+"src"+config.SEPARATION+"main"+config.SEPARATION+"java"+config.SEPARATION+dic["package"].replace(".",config.SEPARATION)+config.SEPARATION)
    cr.set("mysql",dic["mysql"])
    cr.set("plugin",dic["plugin"])

    fn.safeCopy(config.FILEPATH.NORMAL.value + ".gitignore",rootPath+".gitgnore")

    if dic["language"]=="JAVA":
        tree=config.PROTREE.NORMAL.value
        root={"arrTree":tree,"path":rootPath}
        q=Queue()
        q.put(root)
        javaTree(q)
        if dic["frame"] == "springBoot":
            springBoot()





buildList = []
def springBoot():
    buildList.append("springBoot")
    cr = cach.getInstance()
    arrTree=config.PROTREE.SPRINGBOOT.value
    path = cr.get("packagePath")
    node={ "arrTree":arrTree ,"path": path }
    q = Queue()
    q.put(node)
    parseQueue(q)
    builder.getInstance().build(buildList)
    plugin.getInstance().apply(cr.get("plugin"))




def parseQueue(queue):
    if queue.empty():
        return
    node=queue.get()
    arrTree=node["arrTree"]
    path=node["path"]
    for fileObj in arrTree:
        for key in fileObj:
            buildList.append(key)
            if not os.path.exists(path + key):
                os.makedirs(path + key)
            if len(fileObj[key]) > 0:
                node={"arrTree":fileObj[key],"path":path+config.SEPARATION+key+config.SEPARATION}
                queue.put(node)
    parseQueue(queue)


def javaTree(queue):
    if queue.empty():
        return
    node=queue.get()
    arrTree=node["arrTree"]
    path=node["path"]
    for fileObj in arrTree:
        for key in fileObj:
            if not os.path.exists(path + key):
                os.makedirs(path + key)
            if len(fileObj[key]) > 0:
                node={"arrTree":fileObj[key],"path":path+config.SEPARATION+key+config.SEPARATION}
                queue.put(node)
        javaTree(queue)







