class ConfigureProtocolMaker:
    __Protocol_Ver = "0001"

    def ConfigureParsing(bytes, length):
        return 0
    
    def makeSearchMessage(HW_name):
        message = []
        tempbuff = []
        protocol = []
        
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
        message = []
        tempbuff = []
        protocol = []

        #SOF
        message[0] = 0xFF
        message[1] = 0x53

        #pos=2
        #Potocol version '0001'
        protocol = StringToBytes(__Protocol_Ver)    #Protocol verion length 4

#-----------------------------------------------------------------------------------#

    def StringToBytes(Data):
        dataPacket = [None] * len(Data) #배열은 0부터 시작함
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
        temp = [0] * 4

        for i in range(0, 3):
            temp[i] = 0
            for k in range(0, 3):
                if address