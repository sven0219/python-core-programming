from socket import *

HOST = '127.0.0.1' #此ip位服务端的地址
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode())
udpCliSock.close()