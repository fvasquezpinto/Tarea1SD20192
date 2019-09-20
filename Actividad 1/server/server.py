import socket
import time

f = open("log.txt","w")
f.write(time.strftime("%x"))
f.write("\t\t")
f.write(time.strftime("%X"))
f.write("\n\nIP\t\t\tMensaje\n")
f.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 5000))
serv.listen()

while True:

    conn, addr = serv.accept()
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


