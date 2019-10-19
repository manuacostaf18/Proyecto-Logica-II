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
regla1 = "h7-h6-h5-h4-h3-h2-h1-yyyyyyh8>h8-h6-h5-h4-h3-h2-h1-yyyyyyh7>h8-h7-h5-h4-h3-h2-h1-yyyyyyh6>h8-h7-h6-h4-h3-h2-h1-yyyyyyh5>h8-h7-h6-h5-h3-h2-h1-yyyyyyh4>h8-h7-h6-h5-h4-h2-h1-yyyyyyh3>h8-h7-h6-h5-h4-h3-h1-yyyyyyh2>h8-h7-h6-h5-h4-h3-h2-yyyyyyh1>g7-g6-g5-g4-g3-g2-g1-yyyyyyg8>g8-g6-g5-g4-g3-g2-g1-yyyyyyg7>g8-g7-g5-g4-g3-g2-g1-yyyyyyg6>g8-g7-g6-g4-g3-g2-g1-yyyyyyg5>g8-g7-g6-g5-g3-g2-g1-yyyyyyg4>g8-g7-g6-g5-g4-g2-g1-yyyyyyg3>g8-g7-g6-g5-g4-g3-g1-yyyyyyg2>g8-g7-g6-g5-g4-g3-g2-yyyyyyg1>f7-f6-f5-f4-f3-f2-f1-yyyyyyf8>f8-f6-f5-f4-f3-f2-f1-yyyyyyf7>f8-f7-f5-f4-f3-f2-f1-yyyyyyf6>f8-f7-f6-f4-f3-f2-f1-yyyyyyf5>f8-f7-f6-f5-f3-f2-f1-yyyyyyf4>f8-f7-f6-f5-f4-f2-f1-yyyyyyf3>f8-f7-f6-f5-f4-f3-f1-yyyyyyf2>f8-f7-f6-f5-f4-f3-f2-yyyyyyf1>e7-e6-e5-e4-e3-e2-e1-yyyyyye8>e8-e6-e5-e4-e3-e2-e1-yyyyyye7>e8-e7-e5-e4-e3-e2-e1-yyyyyye6>e8-e7-e6-e4-e3-e2-e1-yyyyyye5>e8-e7-e6-e5-e3-e2-e1-yyyyyye4>e8-e7-e6-e5-e4-e2-e1-yyyyyye3>e8-e7-e6-e5-e4-e3-e1-yyyyyye2>e8-e7-e6-e5-e4-e3-e2-yyyyyye1>d7-d6-d5-d4-d3-d2-d1-yyyyyyd8>d8-d6-d5-d4-d3-d2-d1-yyyyyyd7>d8-d7-d5-d4-d3-d2-d1-yyyyyyd6>d8-d7-d6-d4-d3-d2-d1-yyyyyyd5>d8-d7-d6-d5-d3-d2-d1-yyyyyyd4>d8-d7-d6-d5-d4-d2-d1-yyyyyyd3>d8-d7-d6-d5-d4-d3-d1-yyyyyyd2>d8-d7-d6-d5-d4-d3-d2-yyyyyyd1>c7-c6-c5-c4-c3-c2-c1-yyyyyyc8>c8-c6-c5-c4-c3-c2-c1-yyyyyyc7>c8-c7-c5-c4-c3-c2-c1-yyyyyyc6>c8-c7-c6-c4-c3-c2-c1-yyyyyyc5>c8-c7-c6-c5-c3-c2-c1-yyyyyyc4>c8-c7-c6-c5-c4-c2-c1-yyyyyyc3>c8-c7-c6-c5-c4-c3-c1-yyyyyyc2>c8-c7-c6-c5-c4-c3-c2-yyyyyyc1>b7-b6-b5-b4-b3-b2-b1-yyyyyyb8>b8-b6-b5-b4-b3-b2-b1-yyyyyyb7>b8-b7-b5-b4-b3-b2-b1-yyyyyyb6>b8-b7-b6-b4-b3-b2-b1-yyyyyyb5>b8-b7-b6-b5-b3-b2-b1-yyyyyyb4>b8-b7-b6-b5-b4-b2-b1-yyyyyyb3>b8-b7-b6-b5-b4-b3-b1-yyyyyyb2>b8-b7-b6-b5-b4-b3-b2-yyyyyyb1>a7-a6-a5-a4-a3-a2-a1-yyyyyya8>a8-a6-a5-a4-a3-a2-a1-yyyyyya7>a8-a7-a5-a4-a3-a2-a1-yyyyyya6>a8-a7-a6-a4-a3-a2-a1-yyyyyya5>a8-a7-a6-a5-a3-a2-a1-yyyyyya4>a8-a7-a6-a5-a4-a2-a1-yyyyyya3>a8-a7-a6-a5-a4-a3-a1-yyyyyya2>a8-a7-a6-a5-a4-a3-a2-yyyyyya1>yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

