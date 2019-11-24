from copy import deepcopy
import sys
import pygame

sys.setrecursionlimit(10000)


class Tree():#Clase árbol.
    def __init__(self,label,iz,der):
        self.label = label
        self.left = iz
        self.right = der


def string2Tree(A):#Convierte una cadena de string en un objeto árbol.
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


def Inorder(arbol):#Retorna la forma 'inorder' de un árbol.
	conectivosBinarios = ["*","+",">"]
	if arbol.label in letras:
		return arbol.label
	elif arbol.label == "-":
		return arbol.label+Inorder(arbol.right)
	elif arbol.label in conectivosBinarios:
		return "("+Inorder(arbol.left)+arbol.label+Inorder(arbol.right)+")"
	else:
		print("Oops, rotulo incorrecto")


def hay_clausula_unit(lista):#Retorna true si hay una cláusula unitaria.
	for n in lista:
		#print(n)
		if len(n) == 1:
			return True
	return False


def complemento(n):#Retorna el complemento de la cláusula unitaria ingresada. 
	x = n
	if x[0] == '-':
		return x[1]
	else:
		return '-' + x


def unit_propagate(S, I):#Función que realiza la propagación de la unidad.
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


def DPLL(S, I):#Retorna si es satisfacible o no, y, en caso de que lo sea, la interpretación con la cual se satisface.
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


def enFNC(A):#Convierte una fórmula a su forma normal conjuntiva.
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
        B = '-'+q+"+"+p+"*-"+r+"+"+p+"*"+q+"+"+r+"+-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"+"+p+"*-"+r+"+"+p+"*-"+q+"+"+r+"+-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B


def Tseitin(A, letrasProposicionalesA):#Realiza el procedimiento de Tseitin.
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


def Clausula(C):#Convierte una fórmula en una cláusula.
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


def formaClausal(A):#Retorna la forma clausal de una fórmula.
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





def diccionario(dic): #retorna un diccionario con los valores de las 64 letras proposicionales. 
    d = {}
    for n in dic.keys():
        if n in letras:
            d[n] = dic[n]
    return d


def balanced(f):#retorna true si la fórmula tiene paréntesis balanceados.
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
            
#Lista de letras proposicionales.
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

#Reglas

#Reglas casilla a:
regla_a1 = '3-U-N-F-x-p-l-k-j-i-h-g-f-e-d-c-b-a*****************'
regla_a2 = '3-U-N-F-x-s-r-q-p-o-ñ-n-m-l-k-j-d-c-b-a-i********************'
regla_a3 = '3-U-N-F-A-z-y-x-w-v-u-t-s-r-q-l-k-j-i-a-p********************'
regla_a4 = '3-U-N-I-H-G-F-E-D-C-B-A-z-y-s-r-q-p-i-a-x********************'
regla_a5 = '3-U-P-O-Ñ-N-M-L-K-J-I-H-G-A-z-y-x-p-i-a-F********************'
regla_a6 = '3-X-W-V-U-T-S-R-Q-P-O-Ñ-I-H-G-F-x-p-i-a-N********************'
regla_a7 = '6-5-4-3-2-1-Z-Y-X-W-V-P-O-Ñ-N-F-x-p-i-a-U********************'
regla_a8 = '0-9-8-7-6-5-4-X-W-V-U-N-F-x-p-i-a-3*****************'
regla_a = regla_a8 + regla_a7 + regla_a6 + regla_a5 + regla_a4 + regla_a3 + regla_a2 + regla_a1 + '+++++++'

