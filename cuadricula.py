# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:03:57 2019

@author: manua
"""

import pygame

#Creando la pantalla
ancho = 500 
alto = 600
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Proyecto Lógica II")

#Medidas para el posicionamiento de los números
anchito = ancho/6
altico = alto/8

#Condición para el funcionamiento de Pygame
condicion = False

#Colores
background_color = (255, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#Posiciones correspondientes al centro de cada cuadrícula
pos_a = (anchito*3, altico)
pos_b = (anchito, altico*3)
pos_c = (anchito*3, altico*3)
pos_d = (anchito*5, altico*3)
pos_e = (anchito, altico*5)
pos_f = (anchito*3, altico*5)
pos_g = (anchito*5, altico*5)
pos_h = (anchito*3, altico*7)
     
#Diccionarios para cada número, con claves correspondientes a la casilla, y valores correspondientes a si está o no en la casilla        
claves_1 = {'a':0, 'b':0, 'c':1, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
claves_2 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':1}
claves_3 = {'a':0, 'b':0, 'c':0, 'd':1, 'e':0, 'f':0, 'g':0, 'h':0}
claves_4 = {'a':0, 'b':1, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
claves_5 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':1, 'h':0}
claves_6 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':1, 'f':0, 'g':0, 'h':0}
claves_7 = {'a':1, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
claves_8 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':1, 'g':0, 'h':0}


#Inicializando font, definiendo tipo de letra y tamaño
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 64)

#Definiendo los números del 1 al 8
for i in range(1,9):
	exec('text{} = font.render("{}", True, black, white)'.format(i, str(i)))

for n in range(1,9):
	exec('textRect{} = text{}.get_rect()'.format(n, n))
	

#posicionando numeros
def pos_num(dic, num):
	for q in dic:
		if dic[q] == 1:
			letra = q
	if letra =='a':
	    exec('textRect{}.center = pos_a'.format(num))
	elif letra == 'b':
		exec('textRect{}.center = pos_b'.format(num))
	elif letra == 'c':
	    exec('textRect{}.center = pos_c'.format(num))
	elif letra == 'd':
	    exec('textRect{}.center = pos_d'.format(num))
	elif letra == 'e':
	    exec('textRect{}.center = pos_e'.format(num))
	elif letra == 'f':
	    exec('textRect{}.center = pos_f'.format(num))
	elif letra == 'g':
	    exec('textRect{}.center = pos_g'.format(num))
	elif letra == 'h':
	    exec('textRect{}.center = pos_h'.format(num))
	return 'texRect{}.center'.format(num)

pos_num(claves_1, 1)
pos_num(claves_2, 2)
pos_num(claves_3, 3)
pos_num(claves_4, 4)
pos_num(claves_5, 5)
pos_num(claves_6, 6)
pos_num(claves_7, 7)
pos_num(claves_8, 8)

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
