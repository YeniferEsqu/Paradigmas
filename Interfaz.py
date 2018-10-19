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
			text2.delete('1.0', END)
			text3.delete('1.0', END)
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
	input = text3.get("1.0",END)
	if(input != ''):
		text3.delete('1.0', END)
	algoritmo = Algoritmo.Algoritmo()
	datos = text.get('1.0', END)
	if len(datos)> 1:
		algoritmo.CargarLista(datos)
	datos2 = text2.get('1.0', END)
	if len(datos2)> 1:
		algoritmo.evaluar(datos2)
		salida = algoritmo.ListaaEvaluar()
		#text3.delete(1.0,END)
		text3.insert(END,salida)
	else:
		print("Digite una hilera o escoja un archivo")

def guardarResultado():
	archivo = Archivo.Archivo()
	ruta =archivo.guardarArchivo()
	input = text3.get("1.0",END)
	if(ruta != None):
		archivo.guardarSalida(ruta,input)

def letrasGriegas(letra):
	if letra =="α": 
		text.insert(INSERT,letra)
	if letra =="β": 
		text.insert(INSERT,letra)
	if letra =="γ": 
		text.insert(INSERT,letra)
	if letra =="δ": 
		text.insert(INSERT,letra)
	if letra =="ε": 
		text.insert(INSERT,letra)
	if letra =="ζ": 
		text.insert(INSERT,letra)
	if letra =="η": 
		text.insert(INSERT,letra)
	if letra =="θ": 
		text.insert(INSERT,letra)
	if letra =="ι": 
		text.insert(INSERT,letra)
	if letra =="κ": 
		text.insert(INSERT,letra)
	if letra =="λ": 
		text.insert(INSERT,letra)
	if letra =="μ": 
		text.insert(INSERT,letra)
	if letra =="ν": 
		text.insert(INSERT,letra)
	if letra =="ξ": 
		text.insert(INSERT,letra)
	if letra =="ο": 
		text.insert(INSERT,letra)
	if letra =="π": 
		text.insert(INSERT,letra)
	if letra =="ρ": 
		text.insert(INSERT,letra)
	if letra =="σ": 
		text.insert(INSERT,letra)
	if letra =="τ": 
		text.insert(INSERT,letra)
	if letra =="υ": 
		text.insert(INSERT,letra)
	if letra =="φ": 
		text.insert(INSERT,letra)
	if letra =="χ": 
		text.insert(INSERT,letra)
	if letra =="ψ": 
		text.insert(INSERT,letra)
	if letra =="ω": 
		text.insert(INSERT,letra)

#ventana
root = Tk()
root.title('Algoritmos de Markov')
#tamaño de la ventana
root.geometry("1350x700+0+0")
#root.config(width = 1300, height = 650)
root.configure(background='SkyBlue2')

#titulo de la ventana
titulo = Label(root, text = "Algoritmos de Markov ", font=("Tahoma", 20,'bold'), background='SkyBlue2')
titulo.place(x = 490 , y = 5)

#titulos
label1 = Label(root, text = 'Algoritmo', font = ("Tahoma", 16 ),background='SkyBlue2')
label1.place(x = 10, y = 50)

label2 = Label( root, text = 'Hileras de Prueba', font = ("Tahoma", 16 ),background='SkyBlue2')
label2.place(x = 500, y = 50)

label3 = Label( root, text = 'Salida', font = ("Tahoma", 16 ),background='SkyBlue2')
label3.place(x = 10, y = 370)

label4 = Label( root, text = 'Alfabeto Griego', font = ("Tahoma", 16 ),background='SkyBlue2')
label4.place(x = 1050, y = 400)


#caja de texto para ubicar el algoritmo
text = Text(root, height=15, width=55, bg = 'white', font = ("Tahoma", 12 ))
text.place(x = 10, y = 80)

#ubicar las hileras que se le aplicaran las reglas
text2 = Text(root, height=15, width=55, bg = 'white', font = ("Tahoma", 12 ))
text2.place(x = 520, y = 80)

#ubicar el resultado de las hileras procesadas
text3 = Text( root, height=15, width=113, bg = 'white', font = ("Tahoma", 12 ))
text3.place(x = 10, y = 403)



