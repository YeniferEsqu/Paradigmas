from tkinter import *
import Archivo


def insertar():
	archivo = Archivo.Archivo()
	ruta =archivo.abrirArchivo()
	if(ruta != None):
		carga = archivo.cargarAlgoritmo(ruta)
		text.insert(INSERT,carga)
		
		
#ventana
root = Tk()
root.title('Algoritmos de Markov')
#tamaño de la ventana
root.config(width = 900, height = 500)
root.configure(background='SkyBlue2')

#titulo de la ventana
titulo = Label(root, text = "Algoritmos de Markov ",  font=("Arial", 20,'bold'), background='SkyBlue2')
titulo.place(x = 310 , y = 10)


#botones
boton1 = Button(root,text="Abrir Algoritmo" ,command =insertar, font=("Arial", 14),justify =CENTER, relief =RAISED)
boton1.place(x = 60, y = 60)

boton2 = Button(root,text="Cargar Archivo",  font=("Arial", 14),justify =CENTER, relief =RAISED)
boton2.place(x = 220, y = 60)

boton3 = Button(root,text="Run", font=("Arial", 14),justify =CENTER, relief =RAISED)
boton3.place(x = 530, y = 60)

boton4 = Button(root,text="Guardar Salida", font=("Arial", 14 ), justify =CENTER, relief =RAISED)
boton4.place(x = 610, y = 60)

#caja de texto

text = Text(root, height=20, width=50, bg = 'gray64')
text.place(x = 20, y = 110)


text2 = Label(root,height=21, width=57, bg = 'gray64')
text2.place(x = 450, y = 110)

root.mainloop()