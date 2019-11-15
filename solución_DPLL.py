# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:04:33 2019

@author: manua
"""

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
        B = q+"+-"+p+"*"+r+"+-"+p+"Y-"+q+"+-"+r+"+"+p
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
    letrasProposicionalesB = [chr(x) for x in range(256, 500000)]
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
        B += "Y" + Y
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

def codificar():
	filas = [1, 2, 3, 4, 5, 6, 7, 8]
	columnas = [1, 2, 3, 4, 5, 6, 7, 8]
	letras = [chr(500000+i) for i in range (len(filas)*len(columnas))]
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
		fila = "h"
	return fila, columna

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

letras2 = codificar()
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]


regla1 = '09-8-7-6-5-4-3-*******0-98-7-6-5-4-3-*******0-9-87-6-5-4-3-*******0-9-8-76-5-4-3-*******0-9-8-7-65-4-3-*******0-9-8-7-6-54-3-*******0-9-8-7-6-5-43-*******0-9-8-7-6-5-4-3*******+++++++'

reglap = letras[62]+"-"+letras[61]+"-"+letras[60]+"-"+letras[59]+"-"+letras[58]+"-"+letras[57]+"-"+letras[56]+"-"+"******"+letras[63]+"*"

regla2 = letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+letras[7]+"-"+"******"+letras[63]+"*"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+letras[6]+"-"+"******"+letras[62]+"*"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+letras[5]+"-"+"******"+letras[61]+"*"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+letras[4]+"-"+"******"+letras[60]+"*"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+letras[3]+"-"+"******"+letras[59]+"*"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+letras[2]+"-"+"******"+letras[58]+"*"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+letras[1]+"-"+"******"+letras[57]+"*"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+letras[0]+"-"+"******"+letras[56]+"*"+letras[63]+"-"+letras[47]+"-"+letras[39]+"-"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+letras[7]+"-"+"******"+letras[55]+"*"+letras[62]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+letras[6]+"-"+"******"+letras[54]+"*"+letras[61]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+letras[5]+"-"+"******"+letras[53]+"*"+letras[60]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+letras[4]+"-"+"******"+letras[52]+"*"+letras[59]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+letras[3]+"-"+"******"+letras[51]+"*"+letras[58]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+letras[2]+"-"+"******"+letras[50]+"*"+letras[57]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+letras[1]+"-"+"******"+letras[49]+"*"+letras[56]+"-"+letras[40]+"-"+letras[32]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+letras[0]+"-"+"******"+letras[48]+"*"+letras[63]+"-"+letras[55]+"-"+letras[39]+"-"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+letras[7]+"-"+"******"+letras[47]+"*"+letras[62]+"-"+letras[54]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+letras[6]+"-"+"******"+letras[46]+"*"+letras[61]+"-"+letras[53]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+letras[5]+"-"+"******"+letras[45]+"*"+letras[60]+"-"+letras[52]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+letras[4]+"-"+"******"+letras[44]+"*"+letras[59]+"-"+letras[51]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+letras[3]+"-"+"******"+letras[43]+"*"+letras[58]+"-"+letras[50]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+letras[2]+"-"+"******"+letras[42]+"*"+letras[57]+"-"+letras[49]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+letras[1]+"-"+"******"+letras[41]+"*"+letras[56]+"-"+letras[48]+"-"+letras[32]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+letras[0]+"-"+"******"+letras[40]+"*"+letras[63]+"-"+letras[55]+"-"+letras[47]+"-"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+letras[7]+"-"+"******"+letras[39]+"*"+letras[62]+"-"+letras[54]+"-"+letras[46]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+letras[6]+"-"+"******"+letras[38]+"*"+letras[61]+"-"+letras[53]+"-"+letras[45]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+letras[5]+"-"+"******"+letras[37]+"*"+letras[60]+"-"+letras[52]+"-"+letras[44]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+letras[4]+"-"+"******"+letras[36]+"*"+letras[59]+"-"+letras[51]+"-"+letras[43]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+letras[3]+"-"+"******"+letras[35]+"*"+letras[58]+"-"+letras[50]+"-"+letras[42]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+letras[2]+"-"+"******"+letras[34]+"*"+letras[57]+"-"+letras[49]+"-"+letras[41]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+letras[1]+"-"+"******"+letras[33]+"*"+letras[56]+"-"+letras[48]+"-"+letras[40]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+letras[0]+"-"+"******"+letras[32]+"*"+letras[63]+"-"+letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[23]+"-"+letras[15]+"-"+letras[7]+"-"+"******"+letras[31]+"*"+letras[62]+"-"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[22]+"-"+letras[14]+"-"+letras[6]+"-"+"******"+letras[30]+"*"+letras[61]+"-"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[21]+"-"+letras[13]+"-"+letras[5]+"-"+"******"+letras[29]+"*"+letras[60]+"-"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[20]+"-"+letras[12]+"-"+letras[4]+"-"+"******"+letras[28]+"*"+letras[59]+"-"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[19]+"-"+letras[11]+"-"+letras[3]+"-"+"******"+letras[27]+"*"+letras[58]+"-"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[18]+"-"+letras[10]+"-"+letras[2]+"-"+"******"+letras[26]+"*"+letras[57]+"-"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[17]+"-"+letras[9]+"-"+letras[1]+"-"+"******"+letras[25]+"*"+letras[56]+"-"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+letras[16]+"-"+letras[8]+"-"+letras[0]+"-"+"******"+letras[24]+"*"+letras[63]+"-"+letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[31]+"-"+letras[15]+"-"+letras[7]+"-"+"******"+letras[23]+"*"+letras[62]+"-"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[14]+"-"+letras[6]+"-"+"******"+letras[22]+"*"+letras[61]+"-"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[13]+"-"+letras[5]+"-"+"******"+letras[21]+"*"+letras[60]+"-"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[12]+"-"+letras[4]+"-"+"******"+letras[20]+"*"+letras[59]+"-"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[11]+"-"+letras[3]+"-"+"******"+letras[19]+"*"+letras[58]+"-"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[10]+"-"+letras[2]+"-"+"******"+letras[18]+"*"+letras[57]+"-"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[9]+"-"+letras[1]+"-"+"******"+letras[17]+"*"+letras[56]+"-"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+letras[24]+"-"+letras[8]+"-"+letras[0]+"-"+"******"+letras[16]+"*"+letras[63]+"-"+letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[31]+"-"+letras[23]+"-"+letras[7]+"-"+"******"+letras[15]+"*"+letras[62]+"-"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[6]+"-"+"******"+letras[14]+"*"+letras[61]+"-"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[5]+"-"+"******"+letras[13]+"*"+letras[60]+"-"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[4]+"-"+"******"+letras[12]+"*"+letras[59]+"-"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[3]+"-"+"******"+letras[11]+"*"+letras[58]+"-"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[2]+"-"+"******"+letras[10]+"*"+letras[57]+"-"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[1]+"-"+"******"+letras[9]+"*"+letras[56]+"-"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+letras[24]+"-"+letras[16]+"-"+letras[0]+"-"+"******"+letras[8]+"*"+letras[63]+"-"+letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+"******"+letras[7]+"*"+letras[62]+"-"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+"******"+letras[6]+"*"+letras[61]+"-"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+"******"+letras[5]+"*"+letras[60]+"-"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+"******"+letras[4]+"*"+letras[59]+"-"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+"******"+letras[3]+"*"+letras[58]+"-"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+"******"+letras[2]+"*"+letras[57]+"-"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+"******"+letras[1]+"*"+letras[56]+"-"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+"******"+letras[0]+"*"+"***************************************************************"

regla3 = letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+"**"+letras[63]+"*"+letras[62]+"-"+letras[46]+"-"+letras[30]+"-"+letras[22]+"-"+"***"+letras[55]+"*"+letras[62]+"-"+letras[54]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+"*****"+letras[47]+"*"+letras[62]+"-"+letras[46]+"-"+letras[22]+"-"+letras[14]+"-"+"***"+letras[39]+"*"+letras[54]+"-"+letras[46]+"-"+letras[22]+"-"+letras[6]+"-"+"***"+letras[31]+"*"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[14]+"-"+letras[6]+"-"+"*****"+letras[23]+"*"+letras[46]+"-"+letras[38]+"-"+letras[22]+"-"+letras[6]+"-"+"***"+letras[15]+"*"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+"**"+letras[7]+"*"+letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+"*****"+letras[62]+"*"+letras[63]+"-"+letras[47]+"-"+letras[31]+"-"+letras[23]+"-"+letras[61]+"-"+letras[45]+"-"+letras[29]+"-"+letras[21]+"-"+"*******"+letras[54]+"*"+letras[63]+"-"+letras[55]+"-"+letras[39]+"-"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+letras[61]+"-"+letras[53]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+"***********"+letras[46]+"*"+letras[63]+"-"+letras[47]+"-"+letras[23]+"-"+letras[15]+"-"+letras[61]+"-"+letras[45]+"-"+letras[21]+"-"+letras[13]+"-"+"*******"+letras[38]+"*"+letras[55]+"-"+letras[47]+"-"+letras[23]+"-"+letras[7]+"-"+letras[53]+"-"+letras[45]+"-"+letras[21]+"-"+letras[5]+"-"+"*******"+letras[30]+"*"+letras[55]+"-"+letras[47]+"-"+letras[39]+"-"+letras[31]+"-"+letras[15]+"-"+letras[7]+"-"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[13]+"-"+letras[5]+"-"+"***********"+letras[22]+"*"+letras[47]+"-"+letras[39]+"-"+letras[23]+"-"+letras[7]+"-"+letras[45]+"-"+letras[37]+"-"+letras[21]+"-"+letras[5]+"-"+"*******"+letras[14]+"*"+letras[31]+"-"+letras[23]+"-"+letras[15]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+"*****"+letras[6]+"*"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+"*****"+letras[61]+"*"+letras[62]+"-"+letras[46]+"-"+letras[30]+"-"+letras[22]+"-"+letras[60]+"-"+letras[44]+"-"+letras[28]+"-"+letras[20]+"-"+"*******"+letras[53]+"*"+letras[62]+"-"+letras[54]+"-"+letras[38]+"-"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+letras[60]+"-"+letras[52]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+"***********"+letras[45]+"*"+letras[62]+"-"+letras[46]+"-"+letras[22]+"-"+letras[14]+"-"+letras[60]+"-"+letras[44]+"-"+letras[20]+"-"+letras[12]+"-"+"*******"+letras[37]+"*"+letras[54]+"-"+letras[46]+"-"+letras[22]+"-"+letras[6]+"-"+letras[52]+"-"+letras[44]+"-"+letras[20]+"-"+letras[4]+"-"+"*******"+letras[29]+"*"+letras[54]+"-"+letras[46]+"-"+letras[38]+"-"+letras[30]+"-"+letras[14]+"-"+letras[6]+"-"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[12]+"-"+letras[4]+"-"+"***********"+letras[21]+"*"+letras[46]+"-"+letras[38]+"-"+letras[22]+"-"+letras[6]+"-"+letras[44]+"-"+letras[36]+"-"+letras[20]+"-"+letras[4]+"-"+"*******"+letras[13]+"*"+letras[30]+"-"+letras[22]+"-"+letras[14]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+"*****"+letras[5]+"*"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+"*****"+letras[60]+"*"+letras[61]+"-"+letras[45]+"-"+letras[29]+"-"+letras[21]+"-"+letras[59]+"-"+letras[43]+"-"+letras[27]+"-"+letras[19]+"-"+"*******"+letras[52]+"*"+letras[61]+"-"+letras[53]+"-"+letras[37]+"-"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+letras[59]+"-"+letras[51]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+"***********"+letras[44]+"*"+letras[61]+"-"+letras[45]+"-"+letras[21]+"-"+letras[13]+"-"+letras[59]+"-"+letras[43]+"-"+letras[19]+"-"+letras[11]+"-"+"*******"+letras[36]+"*"+letras[53]+"-"+letras[45]+"-"+letras[21]+"-"+letras[5]+"-"+letras[51]+"-"+letras[43]+"-"+letras[19]+"-"+letras[3]+"-"+"*******"+letras[28]+"*"+letras[53]+"-"+letras[45]+"-"+letras[37]+"-"+letras[29]+"-"+letras[13]+"-"+letras[5]+"-"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[11]+"-"+letras[3]+"-"+"***********"+letras[20]+"*"+letras[45]+"-"+letras[37]+"-"+letras[21]+"-"+letras[5]+"-"+letras[43]+"-"+letras[35]+"-"+letras[19]+"-"+letras[3]+"-"+"*******"+letras[12]+"*"+letras[29]+"-"+letras[21]+"-"+letras[13]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+"*****"+letras[4]+"*"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+"*****"+letras[59]+"*"+letras[60]+"-"+letras[44]+"-"+letras[28]+"-"+letras[20]+"-"+letras[58]+"-"+letras[42]+"-"+letras[26]+"-"+letras[18]+"-"+"*******"+letras[51]+"*"+letras[60]+"-"+letras[52]+"-"+letras[36]+"-"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+letras[58]+"-"+letras[50]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+"***********"+letras[43]+"*"+letras[60]+"-"+letras[44]+"-"+letras[20]+"-"+letras[12]+"-"+letras[58]+"-"+letras[42]+"-"+letras[18]+"-"+letras[10]+"-"+"*******"+letras[35]+"*"+letras[52]+"-"+letras[44]+"-"+letras[20]+"-"+letras[4]+"-"+letras[50]+"-"+letras[42]+"-"+letras[18]+"-"+letras[2]+"-"+"*******"+letras[27]+"*"+letras[52]+"-"+letras[44]+"-"+letras[36]+"-"+letras[28]+"-"+letras[12]+"-"+letras[4]+"-"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[10]+"-"+letras[2]+"-"+"***********"+letras[19]+"*"+letras[44]+"-"+letras[36]+"-"+letras[20]+"-"+letras[4]+"-"+letras[42]+"-"+letras[34]+"-"+letras[18]+"-"+letras[2]+"-"+"*******"+letras[11]+"*"+letras[28]+"-"+letras[20]+"-"+letras[12]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+"*****"+letras[3]+"*"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+"*****"+letras[58]+"*"+letras[59]+"-"+letras[43]+"-"+letras[27]+"-"+letras[19]+"-"+letras[57]+"-"+letras[41]+"-"+letras[25]+"-"+letras[17]+"-"+"*******"+letras[50]+"*"+letras[59]+"-"+letras[51]+"-"+letras[35]+"-"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+letras[57]+"-"+letras[49]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+"***********"+letras[42]+"*"+letras[59]+"-"+letras[43]+"-"+letras[19]+"-"+letras[11]+"-"+letras[57]+"-"+letras[41]+"-"+letras[17]+"-"+letras[9]+"-"+"*******"+letras[34]+"*"+letras[51]+"-"+letras[43]+"-"+letras[19]+"-"+letras[3]+"-"+letras[49]+"-"+letras[41]+"-"+letras[17]+"-"+letras[1]+"-"+"*******"+letras[26]+"*"+letras[51]+"-"+letras[43]+"-"+letras[35]+"-"+letras[27]+"-"+letras[11]+"-"+letras[3]+"-"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[9]+"-"+letras[1]+"-"+"***********"+letras[18]+"*"+letras[43]+"-"+letras[35]+"-"+letras[19]+"-"+letras[3]+"-"+letras[41]+"-"+letras[33]+"-"+letras[17]+"-"+letras[1]+"-"+"*******"+letras[10]+"*"+letras[27]+"-"+letras[19]+"-"+letras[11]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+"*****"+letras[2]+"*"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+"*****"+letras[57]+"*"+letras[58]+"-"+letras[42]+"-"+letras[26]+"-"+letras[18]+"-"+letras[56]+"-"+letras[40]+"-"+letras[24]+"-"+letras[16]+"-"+"*******"+letras[49]+"*"+letras[58]+"-"+letras[50]+"-"+letras[34]+"-"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+letras[56]+"-"+letras[48]+"-"+letras[32]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+"***********"+letras[41]+"*"+letras[58]+"-"+letras[42]+"-"+letras[18]+"-"+letras[10]+"-"+letras[56]+"-"+letras[40]+"-"+letras[16]+"-"+letras[8]+"-"+"*******"+letras[33]+"*"+letras[50]+"-"+letras[42]+"-"+letras[18]+"-"+letras[2]+"-"+letras[48]+"-"+letras[40]+"-"+letras[16]+"-"+letras[0]+"-"+"*******"+letras[25]+"*"+letras[50]+"-"+letras[42]+"-"+letras[34]+"-"+letras[26]+"-"+letras[10]+"-"+letras[2]+"-"+letras[48]+"-"+letras[40]+"-"+letras[32]+"-"+letras[24]+"-"+letras[8]+"-"+letras[0]+"-"+"***********"+letras[17]+"*"+letras[42]+"-"+letras[34]+"-"+letras[18]+"-"+letras[2]+"-"+letras[40]+"-"+letras[32]+"-"+letras[16]+"-"+letras[0]+"-"+"*******"+letras[9]+"*"+letras[26]+"-"+letras[18]+"-"+letras[10]+"-"+letras[24]+"-"+letras[16]+"-"+letras[8]+"-"+"*****"+letras[1]+"*"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+"**"+letras[56]+"*"+letras[57]+"-"+letras[41]+"-"+letras[25]+"-"+letras[17]+"-"+"***"+letras[48]+"*"+letras[57]+"-"+letras[49]+"-"+letras[33]+"-"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+"*****"+letras[40]+"*"+letras[57]+"-"+letras[41]+"-"+letras[17]+"-"+letras[9]+"-"+"***"+letras[32]+"*"+letras[49]+"-"+letras[41]+"-"+letras[17]+"-"+letras[1]+"-"+"***"+letras[24]+"*"+letras[49]+"-"+letras[41]+"-"+letras[33]+"-"+letras[25]+"-"+letras[9]+"-"+letras[1]+"-"+"*****"+letras[16]+"*"+letras[41]+"-"+letras[33]+"-"+letras[17]+"-"+letras[1]+"-"+"***"+letras[8]+"*"+letras[25]+"-"+letras[17]+"-"+letras[9]+"-"+"**"+letras[0]+"*"+"***************************************************************"

regla4 = letras[63]+letras[62]+letras[61]+letras[60]+letras[59]+letras[58]+letras[57]+letras[56]+"+++++++"+letras[55]+letras[54]+letras[53]+letras[52]+letras[51]+letras[50]+letras[49]+letras[48]+"+++++++"+letras[47]+letras[46]+letras[45]+letras[44]+letras[43]+letras[42]+letras[41]+letras[40]+"+++++++"+letras[39]+letras[38]+letras[37]+letras[36]+letras[35]+letras[34]+letras[33]+letras[32]+"+++++++"+letras[31]+letras[30]+letras[29]+letras[28]+letras[27]+letras[26]+letras[25]+letras[24]+"+++++++"+letras[23]+letras[22]+letras[21]+letras[20]+letras[19]+letras[18]+letras[17]+letras[16]+"+++++++"+letras[15]+letras[14]+letras[13]+letras[12]+letras[11]+letras[10]+letras[9]+letras[8]+"+++++++"+letras[7]+letras[6]+letras[5]+letras[4]+letras[3]+letras[2]+letras[1]+letras[0]+"+++++++*******"

reglas = regla1+regla2+regla3+regla4+"***"


regla = string2Tree(reglas)
r = Inorder(regla)
#print(r)
prueba_tseitin = Tseitin(r, letras)
prueba_clausal = formaClausal(prueba_tseitin)
#print(prueba_clausal)
prueba_dpll = DPLL(prueba_clausal, {})
#print(prueba_dpll)
dic_prueba = diccionario(prueba_dpll[1])
print(dic_prueba)
print(len(dic_prueba))