#botones
boton1 = Button(root,text="Abrir Algoritmo" ,command =insertar, font=("Tahoma", 14),justify =CENTER, relief =RAISED, bd=3)
boton1.place(x = 1050, y = 100)

boton2 = Button(root,text="Cargar Archivo", command=insertarHileras,  font=("Tahoma", 14),justify =CENTER, relief =RAISED, bd=3)
boton2.place(x = 1050, y = 160)

boton3 = Button(root,text="Aplicar Reglas ", command=guardarAlgortimo, font=("Tahoma", 14),justify =CENTER, relief =RAISED, bd=3)
boton3.place(x = 1050, y = 220)

boton4 = Button(root,text="Guardar Salida", command=guardarResultado, font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
boton4.place(x = 1050, y = 280)

#alfabeto griego botones
alfabeto1 = Button(root,text="α", command=lambda:letrasGriegas("α"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto1.place(x = 1050, y = 450)

alfabeto2 = Button(root,text="β", command=lambda:letrasGriegas("β"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto2.place(x = 1080, y = 450)

alfabeto3 = Button(root,text="γ", command=lambda:letrasGriegas("γ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto3.place(x = 1110, y = 450)

alfabeto4 = Button(root,text="δ", command=lambda:letrasGriegas("δ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto4.place(x = 1139, y = 450)

alfabeto5 = Button(root,text="ε", command=lambda:letrasGriegas("ε"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto5.place(x = 1169, y = 450)

alfabeto6 = Button(root,text="ζ", command=lambda:letrasGriegas("ζ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto6.place(x = 1199, y = 450)

alfabeto7 = Button(root,text="η", command=lambda:letrasGriegas("η"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto7.place(x = 1050, y = 500)

alfabeto8 = Button(root,text="θ", command=lambda:letrasGriegas("θ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto8.place(x = 1080, y = 500)

alfabeto9 = Button(root,text="ι", command=lambda:letrasGriegas("ι"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto9.place(x = 1110, y = 500)

alfabeto10 = Button(root,text="κ", command=lambda:letrasGriegas("κ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto10.place(x = 1139, y = 500)

alfabeto11 = Button(root,text="λ", command=lambda:letrasGriegas("λ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto11.place(x = 1169, y = 500)

alfabeto12 = Button(root,text="μ", command=lambda:letrasGriegas("μ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto12.place(x = 1199, y = 500)

alfabeto13 = Button(root,text="ν", command=lambda:letrasGriegas("ν"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto13.place(x = 1050, y = 550)

alfabeto14 = Button(root,text="ξ", command=lambda:letrasGriegas("ξ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto14.place(x = 1080, y = 550)

alfabeto15 = Button(root,text="ο", command=lambda:letrasGriegas("ο"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto15.place(x = 1110, y = 550)

alfabeto16 = Button(root,text="π", command=lambda:letrasGriegas("π"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto16.place(x = 1139, y = 550)

alfabeto17 = Button(root,text="ρ", command=lambda:letrasGriegas("ρ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto17.place(x = 1169, y = 550)

alfabeto18 = Button(root,text="σ", command=lambda:letrasGriegas("σ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto18.place(x = 1199, y = 550)

alfabeto19 = Button(root,text="τ", command=lambda:letrasGriegas("τ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto19.place(x = 1050, y = 600)

alfabeto20 = Button(root,text="υ", command=lambda:letrasGriegas("υ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto20.place(x = 1080, y = 600)

alfabeto21 = Button(root,text="φ", command=lambda:letrasGriegas("φ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto21.place(x = 1110, y = 600)

alfabeto22 = Button(root,text="χ", command=lambda:letrasGriegas("χ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto22.place(x = 1139, y = 600)

alfabeto23 = Button(root,text="ψ", command=lambda:letrasGriegas("ψ"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto23.place(x = 1169, y = 600)

alfabeto24 = Button(root,text="ω", command=lambda:letrasGriegas("ω"), font=("Tahoma", 14 ), justify =CENTER, relief =RAISED, bd=3)
alfabeto24.place(x = 1199, y = 600)

text.delete('1.0', END)
text2.delete('1.0', END)
text3.delete('1.0', END)

root.mainloop()