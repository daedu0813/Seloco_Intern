arr = [1,2,3,"11","22", 0xFF]

dataPacket = [None] * len(arr)

barr = bytearray(5)

#print(arr[5])
barr[3] = ord('a')

for i in barr:
    print(i)