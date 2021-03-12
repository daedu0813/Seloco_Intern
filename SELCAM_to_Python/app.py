import socket
import time
import threading
import io
import atexit

from flask import Flask
app = Flask(__name__)

from collections import namedtuple
Device = namedtuple("Device", "device_name ip subnetmask gateway port")
defaultDevice = Device("SenTerm", "192.168.0.254", "255.255.255.0", "192.168.0.1", 19860)
#selectedDevice
#deviceList

__udpbroadcaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
__udpbroadcaster.connect((defaultDevice.ip, defaultDevice.port))
TCP_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#__udpbroadcasterEndpoint


@app.route("/")
def home():
    
    return "Hello, Flask!"

@app.route("/seloco/")
def info():
    return "Hello, Seloco!"

# 프로그램 종료시
@atexit.register
def goodbye():
    print('Close Socket')
    try:
        __udpbroadcaster.close()    # 소켓 닫는다
    except:
        print('예외 발생')