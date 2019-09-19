import socket
import time

f = open("respuestas.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))
f.write("\n\nRespuestas\n")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 5000))
client.send(bytes('¡Hola!', 'utf-8'))
from_server = client.recv(4096)
f.write(from_server.decode("utf-8") + "\n")

while(True):

	msg = input()
	client.send(bytes(msg, 'utf-8'))
	from_server = client.recv(4096)
	#client.close()
	print(from_server.decode("utf-8"))
	f.write(from_server.decode("utf-8") + "\n")