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

#Inicializando font, definiendo tipo de letra y tamaño
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 64)

#Definiendo los números del 1 al 8
text1 = font.render("1", True, black, white)
text2 = font.render("2", True, black, white)
text3 = font.render("3", True, black, white)
text4 = font.render("4", True, black, white)
text5 = font.render("5", True, black, white)
text6 = font.render("6", True, black, white)
text7 = font.render("7", True, black, white)
text8 = font.render("8", True, black, white)

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect6 = text6.get_rect()
textRect7 = text7.get_rect()
textRect8 = text8.get_rect()

#Función que obtiene la casilla correspondiente a cada número, teniendo en cuenta un diccionario dado
def get_pos(diccionario):
    for n in diccionario:
        if diccionario[n] == 1:
            return n
         
#Diccionarios para cada número, con claves correspondientes a la casilla, y valores correspondientes a si está o no en la casilla        
claves_1 = {'a':0, 'b':0, 'c':1, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
claves_2 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':1}
claves_3 = {'a':0, 'b':0, 'c':0, 'd':1, 'e':0, 'f':0, 'g':0, 'h':0}
claves_4 = {'a':0, 'b':1, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
claves_5 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':1, 'h':0}
claves_6 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':1, 'f':0, 'g':0, 'h':0}
claves_7 = {'a':1, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
claves_8 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':1, 'g':0, 'h':0}

#Posiciones correspondientes a cada número        
p1 = get_pos(claves_1)
p2 = get_pos(claves_2)
p3 = get_pos(claves_3)
p4 = get_pos(claves_4)
p5 = get_pos(claves_5)
p6 = get_pos(claves_6)
p7 = get_pos(claves_7)
p8 = get_pos(claves_8)

#Posicionando el número 1
if p1 =='a':
    textRect1.center = pos_a
elif p1 == 'b':
    textRect1.center = pos_b
elif p1 == 'c':
    textRect1.center = pos_c
elif p1 == 'd':
    textRect1.center = pos_d
elif p1 == 'e':
    textRect1.center = pos_e
elif p1 == 'f':
    textRect1.center = pos_f
elif p1 == 'g':
    textRect1.center = pos_g
elif p1 == 'h':
    textRect1.center = pos_h
    
#Posicionando el número 2
if p2 =='a':
    textRect2.center = pos_a
elif p2 == 'b':
    textRect2.center = pos_b
elif p2 == 'c':
    textRect2.center = pos_c
elif p2 == 'd':
    textRect2.center = pos_d
elif p2 == 'e':
    textRect2.center = pos_e
elif p2 == 'f':
    textRect2.center = pos_f
elif p2 == 'g':
    textRect2.center = pos_g
elif p2 == 'h':
    textRect2.center = pos_h
    
#Posicionando el número 3
if p3 =='a':
    textRect3.center = pos_a
elif p3 == 'b':
    textRect3.center = pos_b
elif p3 == 'c':
    textRect3.center = pos_c
elif p3 == 'd':
    textRect3.center = pos_d
elif p3 == 'e':
    textRect3.center = pos_e
elif p3 == 'f':
    textRect3.center = pos_f
elif p3 == 'g':
    textRect3.center = pos_g
elif p3 == 'h':
    textRect3.center = pos_h
    
#Posicionando el número 4
if p4 =='a':
    textRect4.center = pos_a
elif p4 == 'b':
    textRect4.center = pos_b
elif p4 == 'c':
    textRect4.center = pos_c
elif p4 == 'd':
    textRect4.center = pos_d
elif p4 == 'e':
    textRect4.center = pos_e
elif p4 == 'f':
    textRect4.center = pos_f
elif p4 == 'g':
    textRect4.center = pos_g
elif p4 == 'h':
    textRect4.center = pos_h
    
#Posicionand el número 5
if p5 =='a':
    textRect5.center = pos_a
elif p5 == 'b':
    textRect5.center = pos_b
elif p5 == 'c':
    textRect5.center = pos_c
elif p5 == 'd':
    textRect5.center = pos_d
elif p5 == 'e':
    textRect5.center = pos_e
elif p5 == 'f':
    textRect5.center = pos_f
elif p5 == 'g':
    textRect5.center = pos_g
elif p5 == 'h':
    textRect5.center = pos_h
    
#Posicionando el número 6
if p6 =='a':
    textRect6.center = pos_a
elif p6 == 'b':
    textRect6.center = pos_b
elif p6 == 'c':
    textRect6.center = pos_c
elif p6 == 'd':
    textRect6.center = pos_d
elif p6 == 'e':
    textRect6.center = pos_e
elif p6 == 'f':
    textRect6.center = pos_f
elif p6 == 'g':
    textRect6.center = pos_g
elif p6 == 'h':
    textRect6.center = pos_h
    
#Posicionando el número 7
if p7 =='a':
    textRect7.center = pos_a
elif p7 == 'b':
    textRect7.center = pos_b
elif p7 == 'c':
    textRect7.center = pos_c
elif p7 == 'd':
    textRect7.center = pos_d
elif p7 == 'e':
    textRect7.center = pos_e
elif p7 == 'f':
    textRect7.center = pos_f
elif p7 == 'g':
    textRect7.center = pos_g
elif p7 == 'h':
    textRect7.center = pos_h

#Posicionando el número 8
if p8 =='a':
    textRect8.center = pos_a
elif p8 == 'b':
    textRect8.center = pos_b
elif p8 == 'c':
    textRect8.center = pos_c
elif p8 == 'd':
    textRect8.center = pos_d
elif p8 == 'e':
    textRect8.center = pos_e
elif p8 == 'f':
    textRect8.center = pos_f
elif p8 == 'g':
    textRect8.center = pos_g
elif p8 == 'h':
    textRect8.center = pos_h

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
    pygame.draw.line(screen, black, (500/3, 0), (1000/3, 0))
    pygame.draw.line(screen, black, (0, 600/4), (500, 600/4))
    pygame.draw.line(screen, black, (0, 1200/4), (500, 1200/4))
    pygame.draw.line(screen, black, (0, 1800/4), (500, 1800/4))
    pygame.draw.line(screen, black, (500/3, 599), (1000/3, 599))
    
    #Líneas verticales
    pygame.draw.line(screen, black, (0, 600/4), (0, 1800/4))
    pygame.draw.line(screen, black, (500/3, 0), (500/3, 600))
    pygame.draw.line(screen, black, (1000/3, 0), (1000/3, 600))
    pygame.draw.line(screen, black, (499, 600/4), (499, 1800/4))
   
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
