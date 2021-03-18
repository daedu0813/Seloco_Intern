from typing import Protocol


class ConfigureProtocolMaker:
    __Protocol_Ver = "0001"

    def ConfigureParsing(bytes, length):
        return 0
    
    def makeSearchMessage(HW_name):
        message = bytearray(20)
        tempbuff = bytearray()
        protocol = bytearray(10)
        
        #SOF    [VB에서는 '&H' Python에서는 '0x']
        message[0] = 0xFF
        message[1] = 0x53

        #Protocol version '0001'
        protocol =  StringToBytes(__Protocol_Ver)   # Protocol version length 4
        message[2] = protocol[0]
        message[3] = protocol[1]
        message[4] = protocol[2]
        message[5] = protocol[3]

        #Data length
        message[6] = 0
        message[7] = 8

        #Service Type
        message[8] = 0x21   #Tool to device
        
        #Service ID
        message[9] = 0xA0   #Set IP command

        #Data get all the node info
        tempbuff = StringToBytes(HW_name)   # HW name length 8

        message[10] = tempbuff[0]
        message[11] = tempbuff[1]
        message[12] = tempbuff[2]
        message[13] = tempbuff[3]
        message[14] = tempbuff[4]
        message[15] = tempbuff[5]
        message[16] = tempbuff[6]
        message[17] = tempbuff[7]

        #SOF
        message[18] = 0xFF
        message[19] = 0x45

        makeSearchMessage = message

    def makeNetworkSettingMessage(HW_name, IP, subnetmask, gateway, port):
        message = bytearray(38)
        tempbuff = bytearray()
        protocol = bytearray(10)
        pos = 0

        #SOF
        message[0] = 0xFF
        message[1] = 0x53

        pos = 2
        #Potocol version '0001'
        protocol = StringToBytes(__Protocol_Ver)    #Protocol verion length 4
        message[2] = protocol[0]
        message[3] = protocol[1]
        message[4] = protocol[2]
        message[5] = protocol[3]

        pos = 6
        #Data length
        message[6] = 0
        message[7] = 26

        pos = 8
        #Service Type
        message[8] = 0x21 #Tool to device
        #Service ID
        message[9] = 0xA1 #Set IP command

        pos = 10
        #Data get all the node info
        tempbuff = StringToBytes(HW_name)   # HW Name length 8
        print('HW Name' + str(len(tempbuff)))
        for i in range(0, len(tempbuff) -2):
            message[pos] = tempbuff[i]
            pos = pos + 1
        print('hw pos' + str(pos))

        message[pos] = 0x25 # %
        pos = pos + 1

        tempbuff = StringToBytes(IP)
        tempbuff = __IPto4B(tempbuff)
        for i in range(0, len(tempbuff) -2):
            message[pos] = tempbuff[i]
            pos = pos + 1
        print('ip pos ' + str(pos))
        message[pos] = 0x25 # %
        pos = pos + 1

        tempbuff = StringToBytes(subnetmask)
        tempbuff = __IPto4B(tempbuff)
        for i in range(0, len(tempbuff) -2):
            message[pos] = tempbuff[i]
            pos = pos + 1
        print('sub pos ' + str(pos))
        message[pos] = 0x25 # %
        pos = pos + 1

        tempbuff = StringToBytes(gateway)
        tempbuff = __IPto4B(tempbuff)
        for i in range(0, len(tempbuff) -2):
            message[pos] = tempbuff[i]
            pos = pos + 1
        print('gw pos ' + str(pos))
        message[pos] = 0x25 # %
        pos = pos + 1 

        message[pos] = port // 256
        message[pos + 1] = port % 256
        print('port: ' + str(pos))

        pos = pos + 2
        #SOF
        message[pos] = 0xFF
        message[pos + 1] = 0x45
        print(len(message))
        makeNetworkSettingMessage = message

    def makeDHCPSettingMessage(HW_name, port):
        message = bytearray(38)
        tempbuff = bytearray()
        protocol = bytearray(10)

        #SOF
        message[0] = 0xFF
        message[1] = 0x53

        pos = 2
        #Protocol version '0001'
        protocol = StringToBytes(__Protocol_Ver)    # Protocol version length 4
        message[2] = protocol[0]
        message[3] = protocol[1]
        message[4] = protocol[2]
        message[5] = protocol[3]

        pos = 6
        #Data length
        message[6] = 0
        message[7] = 11

        pos = 8
        #Service Type
        message[8] = 0x21   #Tool to device
        #Servcie ID
        message[9] = 0xA3   #set DHCP command

        pos = 10
        #Data get all the node info
        tempbuff = StringToBytes(HW_name)   # HW Name length 8
        print('HW Name' + str(len(tempbuff)))
        for i in range(0, len(tempbuff) -2):
            message[pos] = tempbuff[i]
            pos = pos + 1

        print('hw pos' + str(pos))
        message[pos] = 0x25 # %
        pos = pos + 1

        message[pos] = port // 256
        message[pos + 1] = port % 256
        print('port: ' + str(pos))

        pos = pos + 2
        #SOF
        message[pos] = 0xFF
        message[pos + 1] = 0x45
        print(len(message))
        makeDHCPSettingMessage = message

    def makeChangeDeviceNameMessage(Old_HW_Name, New_HW_Name):
        message = bytearray(38)
        tempbuff = bytearray()
        protocol = bytearray()

        #SOF
        message[0] = 0xFF
        message[1] = 0x53

        pos = 2
        #Protocol version '0001'
        protocol = StringToBytes(__Protocol_Ver)    # Protocol Verison length 4
        message[2] = protocol[0]
        message[3] = protocol[1]
        message[4] = protocol[2]
        message[5] = protocol[3]

        pos = 6
        #Data length
        message[6] = 0
        message[7] = 0x11

        pos = 8
        #Service Type
        message[8] = 0x21   #Tool to device
        #Service ID
        message[9] = 0xA4   #Set New DeviceID command

        pos = 10
        #Data get all the node info
        tempbuff = StringToBytes(Old_HW_Name)   #HW Name length 8
        print("Old HW Name" + str(len(tempbuff)))
        for i in range(0, len(tempbuff)-2):
            message[pos] = tempbuff[i]
            pos = pos + 1
        
        print("HW Pos " + str(pos))
        message[pos] = 0x25 # %
        pos = pos + 1

        tempbuff = StringToBytes(New_HW_Name) # HW Name length 8
        print("New HW Name " + str(len(tempbuff)))
        for i in range(0, len(tempbuff) - 2):
            message[pos] = tempbuff[i]
            pos = pos + 1

        #SOF
        message[pos] = 0xFF
        message[pos + 1] = 0x45
        print(len(message))
        makeChangeDeviceNameMessage = message

    def makeDeviceRTCMessage(HW_Name, RTCStr):
        message = bytearray(38)
        tempbuff = bytearray()
        protocol = bytearray(10)

        #SOF
        message[0] = 0xFF
        message[1] = 0x53

        pos = 2
        #Protocol version '0001'
        protocol = StringToBytes(__Protovol_Ver)    # Protocol verion length 4
        message[2] = protocol[0]
        message[3] = protocol[1]
        message[4] = protocol[2]
        message[5] = protocol[3]

        pos = 6
        #Data length
        message[6] = 0
        message[7] = 0x17

        pos = 8
        #Service Type
        message[8] = 0x21   #Tool to device
        #Service ID'
        message[9] = 0xA5   #Set Device RTC

        pos = 10
        #Data get all the node info
        tempbuff = StringToBytes(HW_Name)   #HW Name length 8
        print("Old HW Name" + str(len(tempbuff)))
        for i in range(0, len(tempbuff) -2):
            message[pos] = tempbuff[i]
            pos = pos + 1

        print("hw pos: " + str(pos))
        message[pos] = 0x25 # %
        pos = pos + 1

        tempbuff = StringToBytes(RTCStr)    # HW Name length 8
        print("RTC" + str(len(tempbuff)))
        for i in range(0, len(tempbuff) - 2):
            message[pos] = tempbuff[i]
            pos = pos + 1

        #SOF
        message[pos] = 0xFF
        message[pos+1] = 0x45
        print(len(message))
        makeDeviceMessage = message

    def makeSEMSIPSettingMessage(HW_Name, SEMSServerIP, port):
        message = bytearray(35)
        tempbuff = bytearray()
        protocol = bytearray(10)

        #SOF
        message[0] = 0xFF
        message[1] = 0x53

        pos = 2
        #Protocol version '0001'
        protocol = StringToBytes(__Protocol_Ver)    # Protocol verion length 4
        message[2] = protocol[0]
        message[3] = protocol[1]
        message[4] = protocol[2]
        message[5] = protocol[3]

        pos = 6
        #Data length
        message[6] = 0
        message[7] = 16

        pos = 8
        #Service Type
        message[8] = 0x21   #Tool to device
        #Service ID
        message[9] = 0xA2   #Set IP Command

        pos = 10
        #Data get all the node info
        tempbuff = StringToBytes(HW_Name)
        print("HW Name" + str(len(tempbuff)))

        for i in range(0, len(tempbuff)-2):
            message[pos] = tempbuff[i]
            pos = pos + 1
        print("hw pos " + str(pos))

        message[pos] = 0x25 # %
        pos = pos + 1

        tempbuff = StringToBytes(SEMSServerIP)
        tempbuff = IPto4B(tempbuff)
        for i in range(0, len(tempbuff)-2):
            message[pos] = tempbuff[i]
            pos = [pos + 1]
        print("SEMSServerIP " + str(pos))

        message[pos] = 

        


#-----------------------------------------------------------------------------------#

    def StringToBytes(Data):
        dataPacket = bytearray(len(Data))   # 배열은 0부터 시작함
        try:
            myLoop = None
            myIndex = None
            
            myIndex = 0

            cmdbytes = Data.encode('ascii')

            for myLoop in range(0, len(Data.encode('ascii')) - 1):
                dataPacket[myIndex] = cmdbytes[myLoop]
                myIndex += 1
        except:
            print('예외 발생')

        StringToBytes = dataPacket

    def __IPto4B(address):
        temp = bytearray(4)
        pos = 0

        for i in range(0, 3):
            temp[i] = 0
            for k in range(0, 3):
                if address[pos] == 0x2E:
                    pos = pos + 1
                    break
                else:
                    temp[i] = temp[i] * 10 + (address[pos] - 0x30)
                    pos = pos + 1
                    if pos > (len(address) -2):
                        break
            if pos > (len(address) -2):
                break
        
        __IPto4B = temp
    
#-----------------------------------------------------------------------------------#