# -*- coding: utf-8 -*-
import re
class Algoritmo:
#variables globales
	global lista1 #reglas busqueda
	global lista2 #reglas de sustitucion
	global lista3 #simbolos
	global lista4 #variables
	global lista5 #marcadores
	global caracteresEspeciales
	global listadef
	global variablesUsadas  #lista auxiliar para almacenar las variable que utiliza una regla y su posicion en dicha cadena
	global etiquetaInicio
	global hileraSustituida
	global terminal 
	global sustitucion
	global reglaAplicada
	global aplico
	global Salida

	Salida = ""
	caracteresEspeciales = ["(",")","+",".","$","*","?","[","]","{","}","|"]
	etiquetaInicio = None
	variablesUsadas=[]
	
	

	#lista1=["P1: βX","P2: Xβ","P3: X"]
	#lista2=["Xβ (P1)","Λ.","βX (P1)"]
	#lista3=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
	#lista4=["X"]
	#lista5=["β"]
	#lista1=["(())","())","(()","()","(α","α)",")","(","αα","α" ]
	#lista2=["()","α)","(α","VALIDO.","α","α","α","α","α","INVALIDO."]
	#lista3=["(",")"]
	#lista4=["I","N","V","A","L","I","D","O"]
	#lista5=["α"]
	listadef=[]
	terminal = False
	sustitucion=""
	aplico =False
	


#devuelve posicion de regla terminal	
	def ReglaTerminal(self):
		global lista2
		for x in lista2:
			if(x.find(".")== 1):
				terminal2 = x
				return terminal2
				
	def CargarLista(self, algoritmo):
		global lista1
		global lista2
		global lista3
		global lista4
		global lista5
		global Salida
		lista1=[]
		lista2=[]
		lista3=[]
		lista4=[]
		lista5=[]
		lista=[]
		Salida=""
		carga = algoritmo
		if re.match("\ufeff",carga) != None:
			carga = re.sub("\ufeff","",carga,1)

#guardar cada línea en carga excepto campos vacios y comentarios
		for line in carga.splitlines():			
			if(len(line) > 1 and line[0] is not ' '):
				if(line[0] != '%'):
				    lista.append(line)

#saber el tamaño de la lista
		list_len = len(lista)
#Listas para guardar las reglas, variables, simbolos, marcadores
		
		for x in lista:
			caracter = x
			#car = caracter[0]
			
#si tiene symbols en la linea, lo guarda en la lista3
			if(caracter.find("#symbols") is not -1):
				simb = x.split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista3.append(palabra[y])
				
#si tiene vars en la linea, lo guarda en la lista4
			elif(caracter.find("#vars") is not -1):
				#print("Entro3")
				simb = x.split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista4.append(palabra[y])
				
#si tiene markers en la linea, lo guarda en la lista5
			elif(caracter.find("#markers") is not -1):
				#print("Entro5")
				simb = x.split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista5.append(palabra[y])
			
#sino las reglas las guarda en lista2 y lista1
			else:
				simb = x.split("->")
				lista1.append(simb[0])
				lista2.append(simb[1])
	
	#metodo para agarrar lo del campo de texto y comprobar que esta en el alfabeto
	def estaenlalista(self, cadena):
		global lista3
		esta = 0
		hil= cadena
		res = 0
		tamano = len(cadena)
		for x in range(0,tamano):
			if hil[x] in lista3:
				esta = esta + 1

		if(esta == tamano):
			res = 1
		
		return res
		
#verifica que las hileras coincidan con los simbolos
	def evaluar(self,hilera):
		cadena = hilera
		lista=[]
		global listadef
		listadef = []
		num=0
		#inserta todo lo que tiene el campo de texto de las hileras en la lista
		for line in cadena.splitlines():			
			if(len(line) > 1 and line[0] is not ' '):
					lista.append(line)
		#print(lista)
		
		#si cada hilera esta en la lista la inserta, sino no
		for x in lista:
			if (self.estaenlalista(x) == 1):
				listadef.append(x)
				num = num + 1
		return listadef

	#metodo que busca si existe una etiqueta 
	def buscaEtiqueta(self,regla):
		etiqueta = re.match("(.+?)+:" , regla)
		if (etiqueta != None):
			etiqueta = etiqueta.group()
			etiqueta = re.sub(r":","",etiqueta)
			return etiqueta
		else:
			return None
	
