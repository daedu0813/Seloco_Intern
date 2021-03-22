import socket
import time
import threading
import io
import atexit
import ConfigureProtocolMaker as configMaker
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
    __UDPbroadcaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    __UDPbroadcasterEndpoint = __UDPbroadcaster.bind(socket.gethostbyname(socket.gethostname()), 19860)
    __broadcasts_Address = ipaddress.ip_address('255.255.255.255')

    TCPListenthread : threading.Thread
    UDPListenThread = threading.Thread
    TCP_Client_Socket : socket
    
    selectedDeviceNameStr : str = None

    __net_init()
    UDPListenThread = threading.Thread(target=__startListener)
    UDPListenThread.start()

    deviceList = list()

    app.run()

    # 프로그램 종료시
    @atexit.register
    def goodbye():
        print('Close Socket')
        try:
            __UDPbroadcaster.close()    # 소켓 닫는다
        except:
            print('예외 발생')

    def __net_init():
        try:
            __UDPbroadcaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            __UDPbroadcaster.bind(socket.gethostbyname(socket.gethostname()), 19860)
        except:
            print("Error creating udp client ! port already in use?")

    working : bool = None
    __listenPort = 19860

    def __startListener():
        groupEP : socket = groupEP.bind('0.0.0.0', __listenPort)
        bytes = bytearray()
        working = True
        try:
            while working:
                print("waiting for broadcast")
                bytes = __UDPbroadcaster.recv(groupEP)

                print("Received UDP listener" + str(len(bytes)))
                if len(bytes) > 10:
                    parsing(bytes)
        except:
            print(str(ex))
        finally:
            __UDPbroadcaster.close()

    def parsing(message : bytearray()):
        if message[8] == 0x12:
            if message[9] == 0xB0:
                findNewDevice(message)
    
    def findNewDevice(message : bytearray()):
        tempDevice : Device
        address : bytes
        
        tempDevice = Device()
        
        tempDevice.device_name = message.encode("ascii")
