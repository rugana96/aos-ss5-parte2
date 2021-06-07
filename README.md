# Imagen de Docker Subsistema 5
Repositorio con la imagen del subsistema 5 de la asignatura de AOS encargado del servicio de facturación de un taller.

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
