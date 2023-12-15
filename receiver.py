import socket
import math

HOST = "127.0.0.1"
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name,"wb")

file_bytes = b""

done = False


recv_size = pow(2,int(math.log(int(file_size),2)))

while not done:
    data = client.recv(recv_size)
    file_bytes += data
    if data[-5:] == b"<END>":
        done = True

file.write(file_bytes)

file.close()
server.close()