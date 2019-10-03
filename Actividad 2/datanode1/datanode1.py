import socket
import time
import struct
import sys

# f = open("datanode1/data.txt","w")

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('0.0.0.0', 6000))

# print("\nConectado a " + client.getpeername()[0] + "\n")

# f.close()

multicast_group = '224.10.10.10'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to
# the multicast group on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq)

# Receive/respond loop
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    print('sending acknowledgement to', address)
    sock.sendto(b'ack', address)

# while(True):

# 	from_server = client.recv(4096)

# 	if (from_server.decode("utf-8")=="ping"):
# 		msg = "pong"
# 		client.send(bytes(msg, 'utf-8'))
# 		print("se ha enviado respuesta a headnode")
# 	else:
# 		f = open("datanode1/data.txt","a")
# 		f.write(from_server.decode("utf-8")+"\n")
# 		f.close()
# 		print("se ha guardado en data")
# 		msg = "ok"
# 		client.send(bytes(msg, 'utf-8'))


