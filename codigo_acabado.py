from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

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
	c_vacio = []
	aux = hay_clausula_unit(S)
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

def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    #print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"+-"+q+"*"+p+"+"+q
    elif "*" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"+-"+p+"*"+r+"+-"+p+"*-"+q+"+-"+r+"+"+p
    elif "+" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"+"+p+"*-"+r+"+"+p+"*"+q+"+"+r+"+-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"+"+p+"*-"+r+"+"+p+"*-"+q+"+"+r+"+-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 900000)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    L =[]
    Pila = []
    i = -1
    s = A[0]
    #atomo = letrasProposicionalesA + letrasProposicionalesB
    while len(A) > 0:
        if s in (letrasProposicionalesA or letrasProposicionalesB) and Pila[-1] == '-' and len(Pila) > 0:#modificacion.
            i += 1
            atomo = letrasProposicionalesB[i]
            Pila = Pila[:-1]
            Pila.append(atomo)
            L.append(atomo+'='+'-'+s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = Pila[-1]
            o = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo + "=" + "(" + v + o + w + ")")
            s = atomo
        else:
            Pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    B = ''
    if i < 0:
        atomo = Pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for X in L:
        Y = enFNC(X)
        B += "*" + Y
    B = atomo + B
    return B
    return "OK"

def Clausula(C):
    L = []
    while len(C) > 0:
        s = C[0]
        if s == "+":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L
    return "OK"

def formaClausal(A):
    L = []
    i = 0
    while len(A) > 0:
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == "*":
                L.append(Clausula(A[:i]))
                A = A[i + 1:]
                i = 0
            else:
                i += 1
    return L
    return "OK"

class Tree():
    def __init__(self,label,iz,der):
        self.label = label
        self.left = iz
        self.right = der

def string2Tree(A):
    conectivos = ["*","+",">"]
    stack = []
    for c in A:
        if c in letras:
            stack.append(Tree(c,None,None))
        elif c == "-":
            formaux = Tree(c, None, stack[-1])
            del stack[-1]
            stack.append(formaux)
        elif c in conectivos:
            formaux = Tree(c, stack[-1], stack[-2])
            del stack[-1]
            del stack[-1]
            stack.append(formaux)
    return stack[-1]

def Inorder(arbol):
	conectivosBinarios = ["*","+",">"]
	if arbol.label in letras:
		return arbol.label
	elif arbol.label == "-":
		return arbol.label+Inorder(arbol.right)
	elif arbol.label in conectivosBinarios:
		return "("+Inorder(arbol.left)+arbol.label+Inorder(arbol.right)+")"
	else:
		print("Oops, rotulo incorrecto")

def diccionario(dic):
    d = {}
    for n in dic.keys():
        if n in letras:
            d[n] = dic[n]
    return d

def balanced(f):
	s = []
	for i in f:
		if i == '(':
			s.append(i)
		elif i == ')':
			if len(s) == 0:
				return False
			elif s[-1] == '(':
				s = s[:-1]
	if len(s) == 0:
		return True
	else:
		return False
    
def diccionario_true(dic): #retorna un diccionario sólo con las letras que tienen valor 1. 
    d = {}
    for n in dic.keys():
        if dic[n] == 1:
            d[n] = dic[n]
    return d
    
def lista_true(dic): #retorna una lista con las letras que tienen valor 1.
    d = []
    for n in dic.keys():
        d.append(n)
    return d
            
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

