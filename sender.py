import os
import socket
import math

HOST = "127.0.0.1"
PORT = 9090

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

file = open("PROClient_86.zip","rb")
file_size = os.path.getsize("PROClient_86.zip")


client.send("RECV.zip".encode())
client.send(str(file_size).encode())

# data = file.read()
client.sendall(file.read())
client.send(b"<END>")

file.close()
client.close()