#Reglas casilla b:
regla_b1 = '4-V-Ñ-G-y-q-n-m-k-j-i-h-g-f-e-d-c-a-b******************'
regla_b2 = '4-V-Ñ-G-y-u-t-r-q-p-o-ñ-n-m-l-k-i-f-e-c-b-a-j**********************'
regla_b3 = '4-V-Ñ-G-C-B-z-y-x-w-v-u-t-s-r-p-n-m-k-j-i-b-q**********************'
regla_b4 = '4-V-Ñ-K-J-H-G-F-E-D-C-B-A-z-x-u-t-r-q-p-j-b-y**********************'
regla_b5 = '4-V-R-Q-O-Ñ-N-M-L-K-J-I-H-F-C-B-z-y-x-q-j-b-G**********************'
regla_b6 = '4-Z-Y-W-V-U-T-S-R-Q-P-O-N-K-J-H-G-F-y-q-j-b-Ñ**********************'
regla_b7 = '8-7-5-4-3-2-1-Z-Y-X-W-U-R-Q-O-Ñ-N-G-y-q-j-b-V**********************'
regla_b8 = '0-9-8-7-6-5-3-Z-Y-W-V-U-Ñ-G-y-q-j-b-4******************'
regla_b = regla_b8 + regla_b7 + regla_b6 + regla_b5 + regla_b4 + regla_b3 + regla_b2 + regla_b1 + '+++++++'

#Reglas casilla c:
regla_c1 = '5-W-O-H-z-r-ñ-n-m-l-k-j-i-h-g-f-e-d-b-a-c********************'
regla_c2 = '5-W-O-H-z-v-u-t-s-r-q-p-o-ñ-n-m-l-j-i-g-f-e-d-c-b-a-k**************************'
regla_c3 = '5-W-O-H-D-C-B-A-z-y-x-w-v-u-r-s-q-p-ñ-n-m-l-k-j-i-c-r**************************'
regla_c4 = '5-W-O-L-K-J-I-H-G-F-E-D-C-B-A-y-x-v-u-t-s-r-q-p-k-c-z**************************'
regla_c5 = '5-W-S-R-Q-P-O-Ñ-N-M-L-K-J-I-G-F-D-C-B-A-z-y-x-r-k-c-H**************************'
regla_c6 = '5-1-Z-Y-X-W-V-U-T-S-R-Q-P-Ñ-N-L-K-J-I-H-G-F-z-r-k-c-O**************************'
regla_c7 = '9-8-7-6-5-4-3-2-1-Z-Y-X-V-U-S-R-Q-P-O-Ñ-N-H-z-r-k-c-W**************************'
regla_c8 = '0-9-8-7-6-4-3-1-Z-Y-X-W-V-U-O-H-z-r-k-c-5********************'
regla_c = regla_c8 + regla_c7 + regla_c6 + regla_c5 + regla_c4 + regla_c3 + regla_c2 + regla_c1 + '+++++++'

#Reglas casilla d:
regla_d1 = '6-X-P-I-A-s-ñ-n-l-k-i-h-g-f-e-c-b-a-d******************'
regla_d2 = '6-X-P-I-A-v-u-s-r-p-o-ñ-n-m-k-j-i-g-f-d-c-a-l**********************'
regla_d3 = '6-X-P-I-D-C-A-z-x-w-v-u-t-r-q-p-ñ-n-l-k-i-d-s**********************'
regla_d4 = '6-X-P-L-K-I-H-F-E-D-C-B-z-y-x-v-u-s-r-p-l-d-A**********************'
regla_d5 = '6-X-S-R-P-O-N-M-L-K-J-H-G-F-D-C-A-z-x-s-l-d-I**********************'
regla_d6 = '6-1-Z-X-W-U-T-S-R-Q-O-Ñ-N-L-K-I-H-F-A-s-l-d-P**********************'
regla_d7 = '9-8-6-5-3-2-1-Z-Y-W-V-U-S-R-P-O-N-I-A-s-l-d-X**********************'
regla_d8 = '0-9-8-7-5-4-3-1-Z-X-W-U-P-I-A-s-l-d-6******************'
regla_d = regla_d8 + regla_d7 + regla_d6 + regla_d5 + regla_d4 + regla_d3 + regla_d2 + regla_d1 + '+++++++'