#metodo que busca si existe una etiqueta al final de una regla 
# y la asigna a su correspondiente variable global
	def buscaEtiquetaInicio(self,reglaSustitucion):
		global etiquetaInicio
		etiqueta = re.search("([(].+?[)])$" , reglaSustitucion)
		if etiqueta != None:
			etiqueta = etiqueta.group()
			etiqueta = etiqueta[1:]
			etiqueta = etiqueta[:len(etiqueta)-1]
			etiquetaInicio = etiqueta
			return etiqueta
		else:
			etiquetaInicio = None
			return None

#metodo que convierte una regla de busqueda en un patron de busqueda de expresiones regulares
	def convertirPatron(self,etiqueta,regla):
		global variablesUsadas
		global caracteresEspeciales
		variablesUsadas =[]
		if (etiqueta != None):
			regla = re.sub(etiqueta + ":","",regla,1)

		tam = len(regla)
		patron = ""
		cont = 0
		for x in range(0,tam):
			if regla[x] == ' ': #si es un espacio no hace nada
				continue
			elif regla[x] == 'Λ':   #si es un Λ que simboliza inicio de cadena agrega el simbolo para que compare con el inicio
				patron = patron + "^"  #agrega el simbolo para que compare con el inicio
				cont = cont + 1
			elif regla[x] in lista3:  #si esta en la lista de simbolos
				patron = patron +"[" + regla[x] +"]"
				cont = cont + 1
			elif  regla[x] in lista4:  #si esta en la lista de variables agrega dicha variable a la lista auxiliar 
				variablesUsadas.append(regla[x])
				variablesUsadas.append(cont)
				variablesUsadas.append("")
				patron = patron +"."
				cont = cont + 1
			elif regla[x] in lista5:   #si esta en la lista de marcadores
				patron = patron +"[" + regla[x] +"]"
				cont = cont + 1
			else:
				return None
		return patron

#recibe un patron y una hilera y determina si existe alguna coincidencia
	def buscarPatrones(self,patron,hilera):
		global variablesUsadas
		global caracteresEspeciales
		if patron == "^":
			return patron
		patronEncontrado = re.search(patron,hilera)
		if patronEncontrado != None:
			patronEncontrado=patronEncontrado.group()
			while True:
				aux = patronEncontrado
				patronEncontrado = patronEncontrado[1:]
				patronEncontrado = re.search(patron,patronEncontrado)
				if( patronEncontrado == None):
					patronEncontrado = aux
					break
				else:
					patronEncontrado = patronEncontrado.group()
			tam = len(variablesUsadas)
			for i in range(0,tam,3):
				variablesUsadas[i+2] = patronEncontrado[variablesUsadas[i+1]]
			
			for i in range(0,tam,3):
				for j in range(0,tam,3):
					if i != j:
						if variablesUsadas[i] == variablesUsadas[j]:
							if variablesUsadas[i + 2] != variablesUsadas[j + 2]:
								return None
						else:
							if variablesUsadas[i + 2] == variablesUsadas[j + 2]:
								return None
			tam1 = len(patronEncontrado)
			patronRetorno=""
			for k in range(0,tam1):
				if patronEncontrado[k] in caracteresEspeciales:
					patronRetorno = patronRetorno + "["+patronEncontrado[k]+"]"
				else:
					patronRetorno = patronRetorno + patronEncontrado[k]

			return patronRetorno
		else:
			return None

