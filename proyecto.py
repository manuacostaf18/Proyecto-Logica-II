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

regla2 = "g8-f8-e8-d8-c8-b8-a8-yyyyyyh8>g7-f7-e7-d7-c7-b7-a7-yyyyyyh7>g6-f6-e6-d6-c6-b6-a6-yyyyyyh6>g5-f5-e5-d5-c5-b5-a5-yyyyyyh5>g4-f4-e4-d4-c4-b4-a4-yyyyyyh4>g3-f3-e3-d3-c3-b3-a3-yyyyyyh3>g2-f2-e2-d2-c2-b2-a2-yyyyyyh2>g1-f1-e1-d1-c1-b1-a1-yyyyyyh1>yyyyyyyh8-f8-e8-d8-c8-b8-a8-yyyyyyg8>h7-f7-e7-d7-c7-b7-a7-yyyyyyg7>h6-f6-e6-d6-c6-b6-a6-yyyyyyg6>h5-f5-e5-d5-c5-b5-a5-yyyyyyg5>h4-f4-e4-d4-c4-b4-a4-yyyyyyg4>h3-f3-e3-d3-c3-b3-a3-yyyyyyg3>h2-f2-e2-d2-c2-b2-a2-yyyyyyg2>h1-f1-e1-d1-c1-b1-a1-yyyyyyg1>yyyyyyyh8-g8-e8-d8-c8-b8-a8-yyyyyyf8>h7-g7-e7-d7-c7-b7-a7-yyyyyyf7>h6-g6-e6-d6-c6-b6-a6-yyyyyyf6>h5-g5-e5-d5-c5-b5-a5-yyyyyyf5>h4-g4-e4-d4-c4-b4-a4-yyyyyyf4>h3-g3-e3-d3-c3-b3-a3-yyyyyyf3>h2-g2-e2-d2-c2-b2-a2-yyyyyyf2>h1-g1-e1-d1-c1-b1-a1-yyyyyyf1>yyyyyyyh8-g8-f8-d8-c8-b8-a8-yyyyyye8>h7-g7-f7-d7-c7-b7-a7-yyyyyye7>h6-g6-f6-d6-c6-b6-a6-yyyyyye6>h5-g5-f5-d5-c5-b5-a5-yyyyyye5>h4-g4-f4-d4-c4-b4-a4-yyyyyye4>h3-g3-f3-d3-c3-b3-a3-yyyyyye3>h2-g2-f2-d2-c2-b2-a2-yyyyyye2>h1-g1-f1-d1-c1-b1-a1-yyyyyye1>yyyyyyyh8-g8-f8-e8-c8-b8-a8-yyyyyyd8>h7-g7-f7-e7-c7-b7-a7-yyyyyyd7>h6-g6-f6-e6-c6-b6-a6-yyyyyyd6>h5-g5-f5-e5-c5-b5-a5-yyyyyyd5>h4-g4-f4-e4-c4-b4-a4-yyyyyyd4>h3-g3-f3-e3-c3-b3-a3-yyyyyyd3>h2-g2-f2-e2-c2-b2-a2-yyyyyyd2>h1-g1-f1-e1-c1-b1-a1-yyyyyyd1>yyyyyyyh8-g8-f8-e8-d8-b8-a8-yyyyyyc8>h7-g7-f7-e7-d7-b7-a7-yyyyyyc7>h6-g6-f6-e6-d6-b6-a6-yyyyyyc6>h5-g5-f5-e5-d5-b5-a5-yyyyyyc5>h4-g4-f4-e4-d4-b4-a4-yyyyyyc4>h3-g3-f3-e3-d3-b3-a3-yyyyyyc3>h2-g2-f2-e2-d2-b2-a2-yyyyyyc2>h1-g1-f1-e1-d1-b1-a1-yyyyyyc1>yyyyyyyh8-g8-f8-e8-d8-c8-a8-yyyyyyb8>h7-g7-f7-e7-d7-c7-a7-yyyyyyb7>h6-g6-f6-e6-d6-c6-a6-yyyyyyb6>h5-g5-f5-e5-d5-c5-a5-yyyyyyb5>h4-g4-f4-e4-d4-c4-a4-yyyyyyb4>h3-g3-f3-e3-d3-c3-a3-yyyyyyb3>h2-g2-f2-e2-d2-c2-a2-yyyyyyb2>h1-g1-f1-e1-d1-c1-a1-yyyyyyb1>yyyyyyyh8-g8-f8-e8-d8-c8-b8-yyyyyya8>h7-g7-f7-e7-d7-c7-b7-yyyyyya7>h6-g6-f6-e6-d6-c6-b6-yyyyyya6>h5-g5-f5-e5-d5-c5-b5-yyyyyya5>h4-g4-f4-e4-d4-c4-b4-yyyyyya4>h3-g3-f3-e3-d3-c3-b3-yyyyyya3>h2-g2-f2-e2-d2-c2-b2-yyyyyya2>h1-g1-f1-e1-d1-c1-b1-yyyyyya1>yyyyyyyyyyyyyy"

regla3 = 
