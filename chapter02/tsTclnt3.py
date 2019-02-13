# -*- coding: UTF-8 -*-

from socket import  *

HOST = '127.0.0.1' #此ip位服务端的地址
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ') #接收用户输入的数据 str
    if not data:
        break
    tcpCliSock.send(data.encode()) # send方法为byte，这里需要转换
    data = tcpCliSock.recv(BUFSIZE)
    if not  data:
        break
    print(data.decode('utf-8'))  #格式化接收到的数据
tcpCliSock.close()#关闭连接