regla_a1 = 'l-k-j-h-g-f-e-d-c-b-3-U-N-F-x-p-i-a*****************'
regla_a2 = 'o-ñ-n-m-l-k-j-s-r-q-d-c-b-3-U-N-F-x-p-a-i********************'
regla_a3 = 'A-z-y-l-k-j-w-v-u-t-s-r-q-3-U-N-F-x-i-a-p********************'
regla_a4 = 'I-H-G-s-r-q-E-D-C-B-A-z-y-3-U-N-F-p-i-a-x********************'
regla_a5 = 'P-O-Ñ-A-z-y-M-L-K-J-I-H-G-3-U-N-x-p-i-a-F********************'
regla_a6 = 'X-W-V-I-H-G-T-S-R-Q-P-O-Ñ-3-U-F-x-p-i-a-N********************'
regla_a7 = '6-5-4-P-O-Ñ-2-1-Z-Y-X-W-V-3-N-F-x-p-i-a-U********************'
regla_a8 = 'X-W-V-0-9-8-7-6-5-4-U-N-F-x-p-i-a-3*****************'
regla_a = regla_a1 + regla_a2 + regla_a3 + regla_a4 + regla_a5 + regla_a6 + regla_a7 + regla_a8 + '+++++++'

regla_b1 = 'n-m-k-i-h-g-f-e-d-c-a-4-V-Ñ-G-y-q-j-b******************'
regla_b2 = 'u-t-r-p-f-e-c-a-o-ñ-n-m-l-k-i-4-V-Ñ-G-y-q-b-j**********************'
regla_b3 = 'C-B-z-x-n-m-k-i-w-v-u-t-s-r-p-4-V-Ñ-G-y-j-b-q**********************'
regla_b4 = 'K-J-H-F-u-t-r-p-E-D-C-B-A-z-x-4-V-Ñ-G-q-j-b-y**********************'
regla_b5 = 'R-Q-O-N-C-B-y-x-M-L-K-J-I-H-F-4-V-Ñ-y-q-j-b-G**********************'
regla_b6 = 'Z-Y-W-U-K-J-H-F-T-S-R-Q-P-O-N-4-V-G-y-q-j-b-Ñ**********************'
regla_b7 = '8-7-5-3-R-Q-O-N-2-1-Z-Y-X-W-U-4-Ñ-G-y-q-j-b-V**********************'
regla_b8 = 'Z-Y-W-U-0-9-8-7-6-5-3-b-V-Ñ-G-y-q-j-4******************'
regla_b = regla_b1 + regla_b2 + regla_b3 + regla_b4 + regla_b5 + regla_b6 + regla_b7 + '++++++'

regla_c1 = 'ñ-n-m-l-j-i-h-g-f-e-d-b-a-5-W-O-H-z-r-k-c********************'
regla_c2 = 'o-ñ-n-m-l-j-i-v-u-t-s-q-p-g-f-e-d-b-a-5-W-O-H-z-r-c-k**************************'
regla_c3 = 'D-C-B-A-y-x-w-v-u-t-s-q-p-ñ-n-m-l-j-i-5-W-O-H-z-k-c-r**************************'
regla_c4 = 'L-K-J-I-G-F-E-D-C-B-A-y-x-v-u-t-s-q-p-5-W-O-H-r-k-c-z**************************'
regla_c5 = 'S-R-Q-P-Ñ-N-M-L-K-J-I-G-F-D-C-B-A-y-x-5-W-O-z-r-k-c-H**************************'
regla_c6 = '1-Z-Y-X-V-U-T-S-R-Q-P-Ñ-N-L-K-J-I-G-F-5-W-H-z-r-k-c-O**************************'
regla_c7 = '9-8-7-6-4-3-2-1-Z-Y-X-V-U-S-R-Q-P-Ñ-N-5-O-H-z-r-k-c-W**************************'
regla_c8 = '0-9-8-7-6-4-3-1-Z-Y-X-V-U-c-W-O-H-z-r-k-5********************'
regla_c = regla_c1 + regla_c2 + regla_c3 + regla_c4 + regla_c5 + regla_c6 + regla_c7 + regla_c8 + '+++++++'

