import platform

SEPARATION="/"
system = platform.system()
if system == "Windows":
    SEPARATION="\\"
if system == "Linux":
    SEPARATION = "/"
