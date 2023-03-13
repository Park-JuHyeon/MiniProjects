# mp08 - 컴퓨터 정보확인 앱
import psutil
import socket
import requests   # pip install requests로 추가
import re

print(psutil.cpu_freq())

in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)


