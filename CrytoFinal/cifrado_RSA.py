#Bibliotecas python
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

#Bibliotecas propias
from file_admin import open_file,save_file

#Generar par de llaves
def generate_keys():
	key_size = 1024
	random_generator = Crypto.Random.new().read
	Key = RSA.generate(key_size, random_generator)
	private_key = Key.export_key('PEM')
	public_key = Key.publickey().export_key('PEM')
	private_key = binascii.hexlify(private_key)#.decode('utf-8')
	public_key = binascii.hexlify(public_key)#.decode('utf-8')
	#save_file("private_key",private_key,".pem")
	save_file("public_key",public_key,".pem")
	return private_key

#Cifrador RSA
def Cifrar_RSA(public_pem,plano):
	public_key = RSA.importKey(binascii.unhexlify(public_pem))
	cipher = PKCS1_OAEP.new(public_key)
	cifrado = cipher.encrypt(plano)
	return cifrado#.decode('utf-8')

#Decifrador RSA
def Descifrar_RSA(private_pem,cifrado):
	private_key = RSA.importKey(binascii.unhexlify(private_pem))
	cipher = PKCS1_OAEP.new(private_key)
	descifrado = cipher.decrypt(cifrado)
	return descifrado

#Pruebas
if __name__ == "__main__":

	#Generando llaves
    private_key = generate_keys()

    #Abriendo mensaje a cifrar
    plano = open_file()
    print(plano)

    #Abriendo llave publica
    public_key = open_file()
    #print(public_key)

    #Cifrado
    cifrado = Cifrar_RSA(public_key,plano)
    print(cifrado)
    print(len(cifrado))

    #Exportacion del mensaje cifrado
    save_file("CifradoRSA",cifrado,".txt")

    #Importacion del mensaje cifrado¿
    cifrado = open_file()
    print(cifrado)
    print(len(cifrado))

    #Abriendo llave privada
    #private_key = open_file()
    #print(private_key)

    #Descifrado
    descifrado = Descifrar_RSA(private_key,cifrado)
    print(descifrado)
    print(descifrado.decode('utf-8').replace('\r',''))