regla_d1 = 'ñ-n-k-i-h-g-f-e-c-b-a-6-X-P-I-A-s-l-d******************'
regla_d2 = 'v-u-r-p-o-ñ-n-m-k-j-i-g-f-c-a-6-X-P-I-A-s-d-l**********************'
regla_d3 = 'D-C-z-x-w-v-u-t-r-q-p-ñ-n-k-i-6-X-P-I-A-l-d-s**********************'
regla_d4 = 'L-K-H-F-E-D-C-B-z-y-x-v-u-r-p-6-X-P-I-l-s-d-A**********************'
regla_d5 = 'S-R-O-N-M-L-K-J-H-G-F-D-C-z-x-6-X-P-A-l-s-d-I**********************'
regla_d6 = '1-Z-W-U-T-S-R-Q-O-Ñ-N-L-K-H-F-6-X-I-A-l-s-d-P**********************'
regla_d7 = '9-8-5-3-2-1-Z-Y-W-V-U-S-R-O-N-6-P-I-A-l-s-d-X**********************'
regla_d8 = '0-9-8-7-5-4-3-1-Z-W-U-d-X-P-I-A-s-l-6******************'
regla_d = regla_d1 + regla_d2 + regla_d3 + regla_d4 + regla_d5 + regla_d6 + regla_d7 + regla_d8 + '+++++++'

regla_e1 = 'o-n-k-j-h-g-f-d-c-b-a-7-Y-Q-J-B-t-m-e******************'
regla_e2 = 'v-u-r-q-h-f-c-b-o-ñ-n-l-k-j-i-7-Y-Q-J-B-t-e-m**********************'
regla_e3 = 'E-C-z-y-w-v-u-s-r-q-p-o-n-k-j-7-Y-Q-J-B-m-e-t**********************'
regla_e4 = 'M-K-H-G-E-D-C-A-z-y-x-w-u-r-q-7-Y-Q-J-t-m-e-B**********************'
regla_e5 = 'T-R-O-Ñ-M-L-K-I-H-G-F-E-C-z-y-7-Y-Q-B-t-m-e-J**********************'
regla_e6 = '2-Z-W-V-T-S-R-P-O-Ñ-N-M-K-H-G-7-Y-J-B-t-m-e-Q**********************'
regla_e7 = '0-8-5-4-2-1-Z-X-W-V-U-T-R-O-Ñ-7-Q-J-B-t-m-e-Y**********************'
regla_e8 = '0-9-8-6-5-4-3-2-Z-W-V-e-Y-Q-J-B-t-m-7******************'
regla_e = regla_e1 + regla_e2 + regla_e3 + regla_e4 + regla_e5 + regla_e6 + regla_e7 + regla_e8 + '+++++++'

regla_f1 = 'o-ñ-m-l-k-j-h-g-e-d-c-b-a-8-Z-R-K-C-u-n-f********************' 
regla_f2 = 'w-v-t-s-r-q-o-ñ-m-l-k-j-i-h-g-e-d-c-b-8-Z-R-K-C-u-f-n**************************'
regla_f3 = 'E-D-B-A-z-y-w-v-t-s-r-q-p-o-ñ-m-l-k-j-8-Z-R-K-C-n-f-u**************************'
regla_f4 = 'M-L-J-I-H-G-E-D-B-A-z-y-x-w-v-t-s-r-q-8-Z-R-K-u-n-f-C**************************'
regla_f5 = 'T-S-Q-P-O-Ñ-M-L-J-I-H-G-F-E-D-B-A-z-y-8-Z-R-C-u-n-f-K**************************'
regla_f6 = '2-1-Y-X-W-V-T-S-Q-P-O-Ñ-N-M-L-J-I-H-G-8-Z-K-C-u-n-f-R**************************'
regla_f7 = '0-9-7-6-5-4-2-1-Y-X-W-V-U-T-S-Q-P-O-Ñ-8-R-K-C-u-n-f-Z**************************'
regla_f8 = '0-9-7-6-5-4-3-2-1-Y-X-W-V-f-Z-R-K-C-u-n-8********************'
regla_f = regla_f1 + regla_f2 + regla_f3 + regla_f4 + regla_f5 + regla_f6 + regla_f7 + regla_f8 + '+++++++'

