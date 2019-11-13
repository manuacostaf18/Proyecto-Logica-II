from copy import deepcopy
def codificar():
    filas = [1, 2, 3, 4, 5, 6, 7, 8]
    columnas = [1, 2, 3, 4, 5, 6, 7, 8]
    letras = [chr(256+i) for i in range (len(filas)*len(columnas))]
    return letras

letras = codificar()

def hay_clausula_unit(lista):
	for n in lista:
		#print(n)
		if len(n) == 1:
			return True
	return False


def complemento(n):
	x = n#[0]
	if x[0] == '-':
		return x[1]
	else:
		return '-' + x


def unit_propagate(S, I):
	#print("Haciendo unit propagate")
	#print(S, I)
	c_vacio = []
	aux = hay_clausula_unit(S)
	#print(aux)
	while(c_vacio not in S and aux):
		for n in S:
			if len(n) == 1:
				l = n[0]
		S = [y for y in S if l not in y]
		for w in S:
			if complemento(l) in w:
				w.remove(complemento(l))
		if l[0] == '-':
			I[l[1]] = 0
		else:
			I[l] = 1
		aux = hay_clausula_unit(S)
	return S, I


def DPLL(S, I):
	S, I = unit_propagate(S, I)
	c_vacio = []
	if c_vacio in S:
		return "Insatisfacible", {}
	elif len(S) == 0:
		return "Satisfacible", I
	l = ""
	for n in S:
		for x in n:
			if x not in I.keys():
				l = x
	lBarra = complemento(l)
	if l == "":
		print("Oh oh, problemas...")
		return None
	Sp = deepcopy(S)
	Sp = [n for n in Sp if l not in n]
	for m in Sp:
		if lBarra in m:
			m.remove(lBarra)	
	Ip = deepcopy(I)
	if l[0] == '-':
		Ip[l[1]] = 0
	else:
		Ip[l] = 1

	S1, I1 = DPLL(Sp, Ip)
	if S1 == "Satisfacible":
		return S1, I1
	else:
		Spp = deepcopy(S)
		for a in Spp:
			if complemento(l) in a:
				Spp.remove(a)
		for b in Spp:
			if l in b:
				b.remove(l)
		Ipp = deepcopy(I)
		if l[0] == '-':
			Ipp[l[1]] = 0
		else:
			Ipp[l] = 1
		return DPLL(Spp, Ipp)







S1 = [['p'], ['-p', 'q'], ['-q', 'r', 's'], ['u', '-s', 'r'], ['r', 't'], ['p', 's', '-t'], ['-r', 'u']]
prueba1 = unit_propagate(S1, {})
print("prueba1: ", prueba1)

S2 = [['p'], ['-p', 'q', '-r'], ['q']]
prueba2 = DPLL(S2, {})
print("prueba2: ", prueba2)

S3 = [['p'], ['-p', 'q'], ['-q', 'r', 's']]
prueba3 = DPLL(S3, {})
print("prueba3: ", prueba3)

S4 = [['p', 'q', 'r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
prueba4 = DPLL(S4, {})
print("prueba4: ", prueba4)

S5 = [['p', 'q', 'r', '-s'], ['p', 't', 's'], ['-p', '-q'], ['p', 'r', '-q', '-s']]
prueba5 = DPLL(S5, {})
print("prueba5: ", prueba5)

S6 = [['p', 'q', '-r'], ['r', 's', 't'], ['t'], ['p', 's'], ['q', '-p']]
prueba6 = DPLL(S6, {})
print("prueba6: ", prueba6)

S7 = [['p', '-q'], ['-p', '-q'], ['q', 'r'], ['-q', '-r'], ['-p', '-r'], ['p', '-r']]
prueba7 = DPLL(S7, {})
print("prueba7: ", prueba7)

S8 = [['r', 'p', 's'], ['-r', '-p', '-s'], ['-r', 'p', 's'], ['p', '-s']]
prueba8 = DPLL(S8, {})
print("prueba8: ", prueba8)

