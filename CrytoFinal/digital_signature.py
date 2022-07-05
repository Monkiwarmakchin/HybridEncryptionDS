#Bibliotecas python
from os import urandom
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import binascii
import base64

#Bibliotecas propias
from file_admin import open_file,save_file
from cifrado_AES import Cifrar_AES,Descifrar_AES
from cifrado_RSA import generate_keys

#Generacion de la firma (en base 64)
def generate_sign(private_pem,plano):
	private_key = RSA.importKey(binascii.unhexlify(private_pem))
	hashed = SHA.new(plano) #hasheo
	signer = PKCS1_v1_5.new(private_key)
	signature = signer.sign(hashed)
	signature64 = base64.b64encode(signature)
	return signature64

#Comprovacion de la firma
def Verificacion(public_pem,plano,signature64):
	public_key = RSA.importKey(binascii.unhexlify(public_pem))
	hashed = SHA.new(plano)
	verifier = PKCS1_v1_5.new(public_key)
	if verifier.verify(hashed, base64.b64decode(signature64)):
		return True
	else:
		return False

#Pruebas
if __name__ == "__main__":

	#Generamos la llave AES
	secret_key = urandom(16)

    #Abriendo mensaje a firmar
	plano = open_file()
	print(plano)

    #Ciframos el texto plano con AES
	cifrado_AES = Cifrar_AES(secret_key,plano)
	print(cifrado_AES)

	#Generando llaves RSA
	private_key = generate_keys()

	#Generando firma
	signature = generate_sign(private_key, plano)
	print(signature)

	#Firmamos el texto cifrado exportandolo junto con su firma
	save_file("Firmado",cifrado_AES+str("&").encode('utf-8')+signature,".txt")

	#Abrimos el texto cuya firma vamos a verificar
	firmado = open_file().decode('utf-8')
	print(firmado)

	#Separamos la firma del propio texto cifrado
	signature = firmado.split("&")[1].encode('utf-8')
	print(signature)
	cifrado_AES = firmado.split("&")[0].encode('utf-8')
	print(cifrado_AES)

	#Desciframos el mensaje recibido
	plano = Descifrar_AES(secret_key,cifrado_AES)
	print(plano)

	#Abriendo llave publica
	public_key = open_file()

	#Verificanion de la firma
	if Verificacion(public_key,plano,signature):
		print("La firma digital ha sido verificada!")
	else:
		print("La firma digital no coincide!")