import shutil
import os
import time


def safeCopy(source,target):
    print(target)
    if not os.path.exists(target):
        shutil.copy(source, target)

def javaNote(title="empty",author="Alexander Luo(496952252@qq.com)"):
    st='/**\n'+"* %s" %(title)+"\n"+"*"+"\n"+"* @author %s" %(author)+"\n"+"* @date %s" %(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"\n"+"*"+"\n"+"*/"+"\n"
    return st

