from collections import namedtuple
from dataclasses import dataclass 

arr = [1,2,3,"11","22", 0xFF]

dataPacket = [None] * len(arr)
Device = namedtuple("Device", "device_name ip subnetmask gateway port")
d = Device(None, None, None,0x55, 8080)

abc = bytearray()
bbb = bytearray(10)

abc = bbb
abc[0] = 0xA1

@dataclass
class Product:
    weight = bytearray(2)
    price = bytearray(2)
    sttr: str = None

pr = Product()

pr.price[0] = 0x22

barr = bytearray(5)

# print(d)

# print(pr)

print(abc)

# for i in barr:
#     print(i)