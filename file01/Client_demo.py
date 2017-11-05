# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9995)

sk = socket.socket()
sk.connect(ip_port)
sk.sendall(bytes('占领地球','utf8'))
server_reply = sk.recv(1024)
print (str(server_reply,'utf8'))
while True:
    user_input=input(">>>>>:").strip()    #用户输入的内容
    sk.send(bytes(user_input,'utf8'))     #
    server_reply = sk.recv(1024)
    print(str(server_reply, 'utf8'))
sk.close()