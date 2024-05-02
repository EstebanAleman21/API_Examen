from cryptography.fernet import Fernet
import requests
import base64

def encrypt_image(image_path, key):
    # Generar una clave de encriptación si no se proporciona
    if not key:
        key = Fernet.generate_key()

    # Crear un objeto Fernet con la clave
    fernet = Fernet(key)

    # Leer la imagen en bytes
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Encriptar la imagen
    encrypted_image = fernet.encrypt(image_data)

    # Imprimir la imagen encriptada en formato base64
    print("Imagen encriptada (Base64):")
    print(base64.b64encode(encrypted_image).decode('utf-8'))

    return encrypted_image, key

def send_encrypted_image(encrypted_image, key, server_url):
    # Enviar la imagen encriptada y la clave al servidor
    files = {'image': encrypted_image}
    data = {'key': key.decode('utf-8')}  # Decodificar la clave de bytes a cadena
    response = requests.post(server_url, files=files, data=data)

    if response.status_code == 200:
        print("La imagen se envió y desencriptó correctamente en el servidor.")
    else:
        print("Error al enviar la imagen al servidor.")

if __name__ == "__main__":
    image_path = 'imagen.jpeg'  # Ruta de la imagen local
    server_url = 'http://127.0.0.1:5000/decrypt_image'  # URL del servidor

    # Encriptar la imagen y obtener la clave
    encrypted_image, key = encrypt_image(image_path, None)

    # Enviar la imagen encriptada y la clave al servidor
    send_encrypted_image(encrypted_image, key, server_url)