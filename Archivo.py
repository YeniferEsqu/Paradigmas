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