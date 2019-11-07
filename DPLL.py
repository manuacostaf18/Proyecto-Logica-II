def codificar():
    filas = [1, 2, 3, 4, 5, 6, 7, 8]
    columnas = [1, 2, 3, 4, 5, 6, 7, 8]
    letras = [chr(256+i) for i in range (len(filas)*len(columnas))]
    return letras

letras = codificar()

def hay_clausula_unit(lista):
	for n in lista:
		if len(n) == 1:
			return True
		else:
			return False
			

def complemento(n):
	 x = n[0]
	 if	x[0] == '-':
	 	return x[1]
	 else:
	 	return '-' + x		

			
def unit_propagate(S, I):
	c_vacio = []
	while(c_vacio not in S and hay_clausula_unit(S)):
		for n in S:
			if len(n) == 1:
				l = n[0]
		for y in S:
			if l in y:
				S.remove(y)
		for w in S:
			if complemento(l) in w:
				w.remove(complemento(l))
		if l[0] == '-':
			I[l] = 0
		else:
			I[l] = 1
	return S, I
			

def DPLL(S, I):
	S, I = unit_propagate(S, I)
	c_vacio = []
	if c_vacio in S:
		return "Insatisfacible", {}
	elif len(S) == 0:
		return "Satisfacible", I
	for n in S:
		for x in n:
			if x not in I.keys():
				l = x	
	Sp = S
	for w in S:
		if l in w:
			Sp.remove(w)
	for m in S:
		if complemento(l) in m:
			m.remove(complemento(l))		
	Ip = I
	if l[0] == '-':
		Ip[l] = 0
	else:
		Ip[l] = 1
	if DPLL(Sp, Ip) == ("Satisfacible", Ip):
		return "Satisfacible", Ip
	else:
		Spp = S
		for a in Spp:
			if complemento(l) in a:
				Spp.remove(a)
		for b in Spp:
			if l in b:
				b.remove(l)
		Ipp = I
		if l[0] == '-':
			Ipp[l] = 0
		else:
			Ipp[l] = 1
		return DPLL(Spp, Ipp)
				
		
	
	
	
		
S1 = [['p'], ['-p', 'q'], ['-q', 'r', 's'], ['u', '-s', 'r'], ['r', 't'], ['p', 's', '-t'], ['-r', 'u']]
prueba1 = unit_propagate(S1, {})
print(prueba1)

S2 = [['p'], ['-p', 'q', '-r'], ['q']]
prueba2 = DPLL(S2, {})
print(prueba2)

S3 = [['p'], ['-p', 'q'], ['-q', 'r', 's']]
prueba3 = DPLL(S3, {})
print(prueba3)

S4 = [['p', '-q', 'r'], ['-p', 'q', '-r'], ['-p', '-q', 'r'], ['-p', '-q', '-r']]
prueba4 = DPLL(S4, {})
print(prueba4)










