import socket

server_addr = ('127.0.0.1', 55555)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('>')
    print(msg)
    s.sendto(msg.encode('utf-8'), server_addr)
    if msg is 'bye':
        break
s.close()