#Reglas casilla e:
regla_e1 = '7-Y-Q-J-B-t-o-n-m-k-j-h-g-f-d-c-b-a-e******************'
regla_e2 = '7-Y-Q-J-B-w-u-t-r-q-o-ñ-n-l-k-j-i-h-f-r-c-b-m**********************'
regla_e3 = '7-Y-Q-J-E-C-B-z-y-w-v-u-s-r-q-p-o-n-m-k-j-e-t**********************'
regla_e4 = '7-Y-Q-M-K-J-H-G-E-D-C-A-z-y-x-w-u-t-r-q-m-e-B**********************'
regla_e5 = '7-Y-T-R-Q-O-Ñ-M-L-K-I-H-G-F-E-C-B-z-y-t-m-e-J**********************'
regla_e6 = '7-2-Z-Y-W-V-T-S-R-P-O-Ñ-N-M-K-J-H-G-B-t-m-e-Q**********************'
regla_e7 = '0-8-7-5-4-2-1-Z-X-W-V-U-T-R-Q-O-Ñ-J-B-t-m-e-Y**********************'
regla_e8 = '0-9-8-6-5-4-3-2-Z-Y-W-V-Q-J-B-t-m-e-7******************'
regla_e = regla_e8 + regla_e7 + regla_e6 + regla_e5 + regla_e4 + regla_e3 + regla_e2 + regla_e1 + '+++++++'

#Reglas casilla f:
regla_f1 = '8-Z-R-K-C-u-o-ñ-n-m-l-k-j-h-g-e-d-c-b-a-f********************'
regla_f2 = '8-Z-R-K-C-w-v-u-t-s-r-q-o-ñ-m-l-k-j-i-h-g-f-e-d-c-b-n**************************'
regla_f3 = '8-Z-R-K-E-D-C-B-A-z-y-w-v-t-s-r-q-p-o-ñ-n-m-l-k-j-f-u**************************'
regla_f4 = '8-Z-R-M-L-K-J-I-H-G-E-D-B-A-z-y-x-w-v-u-t-s-r-q-n-f-C**************************'
regla_f5 = '8-Z-T-S-R-Q-P-O-Ñ-M-L-J-I-H-G-F-E-D-C-B-A-z-y-u-n-f-K**************************'
regla_f6 = '8-2-1-Z-Y-X-W-V-T-S-Q-P-O-Ñ-N-M-L-K-J-I-H-G-C-u-n-f-R**************************'
regla_f7 = '0-9-8-7-6-5-4-2-1-Y-X-W-V-U-T-S-R-Q-P-O-Ñ-K-C-u-n-f-Z**************************'
regla_f8 = '0-9-7-6-5-4-3-2-1-Z-Y-X-W-V-R-K-C-u-n-f-8********************'
regla_f = regla_f8 + regla_f7 + regla_f6 + regla_f5 + regla_f4 + regla_f3 + regla_f2 + regla_f1 + '+++++++'

#Reglas casilla g:
regla_g1 = '9-1-S-L-D-v-o-ñ-n-l-k-h-f-e-d-c-b-a-g******************'
regla_g2 = '9-1-S-L-D-w-v-u-s-r-o-n-m-l-k-j-i-h-g-f-d-c-ñ**********************'
regla_g3 = '9-1-S-L-E-D-C-A-z-w-u-t-s-r-q-p-o-ñ-n-l-k-g-v**********************'
regla_g4 = '9-1-S-M-L-K-I-H-E-C-B-A-z-y-x-w-v-u-s-r-ñ-g-D**********************'
regla_g5 = '9-1-T-S-R-P-O-M-K-J-I-H-G-F-E-D-C-A-z-v-ñ-g-L**********************'
regla_g6 = '9-2-1-Z-X-W-T-R-Q-P-O-Ñ-N-M-L-K-I-H-D-v-ñ-g-S**********************'
regla_g7 = '0-9-8-6-5-2-Z-Y-X-W-V-U-T-S-R-P-O-L-D-v-ñ-g-1**********************'
regla_g8 = '0-8-7-6-5-4-3-2-1-Z-X-W-S-L-D-v-ñ-g-9******************'
regla_g = regla_g8 + regla_g7 + regla_g6 + regla_g5 + regla_g4 + regla_g3 + regla_g2 + regla_g1 + '+++++++'

