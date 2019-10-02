import socket
import time
import struct
import sys

f = open("datanode3/data.txt","w")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8000))

print("\nConectado a " + client.getpeername()[0] + "\n")

f.close()

while(True):

	from_server = client.recv(4096)

	if (from_server.decode("utf-8")=="ping"):
		msg = "pong"
		client.send(bytes(msg, 'utf-8'))
		print("se ha enviado respuesta a headnode")
	else:
		f = open("datanode3/data.txt","a")
		f.write(from_server.decode("utf-8")+"\n")
		f.close()
		print("se ha guardado en data")
		msg = "ok"
		client.send(bytes(msg, 'utf-8'))
