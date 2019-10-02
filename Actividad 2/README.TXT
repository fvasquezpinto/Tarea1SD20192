Notas importantes de la Actividad 2

1) La ruta del archivo registro_server.txt es: /Tarea1SD20192/Actividad\ 2/headnode/registro_server.txt

2) La ruta del archivo registro_cliente.txt es: /Tarea1SD20192/Actividad\ 2/client/registro_cliente.txt

2) La ruta del archivo hearbeat_server.txt es: /Tarea1SD20192/Actividad\ 2/hearbeat_server.txt

3) Al ejecutar los comandos "docker-compose build" seguido de "docker-compose up" (en la ruta /Tarea1SD20192/Actividad\ 2/) se levantará tanto el headnode como el cliente y los datanodes; el cliente enviará 20 datos al servidor de manera automatica. Estos mensajes pasarán al headnode el cual lo repartirá aleatoriamente a los datanodes (quedando la data en datanodeX/data.txt donde X es el numero del datanode elegido)
