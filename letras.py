# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:00:41 2019

@author: manua
"""

def codificar():
    filas = [1, 2, 3, 4, 5, 6, 7, 8]
    columnas = [1, 2, 3, 4, 5, 6, 7, 8]
    letras = [chr(256+i) for i in range (len(filas)*len(columnas))]
    return letras

def decodificar(n):
    numero = ord(n)
    num = numero - 256
    m = num % 8
    columna = m+1
    fila = (num//8)+1
    return columna,fila

Letras = codificar()
print(Letras)

prueba = decodificar('Ĉ')
print(prueba)