regla2 = "g8-f8-e8-d8-c8-b8-a8-yyyyyyh8>g7-f7-e7-d7-c7-b7-a7-yyyyyyh7>g6-f6-e6-d6-c6-b6-a6-yyyyyyh6>g5-f5-e5-d5-c5-b5-a5-yyyyyyh5>g4-f4-e4-d4-c4-b4-a4-yyyyyyh4>g3-f3-e3-d3-c3-b3-a3-yyyyyyh3>g2-f2-e2-d2-c2-b2-a2-yyyyyyh2>g1-f1-e1-d1-c1-b1-a1-yyyyyyh1>h8-f8-e8-d8-c8-b8-a8-yyyyyyg8>h7-f7-e7-d7-c7-b7-a7-yyyyyyg7>h6-f6-e6-d6-c6-b6-a6-yyyyyyg6>h5-f5-e5-d5-c5-b5-a5-yyyyyyg5>h4-f4-e4-d4-c4-b4-a4-yyyyyyg4>h3-f3-e3-d3-c3-b3-a3-yyyyyyg3>h2-f2-e2-d2-c2-b2-a2-yyyyyyg2>h1-f1-e1-d1-c1-b1-a1-yyyyyyg1>h8-g8-e8-d8-c8-b8-a8-yyyyyyf8>h7-g7-e7-d7-c7-b7-a7-yyyyyyf7>h6-g6-e6-d6-c6-b6-a6-yyyyyyf6>h5-g5-e5-d5-c5-b5-a5-yyyyyyf5>h4-g4-e4-d4-c4-b4-a4-yyyyyyf4>h3-g3-e3-d3-c3-b3-a3-yyyyyyf3>h2-g2-e2-d2-c2-b2-a2-yyyyyyf2>h1-g1-e1-d1-c1-b1-a1-yyyyyyf1>h8-g8-f8-d8-c8-b8-a8-yyyyyye8>h7-g7-f7-d7-c7-b7-a7-yyyyyye7>h6-g6-f6-d6-c6-b6-a6-yyyyyye6>h5-g5-f5-d5-c5-b5-a5-yyyyyye5>h4-g4-f4-d4-c4-b4-a4-yyyyyye4>h3-g3-f3-d3-c3-b3-a3-yyyyyye3>h2-g2-f2-d2-c2-b2-a2-yyyyyye2>h1-g1-f1-d1-c1-b1-a1-yyyyyye1>h8-g8-f8-e8-c8-b8-a8-yyyyyyd8>h7-g7-f7-e7-c7-b7-a7-yyyyyyd7>h6-g6-f6-e6-c6-b6-a6-yyyyyyd6>h5-g5-f5-e5-c5-b5-a5-yyyyyyd5>h4-g4-f4-e4-c4-b4-a4-yyyyyyd4>h3-g3-f3-e3-c3-b3-a3-yyyyyyd3>h2-g2-f2-e2-c2-b2-a2-yyyyyyd2>h1-g1-f1-e1-c1-b1-a1-yyyyyyd1>h8-g8-f8-e8-d8-b8-a8-yyyyyyc8>h7-g7-f7-e7-d7-b7-a7-yyyyyyc7>h6-g6-f6-e6-d6-b6-a6-yyyyyyc6>h5-g5-f5-e5-d5-b5-a5-yyyyyyc5>h4-g4-f4-e4-d4-b4-a4-yyyyyyc4>h3-g3-f3-e3-d3-b3-a3-yyyyyyc3>h2-g2-f2-e2-d2-b2-a2-yyyyyyc2>h1-g1-f1-e1-d1-b1-a1-yyyyyyc1>h8-g8-f8-e8-d8-c8-a8-yyyyyyb8>h7-g7-f7-e7-d7-c7-a7-yyyyyyb7>h6-g6-f6-e6-d6-c6-a6-yyyyyyb6>h5-g5-f5-e5-d5-c5-a5-yyyyyyb5>h4-g4-f4-e4-d4-c4-a4-yyyyyyb4>h3-g3-f3-e3-d3-c3-a3-yyyyyyb3>h2-g2-f2-e2-d2-c2-a2-yyyyyyb2>h1-g1-f1-e1-d1-c1-a1-yyyyyyb1>h8-g8-f8-e8-d8-c8-b8-yyyyyya8>h7-g7-f7-e7-d7-c7-b7-yyyyyya7>h6-g6-f6-e6-d6-c6-b6-yyyyyya6>h5-g5-f5-e5-d5-c5-b5-yyyyyya5>h4-g4-f4-e4-d4-c4-b4-yyyyyya4>h3-g3-f3-e3-d3-c3-b3-yyyyyya3>h2-g2-f2-e2-d2-c2-b2-yyyyyya2>h1-g1-f1-e1-d1-c1-b1-yyyyyya1>yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

