import codecs

import config
import json
import fn






def initial():
    path=config.FILEPATH.THISPATH.value+"client.json"
    dic = json.load(codecs.open(path,encoding='utf8'))
    builder(dic)



    # fn.safeCopy(config.FILEPATH.NORMAL.value+".gitignore", config.FILEPATH.THISPATH.value)

def builder(dic):
    if dic["frame"]=="springBoot":
        springBoot(dic)




def springBoot(dic):
    path=dic["package"]
    list=config.PROTREE.SPRINGBOOT.value;



