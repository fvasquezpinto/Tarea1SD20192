import socket
import time
import threading
import struct

print("Server iniciado")
f = open("hearbeat_server.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))
f.write("\n\nIP\t\t\tMensaje\n")


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 5000))
serv.listen()

datanode1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
datanode1.bind(('0.0.0.0', 6000))
datanode1.listen()


datanode2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
datanode2.bind(('0.0.0.0', 7000))
datanode2.listen()

datanode3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
datanode3.bind(('0.0.0.0', 8000))
datanode3.listen()

f.close()

message = b'very important data'
multicast_group = ('224.10.10.10', 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

class Datanodes(threading.Thread):
    def run(self):

        while True:

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

        time.sleep(5)

'''
            message = 'estan vivos'
            #luego agregar los demas ip
            #multicast_group = (IP_datanode1, 10000)
            f = open("hearbeat_server.txt","a")
            f.write("se envio el mensaje a datanode1\n")
            print("se envio el mensaje a datanode1")
            f.close()
            
            time.sleep(1)
            conn1.send(bytes(message, 'utf-8'))
'''

while True:

    conn, addr = serv.accept()
    
    conn1, addr1 = datanode1.accept()
    conn2, addr2 = datanode2.accept()
    conn3, addr3 = datanode3.accept()

    thread = Datanodes()
    thread.start()

    IP_datanode1, _ = conn1.getpeername()
    IP_datanode2, _ = conn2.getpeername()
    IP_datanode3, _ = conn3.getpeername()

    from_client = ''

    while True:

        data = conn.recv(4096)
        if not data: break

        from_client = data.decode("utf-8") 
        print(from_client)
        ip, _ = conn.getpeername()

        f = open("hearbeat_server.txt","a")
        f.write(ip + "\t\t" + from_client + "\n")
        f.close()
    
        conn.send(bytes("Se ha recibido su peticion '" + from_client + "'", 'utf-8'))
    
    conn.close()
    print('client disconnected')


