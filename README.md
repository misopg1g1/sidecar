# Guía para ejecutar el sidecar

## Requisitos previos

Asegúrate de tener los siguientes requisitos previos instalados en tu sistema:

- Docker
- Docker Compose (solo para ejecutar con Docker Compose)
- Python 3.9 (solo para ejecución local)

## Configuración

Antes de ejecutar la aplicación, asegúrate de realizar la siguiente configuración:

1. Abre el archivo `docker-compose.yml` y configura las siguientes variables de entorno según tus necesidades:

    - `ENCRYPTION_KEY_SECRET`: La clave de cifrado secreta para tu aplicación.
    - `MICRO_SERVICE_URL`: La URL del microservicio al que la aplicación debe conectarse.

2. Si tienes dependencias adicionales, agrégalas al archivo `requirements.txt`.

## Ejecución con Docker Compose

Sigue estos pasos para ejecutar la aplicación utilizando Docker Compose:

1. Abre una terminal y navega hasta el directorio que contiene el archivo `docker-compose.yml`.

2. Ejecuta el siguiente comando para construir la imagen y ejecutar los contenedores:

```
  docker-compose up
```

3. Docker Compose construirá la imagen de la aplicación y ejecutará el contenedor del servicio. Podrás acceder a la
   aplicación en `http://localhost:3001`.

4. Si deseas detener la aplicación, presiona `Ctrl + C` en la terminal y ejecuta el siguiente comando:

## Ejecución local

Sigue estos pasos para ejecutar la aplicación de forma local:

1. Abre una terminal y navega hasta el directorio que contiene el archivo `Dockerfile`.

2. Ejecuta el siguiente comando para instalar las dependencias de Python:

```shell
 pip install -r requirements.txt
```

3. Una vez instaladas las dependencias, ejecuta el siguiente comando para iniciar la aplicación:

```shell
ENCRYPTION_KEY_SECRET=... MICRO_SERVICE_URL=... python main.py
```

4. La aplicación ahora estará en ejecución y podrás acceder a ella en `http://localhost:3001`.

5. Para detener la aplicación, ve a la terminal y presiona `Ctrl + C`.
