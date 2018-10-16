import re
global lista1 #reglas busqueda
global lista2 #reglas de sustitucion
global lista3 #simbolos
global lista4 #variables
global lista5 #marcadores
global variablesUsadas  #lista auxiliar para almacenar las variable que utiliza una regla y su posicion en dicha cadena
global etiquetaInicio
etiquetaInicio = None
variablesUsadas =[]
lista1=["XβX","XβY","Xβ","βX","X"]
lista2=["Xβ","XYβ","X.","Xβ","βX"]
lista3=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
lista4=["X","Y"]
lista5=['β']

#metodo que busca si existe una etiqueta 
def buscaEtiqueta(regla):
	etiqueta = re.match("\w[+?]+:" , regla)
	if (etiqueta != None):
		etiqueta = etiqueta.group()
		etiqueta = re.sub(r":","",etiqueta)
		return etiqueta
	else:
		return None
	
#metodo que busca si existe una etiqueta al final de una regla 
# y la asigna a su correspondiente variable global
def buscaEtiquetaInicio(reglaSustitucion):
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
def convertirPatron(etiqueta,regla):
	global variablesUsadas
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
				patron = patron +"."
			else:
				patron = patron +"+."
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
def buscarPatrones(patron,hilera):
	global variablesUsadas
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
					else:
						if variablesUsadas[i + 2] == variablesUsadas[j + 2]:
							return None


		return patronEncontrado
	else:
		return None

#recibe el patron encontrado en el metodo anterior, la regla de sustitucion correspondiente 
#y la hilera a la que se va a aplicar. Devuelve la hilera con la sustitucion hecha
def sustituirRegla(patronEncontrado,reglaSustitucion,hilera):
	global variablesUsadas
	global lista3
	global lista4
	global lista5
	etiqueta = buscaEtiquetaInicio(reglaSustitucion)
	if etiqueta != None:
		etiqueta = "("+etiqueta+")"
		reglaSustitucion = re.sub(etiqueta,"",reglaSustitucion)
	
	if patronEncontrado == "":
		return reglaSustitucion
	
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
			if reglaSustitucion[i] in lista3 or reglaSustitucion[i] in lista4  or reglaSustitucion[i] in lista5 or reglaSustitucion[i] == '.':
					if reglaSustitucion[i] != '.':
						sustitucion = sustitucion + reglaSustitucion[i]
			else:
				return None
	
	return re.sub(patronEncontrado,sustitucion,hilera,1)

tam = len(lista1)
for i in range(0,tam):
	hilera = "abcβ"
	print("Regla: ")
	print(lista1[i])
	etiqueta = buscaEtiqueta(lista1[i])
	print("Etiqueta: ")
	print(etiqueta)
	patron = convertirPatron(etiqueta,lista1[i])
	print("Patron: ")
	print(patron)
	patronEncontrado = buscarPatrones(patron,hilera)
	print("Patron Encontrado: ")
	print(patronEncontrado)
	if patronEncontrado != None:
		print("Regla Sustitucion: ")
		print(lista2[i])
		print("Hilera Resultante: ")
		print(sustituirRegla(patronEncontrado,lista2[i],hilera))
		print("Etiqueta Inicio: ")
		print(etiquetaInicio)
		break
