class Algoritmo:
	def BinarioToUnario():
		list=[]
		carga = """%hola
#symbols 01
#vars |
#markers ABC
1->0| 
|0->0|| 
0-> Λ."""
#guardar cada línea en carga
		for line in carga.splitlines():
			list.append(line)
#saber el tamaño de la lista
		list_len = len(list)
#Listas para guardar las reglas, variables, simbolos
		lista1=[]
		lista2=[]
		lista3=[]
		lista4=[]
		lista5=[]
		for x in range(list_len):
			caracter = list[x]
			if caracter[0] == '%':
				print(" ")
			
#si empieza con # y tiene symbols en la linea, lo guarda en la lista3
			elif(caracter[0] == '#' and caracter.find("#symbols") is not -1):
				#print("Entro2")
				simb = list[x].split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista3.append(palabra[y])
					#print("Lista3")
				#print(lista3)
				
#si tiene vars en la linea, lo guarda en la lista4
			elif(caracter.find("#vars") is not -1):
				#print("Entro3")
				simb = list[x].split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista4.append(palabra[y])
					#print("Lista3")
				#print(lista4)
				
#si tiene markers en la linea, lo guarda en la lista5
			elif(caracter.find("#markers") is not -1):
				#print("Entro5")
				simb = list[x].split(" ")
				palabra = simb[1]
				for y in range(len(palabra)):
					lista5.append(palabra[y])
					#print("Lista3")
				#print(lista5)
			
#sino las reglas las guarda en lista2 y lista1
			else:
				#print("Entro4")
				#print(caracter[0])
				simb = list[x].split("->")
				#print(x, simb)
				lista1.append(simb[0])
				lista2.append(simb[1])
		print("Lista1", lista1)
		print("Lista2", lista2)
		print("Lista3", lista3)
		print("Lista4", lista4)
		print("Lista5", lista5)

	BinarioToUnario()
		