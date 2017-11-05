# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1',9995)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print ('server waiting...')
    conn,addr = sk.accept()
    client_data = conn.recv(1024)
    print (str(client_data,'utf8'))
    conn.sendall(bytes('不要回答,不要回答,不要回答','utf8'))
    while True:
        client_data = conn.recv(1024)
        print(str(client_data, 'utf8'))
        server_response=input(">>>>>>>:")   #服务器要说的话请用户输入
        conn.send(bytes(server_response,'utf8'))  #把用户输入的内容发出去

    conn.close()