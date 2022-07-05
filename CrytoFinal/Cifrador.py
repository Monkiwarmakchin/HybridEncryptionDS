#Bibliotecas python
from os import urandom
import base64

#Bibliotecas propias
from file_admin import open_file,save_file
from cifrado_AES import Cifrar_AES
from cifrado_RSA import generate_keys,Cifrar_RSA
from digital_signature import generate_sign

#MAIN
#Generamos la llave AES aleatoriamente
secret_key = urandom(16)

#Obtenemos texto a cifrar
print("\n***Seleccione el texto a cifrar***\n")
plano = open_file()

#Ciframos el texto plano con AES
cifrado_AES = Cifrar_AES(secret_key,plano)

#Obtenemos la llave publica que nos pase nuestro receptor
print("***Seleccione la llave publica que le ha mandado su remitente***\n")
public_key = open_file()

#Ciframos la llave secreta con RSA
secret_RSA = Cifrar_RSA(public_key,secret_key)
secret_64 = base64.b64encode(secret_RSA)

#Generamos las llaves RSA
print("***Envie su llave publica al receptor de su mensaje***\n")
private_key = generate_keys()

#Generamos nuestra firma
signature = generate_sign(private_key, plano)

#Firmamos el texto cifrado exportandolo junto con su firma y agregamos la llave AES cifrada tambien
print("!!!Su texto ha sido cifrado. Envielo a su remitente!!!")
save_file("C&F&K",cifrado_AES+str("&").encode('utf-8')+signature+str("&").encode('utf-8')+secret_64,".txt")
