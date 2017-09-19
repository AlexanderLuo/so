import codecs
import shutil
import os
import time
import config


def safeCopy(source,target):
    if not os.path.exists(target):
        shutil.copy(source, target)



def safeCopyDir(source,target):
    shutil.copytree(source, target)




def thisPath(path=""):
    return config.FILEPATH.THISPATH.value+path


def authNote(title="empty",author="Alexander Luo(496952252@qq.com)"):
    st='    /**\n'+"    * %s" %(title)+"\n"+"    *"+"\n"+"    * @author %s" %(author)+"\n"+\
       "    * @date %s" %(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"\n"+"    *"+"\n"+"    */"+"\n"
    return st


def titleNote(title="empty"):
    st='    /**\n'+"    * %s" %(title)+"\n"+"    */"+"\n"
    return st

def underline2Camel(str):
    arr=str.split("_")
    i=1
    res=""
    while i<len(arr):
        res+=arr[i].capitalize()
        i+=1
    return arr[0]+res


def readAsLines(file):
    try:
        f=codecs.open(file, 'r', encoding='utf8')
        lines=f.readlines()
        f.close()
        return lines
    except Exception as err:
        print(err)

def openFile(file):
    return codecs.open(file,'w',encoding='utf8')


def pt(*args):
    for i in args:
        print(i)






