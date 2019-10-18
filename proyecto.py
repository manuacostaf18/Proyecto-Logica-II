# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:35:52 2019

@author: manua
"""

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numeros = [str(x) for x in range(1, 9)]

def crearLetras():
    lista = []
    for n in letras:
        for x in numeros:
            lista.append(n+x)
    return lista

letrasProposicionales = crearLetras()
print(letrasProposicionales)

conectivosBinarios = ["y","o",">"]

class Tree():
    def __init__(self,label,iz,der):
        self.label = label
        self.left = iz
        self.right = der

def Vi(f,I):
    if f.right == None:
        return I[f.label]
    elif f.label == '-':
        return 1 - Vi(f.right,I)
    elif f.label == 'y':
        return Vi(f.left,I)*Vi(f.right,I)
    elif f.label == 'o':
        return max([Vi(f.left,I),Vi(f.right,I)])
    elif f.label == '>':
        return max([1 - Vi(f.left,I),Vi(f.right,I)])
    elif f.label == '<->':
        return 1 - (Vi(f.left,I) - Vi(f.right,I))**2

def string2Tree(A):
    conectivos = ["y","o",">"]
    stack = []
    for c in A:
        if c in letrasProposicionales:
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
    if arbol.label in letrasProposicionales:
        return arbol.label
    elif arbol.label == "-":
        return arbol.label+Inorder(arbol.right)
    elif arbol.label in conectivosBinarios:
        return "("+Inorder(arbol.left)+arbol.label+Inorder(arbol.right)+")"
    else:
        print("Oops, rotulo incorrecto")
        
        
#Reglas escritas en polaco inverso 
regla1 = 

regla2 = 

regla3 = 