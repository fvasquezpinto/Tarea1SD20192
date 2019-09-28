import socket
import time

f = open("datanode3/data.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8000))

f.write("\nConectado a " + client.getpeername()[0])
f.write("\n\nRespuestas\n")

print("\nConectado a " + client.getpeername()[0] + "\n")

client.send(bytes('¡Hola!', 'utf-8'))
from_server = client.recv(4096)
f.write(from_server.decode("utf-8") + "\n")

f.close()

f = open("datanode3/data.txt","a")

while(True):

	from_server = client.recv(4096)
	print(from_server.decode("utf-8") + "\n")
	f.write(from_server.decode("utf-8") + "\n")

f.close()