import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 5000))

print("\nConectado a " + client.getpeername()[0] + "\n")

f = open("client/registro_cliente.txt","w")
f.write("id_data" + "\t\t" + "datanode guardado" + "\n")
f.close()

data = range(20)
contador = 0

while(True):

	print("Ingrese su solicitud:")
	if (contador<20):
		msg = "data" + str(data[contador])
		contador+=1
		print(msg)
	else:
		msg = input()

	if(msg == "quit()"):
		print("Cerrando programa...")
		client.close()
		break

	client.send(bytes(msg, 'utf-8'))
	from_server = client.recv(4096)
	f = open("client/registro_cliente.txt","a")
	f.write(str(contador) + "\t\t" + from_server.decode("utf-8") + "\n")
	f.close()
