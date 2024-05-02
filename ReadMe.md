# Encrypt-Decrypt-Image-Server

Este es un proyecto simple que demuestra cómo encriptar una imagen, enviarla a un servidor y luego desencriptarla en el servidor utilizando el algoritmo de cifrado simétrico Fernet de la librería cryptography. Este README proporciona instrucciones detalladas sobre cómo configurar y ejecutar el servidor y el cliente.

## Requisitos

Python 3.x
Instalaciones de bibliotecas:
cryptography
Flask
requests

### Puedes instalar las bibliotecas necesarias ejecutando:

pip install cryptography Flask requests

## Configuración

### Servidor

Asegúrate de tener Python 3 instalado en tu sistema.

Clona este repositorio o descarga los archivos server.py y requirements.txt.

Instala las dependencias ejecutando:
pip install -r requirements.txt

### Cliente

Asegúrate de tener Python 3 instalado en tu sistema.

Clona este repositorio o descarga los archivos client.py y requirements.txt.

Instala las dependencias ejecutando:

pip install -r requirements.txt

## Uso

### Servidor

Ejecuta el archivo server.py:
python server.py

#### Esto iniciará el servidor en tu máquina local en el puerto 5000.

### Cliente

Ejecuta el archivo client.py:
python client.py

Este script encriptará una imagen local (imagen.jpeg por defecto), enviará la imagen encriptada al servidor y luego el servidor desencriptará la imagen y la guardará como imagen_desencriptada.jpg.

## Personalización

Rutas de archivo: Puedes cambiar las rutas de los archivos de imagen en el cliente (client.py) según tus necesidades.
URL del servidor: En el cliente (client.py), puedes cambiar la URL del servidor al que enviar la imagen encriptada.
