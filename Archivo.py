#-------------------------------------------------------------------------------------
#Proyecto #1
#Integrantes: 
	#Kimberly Esquivel Reyes
	#Yenifer Esquivel Reyes
	#Juan Pablo Campos León
#Curso
	#Paradigmas de Programacion
#Ciclo Lectivo 2018
#Descripcion del Proyecto
	#Programa desarollado en Python, utilizando la interfaz grafica Tkinter.
	#El programa permite abrir y editar y guardar algoritmos, para luego
	#ser ejecutados con hileras de prueba. Las hileras se pueden escribir en
	#la caja de texto, o bien, cargarlas desde un archivo de texto. 
	#Una vez que se ejecuten las reglas para cada hilera, estas se mostraran
	#en la caja de texto de Salida.
	#Para guardar el algoritmo se debe poner la extension .txt para poder abrirlo
	#con cualquier editor de texto.
#-------------------------------------------------------------------------------------

#Esta clase es la que se encarga de abrir el archivo y cargarlo en la caja de texto
#asi como guardarlo en la carpeta que se desee. Utilizamos el modulo easygui para 
#las ventanas en las que se eligen y se guardan los algoritmos.


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
		guardar = eg.filesavebox(msg="Guardar archivo",title="Guardar Algoritmo",filetypes=extension)
		return guardar
	
#Para guardar el algoritmo si fue editado
	def guardarSalida(self,ruta, hilera):
		archivo = open(ruta, "w",encoding="utf-8")
		archivo.write(hilera) 
		archivo.close() 