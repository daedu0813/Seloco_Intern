import socket
import time
import threading
import io
import atexit
import ConfigureProtocolMaker
import ipaddress

from flask import Flask
app = Flask(__name__)

from dataclasses import dataclass 

# Flask 라우트
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/seloco/")
def info():
    return "Hello, Seloco!"

# MAIN
if __name__ == "__main__":
    @dataclass
    class Device:
        device_name: str = None
        ip = bytearray()
        subnetmask = bytearray()
        gateway = bytearray()
        port: int = None
    
    selectedDevice = Device()
    deviceList = list()

    __UDPbroadcaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    __UDPbroadcasterEndpoint = __UDPbroadcaster.bind(ipaddress, 19860)
    __broadcasts_Address = ipaddress.ip_address('255.255.255.255')

    TCPListenthread : threading.Thread
    TCP_Client_Socket : socket
    UDPListenThread : threading.Thread
    configMaker : ConfigureProtocolMaker
    #__udpbroadcaster.connect((defaultDevice.ip, defaultDevice.port))
    # TCP_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #__udpbroadcasterEndpoint

    app.run()

# 프로그램 종료시
@atexit.register
def goodbye():
    print('Close Socket')
    # try:
    #     __udpbroadcaster.close()    # 소켓 닫는다
    # except:
    #     print('예외 발생')