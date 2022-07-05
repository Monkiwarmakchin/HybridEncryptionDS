#Bibliotecas python
import base64

#Bibliotecas propias
from file_admin import open_file,save_file
from cifrado_AES import Descifrar_AES
from cifrado_RSA import generate_keys,Descifrar_RSA
from digital_signature import Verificacion

#MAIN
#Generamos las llaves RSA
print("\n***Envie su llave publica a quien le enviara el mensaje***\n")
private_key = generate_keys()

#Obtenemos texto a descifrar
print("***Seleccione el texto a descifrar***\n")
CyFyK = open_file().decode('utf-8')

#Separamos la firma del propio texto cifrado
cifrado_AES = CyFyK.split("&")[0].encode('utf-8')
signature = CyFyK.split("&")[1].encode('utf-8')
secret_64 = CyFyK.split("&")[2].encode('utf-8')

#Desciframos la llave secreta
secret_RSA = base64.b64decode(secret_64)
secret_key = Descifrar_RSA(private_key,secret_RSA)

#Obtenemos la llave publica que nos pase nuestro receptor
print("***Seleccione la llave publica que le ha mandado su emisor***\n")
public_key = open_file()

#Desciframos el mensaje recibido
descifrado = Descifrar_AES(secret_key,cifrado_AES)
print("!!!Su texto ha sido descifrado!!!\n")

#Verificanion de la firma
if Verificacion(public_key,descifrado,signature):
	print("!!!La firma digital ha sido verificada!!!")
else:
	print("***Pero la firma digital no coincide***")

#Guardamos el texto descifrado
plano = descifrado.decode('utf-8').replace('\r','')
save_file("Descifrado",plano.encode('utf-8'),".txt")