#Reglas casilla h:
regla_h1 = '0-2-T-M-E-w-o-ñ-n-m-g-f-e-d-c-b-a-h*****************'
regla_h2 = '0-2-T-M-E-w-v-u-t-ñ-n-m-l-k-j-i-h-g-f-e-o********************'
regla_h3 = '0-2-T-M-E-D-C-B-v-u-t-s-r-q-p-o-ñ-n-m-h-w********************'
regla_h4 = '0-2-T-M-L-K-J-D-C-B-A-z-y-x-w-v-u-t-o-h-E********************'
regla_h5 = '0-2-T-S-R-Q-L-K-J-I-H-G-F-E-D-C-B-w-o-h-M********************'
regla_h6 = '0-2-1-Z-Y-S-R-Q-P-O-Ñ-N-M-L-K-J-E-w-o-h-T********************'
regla_h7 = '0-9-8-7-1-Z-Y-X-W-V-U-T-S-R-Q-M-E-w-o-h-2********************'
regla_h8 = '9-8-7-6-5-4-3-2-1-Z-Y-T-M-E-w-o-h-0*****************'
regla_hh = 'T-M-E-w-***'
regla_h = regla_h8 + regla_h7 + regla_h6 + regla_h5 + regla_h4 + regla_h3 + regla_h2 + regla_h1 + '+++++++'

#Pruebas concatenación de reglas:
prueba1 = regla_d + regla_c + regla_b + regla_a + '***'
prueba2 = regla_h + regla_g + regla_f + regla_e + '***'

#Reglas finales:
regla = regla_h + regla_g + regla_f + regla_e + regla_d + regla_c + regla_b + regla_a + '*******'
regla_final = regla + regla_hh + '*'

rprueba = string2Tree(regla_final)
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
print(len(dic_final))
lista = lista_true(dic_final)
print('')
print('Lista letras con true:', lista)


"""graficando con pygame"""
#Creando la pantalla
ancho = 500 
alto = 600
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Proyecto Lógica II")
condicion = False


#Colores
background_color = (255, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#Posiciones correspondientes para cualquier numero en cada casilla
pos_a = (ancho*3/6, alto/8)
pos_b = (ancho/6, alto*3/8)
pos_c = (ancho*3/6, alto*3/8)
pos_d = (ancho*5/6, alto*3/8)
pos_e = (ancho/6, alto*5/8)
pos_f = (ancho*3/6, alto*5/8)
pos_g = (ancho*5/6, alto*5/8)
pos_h = (ancho*3/6, alto*7/8)


#Inicializando tipo de fuente, definiendo tipo de letra y tamaño
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 64)


#Definiendo los números del 1 al 8
for i in range(1,9):
	exec('text{} = font.render("{}", True, black, white)'.format(i, str(i)))

for n in range(1,9):
	exec('textRect{} = text{}.get_rect()'.format(n, n))


def pos_num(lista, letras):
#optinen una asignacion para cada numero en su respectva casilla que depende de la lista de entrada
	letras_aux = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	count = 0
	for q in lista:
		for x in letras:
			if q == x:
				count = letras.index(x)
				letra = (count%8) 	   #columna
				numero = (count//8)+1  #fila
				exec('textRect{}.center = pos_{}'.format(numero, letras_aux[letra])) 


pos_num(lista, letras)


#Inicializando Pygame
pygame.init()

while not condicion:
   
    #Cerrando el programa cuando se pulsa la x de salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #Rellenando el fondo de la pantalla
    screen.fill(background_color)
    
    #Líneas horizontales
    pygame.draw.line(screen, black, (ancho/3, 0), (2*ancho/3, 0))
    pygame.draw.line(screen, black, (0, alto/4), (ancho, alto/4))
    pygame.draw.line(screen, black, (0, 2*alto/4), (ancho, 2*alto/4))
    pygame.draw.line(screen, black, (0, 3*alto/4), (ancho, 3*alto/4))
    pygame.draw.line(screen, black, (ancho/3, alto-1), (2*ancho/3, alto-1))
    
    #Líneas verticales
    pygame.draw.line(screen, black, (0, alto/4), (0, 3*alto/4))
    pygame.draw.line(screen, black, (ancho/3, 0), (ancho/3, alto))
    pygame.draw.line(screen, black, (2*ancho/3, 0), (2*ancho/3, alto))
    pygame.draw.line(screen, black, (ancho-1, alto/4), (ancho-1, 3*alto/4))
   
    #Números
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    screen.blit(text5, textRect5)
    screen.blit(text6, textRect6)
    screen.blit(text7, textRect7)
    screen.blit(text8, textRect8)
    
    pygame.display.flip()
    pygame.display.update()























