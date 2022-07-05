#Bibliotecas python
import tkinter as tk
from tkinter import filedialog

#Abrir archivo TK
def open_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return get_content(file_path)

#Obtener contenido del archivo
def get_content(path):
    file = open(path,"rb")
    return file.read()

#Guardar el archivo (sobrescribir)
def save_file(nombre,contenido,extension):
    f = open(save_path(nombre,extension),"wb")
    f.write(contenido)
    f.close()
    
#Direccion de guardado
def save_path(nombre,extension):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=extension,initialfile=nombre)
    return file_path

#Pruebas
if __name__ == "__main__":

	#Guardar
	contenido = "Hola Mundo"
	save_file("Prueba",contenido,".txt")
	print(open_file())

	#Añadir
	añadido = " Cruel"
	add_to_file("Prueba",añadido,".txt")
	print(open_file())
