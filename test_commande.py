import os
import socket
import platform
import sys
import psutil
from socket import *

print ("utilisation actuelle du processeur en % ->",str(psutil.cpu_times_percent()))
print (gethostbyname(gethostname()))
print("Pourcentage de la RAM utilisé :  ",psutil.virtual_memory().percent)
print(platform.system())
print("version de python: ",sys.version)