#recibe el patron encontrado en el metodo anterior, la regla de sustitucion correspondiente 
#y la hilera a la que se va a aplicar. Devuelve la hilera con la sustitucion hecha
	def sustituirRegla(self,patronEncontrado,reglaSustitucion,hilera):
		global terminal
		global variablesUsadas
		global lista3
		global lista4
		global lista5
		etiqueta = self.buscaEtiquetaInicio(reglaSustitucion)
		if etiqueta != None:
			etiqueta = "[(]"+etiqueta+"[)]"
			reglaSustitucion = re.sub(etiqueta,"",reglaSustitucion)
		
		
		sustitucion = ""
		tam = len(reglaSustitucion)
		tam1 = len(variablesUsadas)

		for i in range(0,tam):
			bandera = True
			for j in range(0,tam1,3):
				if variablesUsadas[j] == reglaSustitucion[i]:
					sustitucion = sustitucion + variablesUsadas[j+2]
					bandera = False
					break
			if bandera:
				if reglaSustitucion[i] in lista3 or reglaSustitucion[i] in lista4  or reglaSustitucion[i] in lista5 or reglaSustitucion[i] == '.'or reglaSustitucion[i] == 'Λ' or reglaSustitucion[i] == ' ':
						if reglaSustitucion[i] != '.' and reglaSustitucion[i] != 'Λ' and reglaSustitucion[i] != ' ':
							sustitucion = sustitucion + reglaSustitucion[i]
						if reglaSustitucion[i] == '.':
							terminal = True
				else:
					return None
		
		if patronEncontrado == "^":
			return sustitucion + hilera
		if patronEncontrado in caracteresEspeciales:
			patronEncontrado = "["+patronEncontrado+"]"
		return re.sub(patronEncontrado,sustitucion,hilera,1)

#aplica las reglas 1 vez 
	def SustituirCadena(self,hilera):
		tam = len(lista1)
		global aplico
		restart = True
		global terminal 
		global sustitucion
		global etiquetaInicio
		global Salida
		for i in range(0,tam):
			etiqueta = self.buscaEtiqueta(lista1[i])
			if etiquetaInicio != None:
				if etiqueta == etiquetaInicio:
					etiquetaInicio = None
				else:
					continue
			patron = self.convertirPatron(etiqueta,lista1[i])
			patronEncontrado = self.buscarPatrones(patron,hilera)
			if patronEncontrado != None:
				print("Regla Sustitucion: ")
				print(lista2[i])
				print("Hilera Resultante: ")
				sustitucion = self.sustituirRegla(patronEncontrado,lista2[i],hilera)
				
				#print(sustitucion)
				#print("ReglaTerminal")
				#print(self.ReglaTerminal())
				aplico = True
				#if(self.ReglaTerminal() == lista2[i]):
					#terminal = True
				break
		#print("sustitucion  "+sustitucion)
		if sustitucion == None:
			Salida = Salida + "HA OCURRIDO UN ERROR" + "\n"
			terminal = True
		else:
			Salida = Salida + sustitucion + "\n"
		return sustitucion
		
				
#agarra lo que tiene sustitucion y sigue aplicando regla si no aplica regla terminal
	def recorrerHilera(self,hilera):
		global terminal 
		sustitucion = self.SustituirCadena(hilera)
#si no aplico regla terminal que siga evaluando
		while(terminal is False or aplico is False):
			sustitucion =self.SustituirCadena(sustitucion)
			

#la primera vez que entra cambia la hilera, luego agarra lo que tiene la variable global sustitucion y lo evalua para aplicar las reglas 
	def CambiaHilera(self, hilera):
		global sustitucion	
		global Salida	
		if(sustitucion==""):
			Salida= Salida+"\n" + hilera +"\n"
			sustitucion =self.recorrerHilera(hilera)
		else:
			sustitucion =self.recorrerHilera(sustitucion)

#metodo que recorre la listaDefinidos y la evalua para aplicar las reglas
	def ListaaEvaluar(self):
		#listaDefinidos = []
		global terminal 
		global sustitucion
		global aplico
		global listadef
		global Salida
		#listaDefinidos = self.evaluar(hilera)
		for i in listadef:
			self.CambiaHilera(i)
			#print(listaDefinidos)
			print("\n")
			terminal = False
			sustitucion=""
			aplico =False
		return Salida
		
		
		
#a = Algoritmo()
#hilera = """abc
#nop
#asd
#cvb"""

#hilera = """((()))
#(())
#()))
#((("""
#a.ListaaEvaluar(hilera)


	





	

				
			

