# 二进制读写文件

import struct
import base64

index = 0
filepath = "C:\\Users\\Administrator\\Desktop\\ElementCode.le"
binfile = open(filepath, 'rb')
bytes = binfile.read()
eleNum = struct.unpack("I", bytes[0:4])
print(type(eleNum))
index += 4
eleList = [[0 for i in range(14)] for i in range(eleNum[0])]
# H64s16sHHHHHHHHHHH
for i in eleList:
    i[0] = struct.unpack('H',  bytes[index:(index+2)])
    index += 2
    i[1] = struct.unpack('64s', bytes[index:(index + 64)])
    index += 64
    i[2] = struct.unpack('16s', bytes[index:(index + 16)])
    index += 16
    i[3] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[4] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[5] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[6] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[7] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[8] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[9] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[10] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[11] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[12] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
    i[13] = struct.unpack('H', bytes[index:(index + 2)])
    index += 2
print(eleList[0][1])
print(eleList[0][1][0])
binfile.close()