regla_g1 = 'o-n-l-k-h-f-e-d-c-b-a-9-1-S-L-D-v-ñ-g******************'
regla_g2 = 'w-u-s-r-o-n-m-l-k-j-i-h-f-d-c-9-1-S-L-D-v-g-ñ**********************'
regla_g3 = 'E-C-A-z-w-u-t-s-r-q-p-o-n-l-k-9-1-S-L-D-ñ-g-v**********************'
regla_g4 = 'M-K-I-H-E-C-B-A-z-y-x-w-u-s-r-9-1-S-L-v-ñ-g-D**********************'
regla_g5 = 'T-R-P-O-M-K-J-I-H-G-F-E-C-A-z-9-1-S-D-v-ñ-g-L**********************'
regla_g6 = '2-Z-X-W-T-R-Q-P-O-Ñ-N-M-K-I-H-9-1-L-D-v-ñ-g-S**********************'
regla_g7 = '0-8-6-5-2-Z-Y-X-W-V-U-T-R-P-O-9-S-L-D-v-ñ-g-1**********************'
regla_g8 = '0-8-7-6-5-4-3-2-Z-X-W-g-1-S-L-D-v-ñ-9*****************'
regla_g = regla_g1 + regla_g2 + regla_g3 + regla_g4 + regla_g5 + regla_g6 + regla_g7 + regla_g8 + '+++++++'

regla_h1 = 'ñ-n-m-g-f-e-d-c-b-a-0-2-T-M-E-w-o-h*****************'
regla_h2 = 'v-u-t-ñ-n-m-l-k-j-i-g-f-e-0-2-T-M-E-w-h-o********************'
regla_h3 = 'D-C-B-v-u-t-s-r-q-p-ñ-n-m-0-2-T-M-E-o-h-w********************'
regla_h4 = 'L-K-J-D-C-B-A-z-y-x-v-u-t-0-2-T-M-w-o-h-E********************'
regla_h5 = 'S-R-Q-L-K-J-I-H-G-F-D-C-B-0-2-T-E-w-o-h-M********************'
regla_h6 = '1-Z-Y-S-R-Q-P-O-Ñ-N-L-K-J-0-2-M-E-w-o-h-T********************'
regla_h7 = '9-8-7-1-Z-Y-X-W-V-U-S-R-Q-0-T-M-E-w-o-h-2********************'
regla_h8 = '9-8-7-6-5-4-3-1-Z-Y-h-2-T-M-E-w-o-0*****************'
regla_h = regla_h1 + regla_h2 + regla_h3 + regla_h4 + regla_h5 + regla_h6 + regla_h7 + regla_h8 + '+++++++'

regla = regla_a + regla_b + regla_c + regla_d + regla_e + regla_f + regla_g + regla_h + '*******' 

prueba1 = regla_a + regla_b + regla_c + '**'
prueba2 = regla_a + regla_h + '*'
prueba3 = regla_a + regla_b + regla_g + regla_h + '***'
prueba4 = regla_a + regla_b + regla_d + '**'

rprueba = string2Tree(regla)
r = Inorder(rprueba)
print(r)
prueba_tseitin = Tseitin(r, letras)
prueba_clausal = formaClausal(prueba_tseitin)
#print(prueba_clausal)
prueba_dpll = DPLL(prueba_clausal, {})
print('DPLL:', prueba_dpll)
dic_prueba = diccionario(prueba_dpll[1])
print('')
print('Valores de las letras:', dic_prueba)
#print(len(dic_prueba))
dic_final = diccionario_true(dic_prueba)
print('')
print('Diccionario letras con True:', dic_final)
#print(len(dic_final))
lista = lista_true(dic_final)
print('')
print('Lista letras con true:', lista)
