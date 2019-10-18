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

#Posicionando los números en cada una de las cuadrículas
textRect1.center = pos_c
textRect2.center = pos_h
textRect3.center = pos_d
textRect4.center = pos_b
textRect5.center = pos_g
textRect6.center = pos_e
textRect7.center = pos_a
textRect8.center = pos_f

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
