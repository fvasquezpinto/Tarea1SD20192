Notas importantes de la Actividad 1

1) La ruta del archivo log.txt es: /Tarea1SD20192/Actividad\ 1/log.txt

2) La ruta del archivo respuestas.txt es: /Tarea1SD20192/Actividad\ 1/respuestas.txt

3) Al ejecutar los comandos "docker-compose build" seguido de "docker-compose up" (en la ruta /Tarea1SD20192/Actividad\ 1/) se levantará tanto el servidor como el cliente; el cliente enviará un saludo al server

4) Para enviar una petición personalizada al servidor se debe ejecutar "docker-compose build" seguido de "docker-compose run client" (en la ruta /Tarea1SD20192/Actividad\ 1/), vale decir, sin hacer docker-compose up antes de docker-compose run client para que no esté levantado el cliente antes de intentar levantarlo de nuevo.