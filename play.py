#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Game help MacGyver to escape
in this Game MacGyver must find through a labyrinth three objects before presenting himself to the keeper.
python script 
files : play.py, classes.py, constants.py, lab.txt and images folder

"""


import random 
import pygame 
from pygame.locals import *

from classes import *
from constants import *

pygame.init()

window = pygame.display.set_mode((size_window, size_window))
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(title)

level = Level()
level.read_lab()
level.show_elemt(window)
perso = Perso()
level.data[0][0] = "X"
pos_perso = [0,0]

continuer = True
while continuer :
    level.show_lab (window)
    choix = " "
    event = pygame.event.wait()
    print(event)
    if event.type == QUIT :
        continuer = False  
    if not event.type == KEYDOWN:
        continue
    if event.key == K_RIGHT:
        choix = "J"
    if event.key == K_LEFT:
        choix = "G"
    if event.key == K_UP:
        choix = "H"
    if event.key == K_DOWN:
        choix = "B"
    print(choix)

    new_pos = perso.deplacement_perso(level.data, pos_perso, choix)
    if perso.sortie(level.data, new_pos[1], new_pos[0]):
        continuer = False
    level.data[pos_perso[1]][pos_perso[0]] = " "
    level.data[new_pos[1]][new_pos[0]] = "X"
    pos_perso = new_pos
    print(perso.num_ob)

   
   

