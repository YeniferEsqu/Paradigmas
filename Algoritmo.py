import re
class Algoritmo:
#variables globales
	global lista1 #reglas busqueda
	global lista2 #reglas de sustitucion
	global lista3 #simbolos
	global lista4 #variables
	global lista5 #marcadores
	global variablesUsadas  #lista auxiliar para almacenar las variable que utiliza una regla y su posicion en dicha cadena

	variablesUsadas=[]
	lista1=[]
	lista2=[]
	lista3=[]
	lista4=[]
	lista5=[]

#devuelve posicion de regla terminal	
	def ReglaTerminal(self):
		for x in lista2:
			if(x.find(".")== 1):
				terminal = lista2.index(x)
				return terminal

	
	
	def CargarLista(self, algoritmo):
		list=[]
		carga = algoritmo
#guardar cada línea en carga excepto campos vacios y comentarios
		for line in carga.splitlines():			
			if(len(line) > 1 and line[0] is not ' '):
				if(line[0] != '%'):
				    list.append(line)

#saber el tamaño de la lista
		list_len = len(list)
#Listas para guardar las reglas, variables, simbolos, marcadores
		
		for x in range(list_len):
			caracter = list[x]
			car = caracter[0]
			
#si tiene symbols en la linea, lo guarda en la lista3
			if(caracter.find("#symbols") is not -1):
				simb = list[x].split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista3.append(palabra[y])
				
#si tiene vars en la linea, lo guarda en la lista4
			elif(caracter.find("#vars") is not -1):
				#print("Entro3")
				simb = list[x].split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista4.append(palabra[y])
				
#si tiene markers en la linea, lo guarda en la lista5
			elif(caracter.find("#markers") is not -1):
				#print("Entro5")
				simb = list[x].split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista5.append(palabra[y])
			
#sino las reglas las guarda en lista2 y lista1
			else:
				simb = list[x].split("->")
				lista1.append(simb[0])
				lista2.append(simb[1])

		#print("Lista1", lista1)
		#print("Lista2", lista2)
		#print("Lista3", lista3)
		#print("Lista4", lista4)
		#print("Lista5", lista5)
	
	#metodo para agarrar lo del campo de texto y comprobar que esta en el alfabeto
	def estaenlalista(self, cadena):
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
		

	def evaluar(self,hilera):
		cadena = hilera
		lista=[]
		listadef=[]
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
		print(listadef)

	#metodo que busca si existe una etiqueta 
	def buscaEtiqueta(self, regla):
		etiqueta = re.match("\w[+?]+:" , regla)
		if (etiqueta != None):
			etiqueta = etiqueta.group()
			etiqueta = re.sub(r":","",etiqueta)
			return etiqueta
		else:
			return None
		
		

    #metodo que convierte una regla de busqueda en un patron de busqueda de expresiones regulares
	def convertirPatron(self,etiqueta,regla):
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
				if cont == 0:
					patron = patron +"(" + regla[x] +")"
				else:
					patron = patron +"+(" + regla[x] +")"
				cont = cont + 1
			elif  regla[x] in lista4:  #si esta en la lista de variables agrega dicha variable a la lista auxiliar 
				variablesUsadas.append(regla[x])
				variablesUsadas.append(cont)
				variablesUsadas.append("")
				if cont == 0:
					patron = patron +"\w"
				else:
					patron = patron +"+\w"
				cont = cont + 1
			elif regla[x] in lista5:   #si esta en la lista de marcadores
				if cont == 0:
					patron = patron +"(" + regla[x] +")"
				else:
					patron = patron +"+(" + regla[x] +")"
				cont = cont + 1
			else:
				return None
		return patron

    #recibe un patron y una hilera y determina si existe alguna coincidencia
	def buscarPatrones(self,patron,hilera):
		if patron == "^":
			if hilera == "":
				return ""
			else:
				return None
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

			return patronEncontrado
		else:
			return None


				
			

