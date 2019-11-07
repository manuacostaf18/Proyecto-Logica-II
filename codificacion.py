def codificar():
	filas = [1, 2, 3, 4, 5, 6, 7, 8]
	columnas = [1, 2, 3, 4, 5, 6, 7, 8]
	letras = [chr(256+i) for i in range (len(filas)*len(columnas))]
	return letras


def decodificar(n):
	x = ord(n)
	m = x % 8
	columna = m + 1
	fila = ((x-256)//8)+1
	if fila == 1:
		fila = "a"
	elif fila == 2:
		fila = "b"
	elif fila == 3:
		fila = "c"
	elif fila == 4:
		fila = "d"
	elif fila == 5:
		fila = "e"
	elif fila == 6:
		fila = "f"
	elif fila == 7:
		fila = "g"
	elif fila == 8:
		fila = "g"
	return fila, columna

b = codificar()
a = decodificar(b[10])
print(a)
