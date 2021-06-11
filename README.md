# Práctica 2 AOS: Infraestructura y despliegue 👨‍🔧
Proyecto de la asignatura Arquitectura Orientada a Servicios (AOS) de la Universidad Politécnica de Madrid (UPM) que consiste en la contenerización y el despliegue de servicios de un taller

## Participantes 👨‍🎓

| Nombre | Email |
| ------ | ------ |
| Rubén Gago Navarro | r.gago@alumnos.upm.es |
| José María Baroja Zapata | jm.baroja@alumnos.upm.es |
| Ignacio García Pardina | ignacio.garcia.pardina@alumnos.upm.es |
| David Ramajo Fernández | d.ramajo@alumnos.upm.es |

## ENLACE DOCKER HUB:
En el siguiente enlace se puede encontrar la imagen de Docker asociada a nuestro servicio en la práctica 1 (facturación)
https://hub.docker.com/r/rugana90/aos-ss5

También hemos subido las de los demás equipos para la realización de esta práctica
- https://hub.docker.com/r/rugana90/aos-ss1
- https://hub.docker.com/r/rugana90/aos-ss2
- https://hub.docker.com/r/rugana90/aos-ss3
- https://hub.docker.com/r/rugana90/aos-ss4
- https://hub.docker.com/r/rugana90/aos-ss6

## Uso
Para correr el servidor ejecutar desde el directorio root:
```
pip3 install -r requirements.txt
python3 -m swagger_server
```

En el navegador escribimos:
```
http://localhost:8080/api/v1/factura
```

## Uso con Docker
Para correr en el servidor en un contenedor de Docker, ejecuta el siguiente comando en el directorio root:
```
# Construimos de la imagen
docker build -t 'NombreImagen':'TagImagen' .

# Creamos el contenedor
docker run -p 8080:8080 'NombreImagen':'TagImagen'
```
NombreImagen es el nombre que le queremos dar a nuestra imagen localmente. Por ejemplo: swagger_python

TagImagen es la tag que le queremos poner a nuestra imagen. Por ejemplo: 0.1

En el navegador escribimos:
```
http://localhost:8080/api/v1/factura
```

## Uso con imagen desde DockerHub:
Hacemos pull de la imagen desde el repositorio:
```
docker pull rugana90/aos-ss5:0.5
```
Creamos el contenedor
```
docker run -p 8080:8080 rugana90/aos-ss5:0.5
```
En el navegador escribimos:
```
http://localhost:8080/api/v1/factura
```
## Busquedas:
Para hacer una busqueda de un parametro utilizamos
```
http://localhost:8080/api/v1/factura/Parametro/ID
```
El valor Parametro puede ser cualquiera de las tres busquedas que se puede realizar con nuestro subsistema:
  - facturaId
  - userId
  - vehiculoId
ID es la busqueda que queremos hacer, por ejemplo:
```
http://localhost:8080/api/v1/factura/facturaId/1234
```
Nos mostrara la factura con ID igual a '1234'

## Docker-Compose:
Hemos creado dos Docker Compose para esta práctica.
En primer lugar hemos creado uno para realizar el despliegue de nuestro subsistema junto con una base de datos y un administrador como es PHPMyAdmin.
Para utilizarlo, lo levantamos con:
```
docker compose -f docker-compose-ss5.yml up
```
Podemos acceder a PHPMyAdmin a través de:
```
http://localhost:8080
```
Y al servicio a través de:
```
http://localhost:8081/api/v1/factura
```
Hemos creado dos tipos de usuarios:
 - Un usario root con credenciales: root / root123
 - Un usario taller con credenciales: user_taller / taller123
 - 
En segundo lugar hemos creado un Docker Compose para levantar todos los servicios a la vez. También cuenta con una base de datos y PHPMyAdmin.

Para utilizarlo, lo levantamos con:
```
docker compose -f docker-compose-taller.yml up
```
Podemos acceder a PHPMyAdmin con las credenciales previas a través de:
```
http://localhost:8080
```
Para acceder a cada servicio utilizaremos las siguientes direcciones:

Puerto 8080 (PHPMyAdmin):
    - http://localhost:8080/

Puerto 8081 (SS1 - Clientes):
    - http://localhost:8081/clientes

Puerto 8082 (SS2 - Vehículos):
    - http://localhost:8082/api/v1/vehiculo

Puerto 8083 (SS3 - Trabajos):
    - http://localhost:8083/api/v1/trabajo

Puerto 8084 (SS4 - Notificaciones):
    - http://localhost:8084/AOS4/swagger-ui/

Puerto 8085 (SS5 - Facturas):
    - http://localhost:8085/api/v1/factura

Puerto 8086 (SS6 - Recambios):
    - http://localhost:8086/api/v1/recambios
