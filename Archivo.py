import easygui as eg

class Archivo:
	def cargarAlgoritmo(self,ruta):
		archivo = open(ruta, "r")
		linea= archivo.read()
		return linea
		
	
	def abrirArchivo(self):
		extension = ["*.txt","*.txt"]
		abrir = eg.fileopenbox(msg="Abrir archivo",title="Abrir Algoritmo",default='',filetypes=extension)
		return abrir

		
		
		
		
		
		
		
