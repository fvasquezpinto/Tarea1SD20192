import socket
import time
import threading

f = open("hearbeat_server.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))
f.write("\n\nIP\t\t\tMensaje\n")


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 4000))
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

class Datanodes(threading.Thread):
    def run(self, conn1):
        while True:
            time.sleep(5)
            message = 'estan vivos'
            #luego agregar los demas ip
            #multicast_group = (IP_datanode1, 10000)
            f = open("hearbeat_server.txt","a")
            f.write("se envio el mensaje a datanode1")
            print("se envio el mensaje a datanode1")
            f.close()
            conn1.send(bytes(message, 'utf-8'))


while True:

    

    conn, addr = serv.accept()
    conn1, addr1 = datanode1.accept()
    conn2, addr2 = datanode2.accept()
    conn3, addr3 = datanode3.accept()

    thread = Datanodes()
    thread.start(conn1)

    IP_datanode1 = conn1.getpeername()

    from_client = ''

    while True:

        data = conn.recv(4096)
        if not data: break

        from_client = data.decode("utf-8") 
        print(from_client)
        ip, _ = conn.getpeername()

        f = open("log.txt","a")
        f.write(ip + "\t\t" + from_client + "\n")
        f.close()

        conn.send(bytes("Se ha recibido su peticion '" + from_client + "'", 'utf-8'))
    
    conn.close()
    print('client disconnected')


