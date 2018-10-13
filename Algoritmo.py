class Algoritmo:
#variables globales
	global lista1
	global lista2
	global lista3
	global lista4
	global lista5

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

		
	

		