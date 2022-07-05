#Bibliotecas python
from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64

#Bibliotecas propias
from file_admin import open_file,save_file

#Cifrador AES (en base 64)
def Cifrar_AES(secret_key,plano):
    plano_bytes = plano#.encode('utf-8')
    iv = urandom(16)
    padded_bytes = pad(plano_bytes,AES.block_size)
    cipher = AES.new(secret_key,AES.MODE_CBC,iv)
    cifrado = iv+cipher.encrypt(padded_bytes)
    cifrado64 = base64.b64encode(cifrado)
    return cifrado64#.decode('utf-8')

#Descifrador AES
def Descifrar_AES(secret_key,cifrado64):
	cifrado = base64.b64decode(cifrado64)
	iv = cifrado[:AES.block_size]
	cipher = AES.new(secret_key,AES.MODE_CBC,iv)
	padded_bytes = cipher.decrypt(cifrado[AES.block_size:])
	plano_bytes = unpad(padded_bytes, AES.block_size)
	return plano_bytes#.decode('utf-8')

#Pruebas
if __name__ == "__main__":

	#Generacion de la llave
    secret_key = urandom(16)

    #Abriendo mensaje a cifrar
    plano = open_file()
    print(plano)
    #print(len(plano))

    #Cifrado
    cifrado = Cifrar_AES(secret_key,plano)
    print(cifrado)
    #print(len(cifrado))

    #Exportacion del mensaje cifrado
    save_file("CifradoAES",cifrado,".txt")

    #Importacion del mensaje cifrado
    cifrado = open_file()

    #Descifrado
    print(cifrado)
    #print(len(cifrado))
    descifrado = Descifrar_AES(secret_key,cifrado)
    print(descifrado)
    print(descifrado.decode('utf-8').replace('\r',''))
