# coding: utf-8
from socket import *
HOST = gethostname()
PORT = 34512
BUFSIZE = 1024
ADDR = (gethostbyname(HOST), PORT)
USER = 'Client'
udpClntSock = socket(AF_INET, SOCK_DGRAM)
while True:
    # data = input('%s > ' % USER) # 標準入力からのデータ入力
    data = "Hello"
    udpClntSock.sendto(data.encode('utf-8'), ADDR) # データ送信
    #udpClntSock.setblocking(0)# Non blocking
    if not data:
        break
udpClntSock.close()