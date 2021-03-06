import platform
import os



SEPARATION="/"
system = platform.system()
if system == "Windows":
    SEPARATION="\\"
if system == "Linux":
    SEPARATION = "/"



# 路由管理
from enum import Enum, unique
@unique
class FILEPATH(Enum):
    THISPATH=os.getcwd()+SEPARATION
    EXAMPLE = '.'+SEPARATION+"example"+SEPARATION
    NORMAL = '.'+SEPARATION+"example"+SEPARATION+"normal"+SEPARATION
    SWAGGER = '.'+SEPARATION+"example"+SEPARATION+"swagger"+SEPARATION
    PO="."+SEPARATION+"example"+SEPARATION+"po"+SEPARATION
    SEARCHMODEL="."+SEPARATION+"example"+SEPARATION+"searchModel"+SEPARATION
    SPRINGBOOT="."+SEPARATION+"example"+SEPARATION+"springboot"+SEPARATION









# 额外信息
from enum import Enum, unique
@unique
class INFO(Enum):
    JAVANOTE = '.'+SEPARATION+"example"+SEPARATION
    NORMAL = '.'+SEPARATION+"example"+SEPARATION+"normal"+SEPARATION
    SWAGGER = '.'+SEPARATION+"example"+SEPARATION+"swagger"+SEPARATION


# 项目树
from enum import Enum, unique
@unique
class PROTREE(Enum):
    NORMAL =[{"lib":[]},{"src":[{"test":[]},{"main":[{"resources":[{"static":[]},{"META-INF":[{"resources":[]}]}]},{"java":[]}]}]}]
    SPRINGBOOT = [{"controller": []}, {"service": []}, {"dao":[{"impl": []}]},{"po": []}, {"config": []}, {"repository": []}, {"annotation": []}, {"filter": []}, {"util": []},{"apiModel": []}]







# MYSQL-JAVA类型映射表
from enum import Enum, unique
@unique
class TYPEMAP(Enum):
    MYSQL2JAVA = {
        "varchar":{"type":"String","rel":""},
        "char": {"type":"String","rel":""},
        "int":{"type":"int","rel":""},
        "tinyint": {"type":"int","rel":""},
        "bigint": {"type":"Long","rel":""},
        "double":{"type":"double","rel":""},
        "float":{"type":"float","rel":""},
        "datetime":{"type":"Date","rel":"import java.util.Date;"},
        "date":{"type":"Date","rel":"import java.util.Date;"}


    }






