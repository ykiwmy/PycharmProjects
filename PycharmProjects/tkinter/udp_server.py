import socket

BUFF_SIZE = 1024
server_addr = ('127.0.0.1', 55555)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)            # SOCK_DGRAM是UDP传输协议
s.bind(server_addr)
print('bind ok!')

while True:
    data, addr = s.recvfrom(BUFF_SIZE)
    print(data)
    if data is 'bye':
        print('client has exit')
        break
    print('received:', data, " from", addr)
s.close()
