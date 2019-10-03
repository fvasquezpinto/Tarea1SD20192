import socket
import time
import threading
import struct
import random

print("Server iniciado")
f = open("hearbeat_server.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))
f.write("\n\nIP\t\t\tMensaje\n")
f.close()

# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind(('0.0.0.0', 5000))
# serv.listen()

# datanode1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# datanode1.bind(('0.0.0.0', 6000))
# datanode1.listen()


# datanode2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# datanode2.bind(('0.0.0.0', 7000))
# datanode2.listen()

# datanode3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# datanode3.bind(('0.0.0.0', 8000))
# datanode3.listen()

# conn, addr = serv.accept()
# conn1, addr1 = datanode1.accept()
# conn2, addr2 = datanode2.accept()
# conn3, addr3 = datanode3.accept()

message = b'very important data'
multicast_group = ('224.10.10.10', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
sock.settimeout(3)

# Set the time-to-live for messages to 1 so they do not
# go past the local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

i = 0

while(i<10):

    try:

        # Send data to the multicast group
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, multicast_group)

        # Look for responses from all recipients
        while True:
            print('waiting to receive')
            try:
                data, server = sock.recvfrom(16)
            except socket.timeout:
                print('timed out, no more responses')
                break
            else:
                print('received {!r} from {}'.format(
                    data, server))

    finally:
        print('closing socket')
        #sock.close()

    i += 1

# class Datanodes(threading.Thread):
#     def run(self):

#         while True:


#             time.sleep(5)


#             message = 'ping'
#             f = open("hearbeat_server.txt","a")

#             conn1.send(bytes(message, 'utf-8'))
#             f.write(time.strftime("%X") + ": se envio ping a datanode1\n")
#             print("se envio ping a datanode1")

#             from_server = conn1.recv(4096)
#             f.write(time.strftime("%X") + ": se recibio respuesta de datanode1\n")
#             print("se recibio respuesta de datanode1")

#             conn2.send(bytes(message, 'utf-8'))
#             f.write(time.strftime("%X") + ": se envio ping a datanode2\n")
#             print("se envio ping a datanode2")

#             from_server = conn2.recv(4096)
#             f.write(time.strftime("%X") + ": se recibio respuesta de datanode2\n")
#             print("se recibio respuesta de datanode2")

#             conn3.send(bytes(message, 'utf-8'))
#             f.write(time.strftime("%X") + ": se envio ping a datanode3\n")
#             print("se envio ping a datanode3")

#             from_server = conn3.recv(4096)
#             f.write(time.strftime("%X") + ": se recibio respuesta de datanode3\n")
#             print("se recibio respuesta de datanode3")
#             f.close()
            
# f = open("headnode/registro_server.txt","w")
# f.write("id"+ "\t\t" + "ip_cliente" + "\t\t" + "datanode" + "\n")
# f.close()

# contador = 0
# while True:



#     thread = Datanodes()
#     thread.start()

#     IP_datanode1, _ = conn1.getpeername()
#     IP_datanode2, _ = conn2.getpeername()
#     IP_datanode3, _ = conn3.getpeername()

#     from_client = ''

#     while True:

#         data = conn.recv(4096)
#         if not data: break

#         from_client = data.decode("utf-8") 
#         print(from_client)

#         datanode_elegido = random.randint(1,3)
#         if datanode_elegido == 1:
#             print("se envio los datos a datanode 1")
#             conn1.send(bytes(from_client, 'utf-8'))
#             from_server = conn1.recv(4096)
#             ip_elegido = IP_datanode1
#         elif datanode_elegido == 2:
#             print("se envio los datos a datanode 1")
#             conn2.send(bytes(from_client, 'utf-8'))
#             from_server = conn2.recv(4096)
#             ip_elegido = IP_datanode2
#         else:
#             print("se envio los datos a datanode 1")
#             conn3.send(bytes(from_client, 'utf-8'))
#             from_server = conn3.recv(4096)
#             ip_elegido = IP_datanode3

#         print("se va a guardar a regisro cliente")
#         ip, _ = conn.getpeername()
#         file = open("headnode/registro_server.txt","a")
#         file.write(str(contador) + "\t\t" + ip + "\t\t" + str(datanode_elegido) + "\n")
#         file.close()
#         contador +=1
    
#         conn.send(bytes("datanode"+str(datanode_elegido), 'utf-8'))
    
#     conn.close()
#     print('client disconnected')


