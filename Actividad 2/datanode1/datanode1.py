import socket
import time

f = open("datanode1/data.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 6000))

f.write("\nConectado a " + client.getpeername()[0])
f.write("\n\nRespuestas\n")

print("\nConectado a " + client.getpeername()[0] + "\n")

f.close()

while(True):

	print("soy el datanode1")

	from_server = client.recv(4096)

	f = open("datanode1/data.txt","a")
	f.write("hola")
	f.close()

	f = open("datanode1/data.txt","a")
	if (from_server.decode("utf-8") == 'estan vivos'):
		f.write("llego mensaje\n")
	print(from_server.decode("utf-8") + "\n")
	f.write(from_server.decode("utf-8") + "\n")
	f.close()