regla3 = "g7-f7-e7-yyh8>h7-f7-d7-c7-yyyg8>h7-g7-e7-d7-c7-b7-yyyyyf8>h7-f7-c7-b7-yyye8>g7-f7-c7-a7-yyyd8>g7-f7-e7-d7-b7-a7-yyyyyc8>f7-e7-c7-a7-yyyb8>d7-c7-b7-yya8>g8-f8-e8-g6-f6-e6-yyyyyh7>h8-f8-d8-c8-h6-f6-d6-c6-yyyyyyyg7>h8-g8-e8-d8-c8-b8-h6-g6-e6-d6-c6-b6-yyyyyyyyyyyf7>h8-f8-c8-b8-h6-f6-c6-b6-yyyyyyye7>g8-f8-c8-a-g6-f6-c6-a6-yyyyyyyd7>g8-f8-e8-d8-b8-a8-g6-f6-e6-d6-b6-a6-yyyyyyyyyyyc7>f8-e8-c8-a8-f6-e6-c6-a6-yyyyyyyb7>d8-c8-b8-d6-c6-b6-yyyyya7>g7-f7-e7-g5-f5-e5-yyyyyh6>h7-f7-d7-c7-h5-f5-d5-c5-yyyyyyyg6>h7-g7-e7-d7-c7-b7-h5-g5-e5-d5-c5-b5-yyyyyyyyyyyf6>h7-f7-c7-b7-h5-f5-c5-b5-yyyyyyye6>g7-f7-c7-a7-g5-f5-c5-a5-yyyyyyyd6>g7-f7-e7-d7-b7-a7-g5-f5-e5-d5-b5-a5-yyyyyyyyyyyc6>f7-e7-c7-a7-f5-e5-c5-a5-yyyyyyyb6>d7-c7-b7-d5-c5-b5-yyyyya6>g6-f6-e6-g4-f4-e4-yyyyyh5>h6-f6-d6-c6-h4-f4-d4-c4-yyyyyyyg5>h6-g6-e6-d6-c6-b6-h4-g4-e4-d4-c4-b4-yyyyyyyyyyyf5>h6-f6-c6-b6-h4-f4-c4-b4-yyyyyyye5>g6-f6-c6-a6-g4-f4-c4-a4-yyyyyyyd5>g6-f6-e6-d6-b6-a6-g4-f4-e4-d4-b4-a4-yyyyyyyyyyyc5>f6-e6-c6-a6-f4-e4-c4-a4-yyyyyyyb5>d6-c6-b6-d4-c4-b4-yyyyya5>g5-f5-e5-g3-f3-e3-yyyyyh4>h5-f5-d5-c5-h3-f3-d3-c3-yyyyyyyg4>h5-g5-e5-d5-c5-b5-h3-g3-e3-d3-c3-b3-yyyyyyyyyyyf4>h5-f5-c5-b5-h3-f3-c3-b3-yyyyyyye4>g5-f5-c5-a5-g3-f3-c3-a3-yyyyyyyd4>g5-f5-e5-d5-b5-a5-g3-f3-e3-d3-b3-a3-yyyyyyyyyyyc4>f5-e5-c5-a5-f3-e3-c3-a3-yyyyyyyb4>d5-c5-b5-d3-c3-b3-yyyyya4>g4-f4-e4-g2-f2-e2-yyyyyh3>h4-f4-d4-c4-h2-f2-d2-c2-yyyyyyyg3>h4-g4-e4-d4-c4-b4-h2-g2-e2-d2-c2-b2-yyyyyyyyyyyf3>h4-f4-c4-b4-h2-f2-c2-b2-yyyyyyye3>g4-f4-c4-a4-g2-f2-c2-a2-yyyyyyyd3>g4-f4-e4-d4-b4-a4-g2-f2-e2-d2-b2-a2-yyyyyyyyyyyc3>f4-e4-c4-a4-f2-e2-c2-a2-yyyyyyyb3>d4-c4-b4-d2-c2-b2-yyyyya3>g3-f3-e3-g1-f1-e1-yyyyyh2>h3-f3-d3-c3-h1-f1-d1-c1-yyyyyyyg2>h3-g3-e3-d3-c3-b3-h1-g1-e1-d1-c1-b1-yyyyyyyyyyyf2>h3-f3-c3-b3-h1-f1-c1-b1-yyyyyyye2>g3-f3-c3-a3-g1-f1-c1-a1-yyyyyyyd2>g3-f3-e3-d3-b3-a3-g1-f1-e1-d1-b1-a1-yyyyyyyyyyyc2>f3-e3-c3-a3-f1-e1-c1-a1-yyyyyyyb2>d3-c3-b3-d1-c1-b1-yyyyya2>g2-f2-e2-yyh1>h2-f2-d2-c2-yyyg1>h2-g2-e2-d2-c2-b2-yyyyyf1>h2-f2-c2-b2-yyye1>g2-f2-c2-a2-yyyd1>g2-f2-e2-d2-b2-a2-yyyyyc1>f2-e2-c2-a2-yyyb1>d2-c2-b2-yya1>yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

reglas = regla1+regla2+regla3+"yyy"

