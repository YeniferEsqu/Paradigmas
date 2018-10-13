from tkinter import *
import Archivo
import Algoritmo

#Insertar el algoritmo el la caja de texto
def insertar():
	archivo = Archivo.Archivo()
	ruta =archivo.abrirArchivo()
	input = text.get("1.0",END)
	if(ruta != None):
		if(input != ''):
			text.delete('1.0', END)
		carga = archivo.cargarAlgoritmo(ruta)
		text.insert(INSERT,carga)
	else:
		print("no escogio ruta")
#Insertar las hileras de prueba
def insertarHileras():
	archivo = Archivo.Archivo()
	ruta =archivo.abrirArchivo()
	input = text2.get("1.0",END)
	if(ruta != None):
		if(input != ''):
			text2.delete('1.0', END)
		carga = archivo.cargarAlgoritmo(ruta)
		text2.insert(INSERT,carga)

#guarda lo que tiene algoritmo y lo pasa a evaluar
def guardarAlgortimo():
	algoritmo = Algoritmo.Algoritmo()
	datos = text.get('1.0', END)
	algoritmo.CargarLista(datos)

def regla():
	algoritmo = Algoritmo.Algoritmo()
	algoritmo.ReglaTerminal()

#ventana
root = Tk()
root.title('Algoritmos de Markov')
#tamaño de la ventana
root.config(width = 1300, height = 650)
root.configure(background='SkyBlue2')

#titulo de la ventana
titulo = Label(root, text = "Algoritmos de Markov ",  font=("Arial", 20,'bold'), background='SkyBlue2')
titulo.place(x = 510 , y = 10)

#botones
boton1 = Button(root,text="Abrir Algoritmo" ,command =insertar, font=("Arial", 14),justify =CENTER, relief =RAISED)
boton1.place(x = 260, y = 100)

boton2 = Button(root,text="Cargar Archivo", command=insertarHileras,  font=("Arial", 14),justify =CENTER, relief =RAISED)
boton2.place(x = 630, y = 100)

boton3 = Button(root,text="RUN", command=guardarAlgortimo, font=("Arial", 14),justify =CENTER, relief =RAISED)
boton3.place(x = 780, y = 100)

boton4 = Button(root,text="Guardar Salida", command=regla, font=("Arial", 14 ), justify =CENTER, relief =RAISED)
boton4.place(x = 1100, y = 100)


#titulos
label1 = Label(root, text = 'Algoritmo', font = ("Arial", 16 ))
label1.place(x = 20, y = 110)

label2 = Label( root, text = 'Hileras de Prueba', font = ("Arial", 16 ))
label2.place(x = 440, y = 110)

label3 = Label( root, text = 'Resultado', font = ("Arial", 16 ))
label3.place(x = 870, y = 110)

#caja de texto para ubicar el algoritmo
text = Text(root, height=27, width=50, bg = 'gray64')
text.place(x = 20, y = 160)

#ubicar las hileras que se le aplicaran las reglas
text2 = Text( root, height=27, width=50, bg = 'gray64')
text2.place(x = 440, y = 160)

#ubicar el resultado de las hileras procesadas
text3 = Text( root, height=27, width=50, bg = 'gray64')
text3.place(x = 860, y = 160)
root.mainloop()