import easygui as eg
import io

class Archivo:
#Para cargar el archivo 
	def cargarAlgoritmo(self,ruta):
		archivo = open(ruta, "r",encoding="utf-8")
		linea= archivo.read()
		return linea
		
#Para escoger el archivo que se desea cargar
	def abrirArchivo(self):
		extension = ['*.txt']
		abrir = eg.fileopenbox(msg="Abrir archivo",title="Abrir Algoritmo",filetypes=extension)
		return abrir
		
#Para guardar el archivo 
	def guardarArchivo(self):
		extension = ['*.txt']
		guardar = eg.filesavebox(msg="Guardar archivo",title="Guardar Salida",filetypes=extension)
		return guardar
	
#Para guardar el resultado de aplicar las reglas
	def guardarSalida(self,ruta, hilera):
		archivo = open(ruta, "w",encoding="utf-8")
		archivo.write(hilera) 
		archivo.close() 