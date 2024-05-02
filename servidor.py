from cryptography.fernet import Fernet
from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route('/decrypt_image', methods=['POST'])
def decrypt_image():
    # Obtener la imagen encriptada y la clave del cliente
    encrypted_image = request.files['image'].read()
    key = request.form['key'].encode('utf-8')  # Codificar la clave de cadena a bytes

    # Crear un objeto Fernet con la clave
    fernet = Fernet(key)

    # Desencriptar la imagen
    decrypted_image = fernet.decrypt(encrypted_image)

    # Guardar la imagen desencriptada en un archivo
    with open('imagen_desencriptada.jpg', 'wb') as file:
        file.write(decrypted_image)

    # Guardar la imagen desencriptada en un búfer de memoria
    image_buffer = io.BytesIO(decrypted_image)

    # Enviar la imagen desencriptada de vuelta al cliente
    return send_file(image_buffer, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')