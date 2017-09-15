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
    SPRINGBOOT = ["controller","service","dao","po","config","repository","annotations",]




