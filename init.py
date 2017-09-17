import codecs
import config
import json
import fn
import builder
import cach



def initial():
    path=fn.thisPath("client.json")
    dic = json.load(codecs.open(path,encoding='utf8'))
    cr=cach.getInstance()
    cr.set("package",dic["package"])
    cr.set("packagePath",config.FILEPATH.THISPATH.value+dic["package"].replace(".",config.SEPARATION)+config.SEPARATION)
    cr.set("mysql",dic["mysql"])
    fn.safeCopy(config.FILEPATH.NORMAL.value + ".gitignore", fn.thisPath(".gitignore"))
    if dic["frame"] == "springBoot":
        springBoot()






def springBoot():
    list=config.PROTREE.SPRINGBOOT.value
    builder.getInstance(list).build()





