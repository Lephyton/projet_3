import random 
import pygame 
from pygame.locals import *
from classes import *
from constantes import *

pygame.init()

window = pygame.display.set_mode((size_window, size_window))
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(title)


   

level = Level()
level.read_lab()
level.show_elemt()
perso = Perso()
level.data[1][1] = "X"
pos_perso = [1,1]

continuer = True
while continuer :
    level.show_lab (window)

    for event in pygame.event.get():
        if event.type == QUIT :
            continuer = False  
    choix = perso.choix_du_joueur ()
    new_pos = perso.deplacement_perso(level.data, pos_perso, choix)
    if sortie(level.data, new_pos[1], new_pos[0]):
        continuer = False
    level.data[pos_perso[1]][pos_perso[0]] = " "
    level.data[new_pos[1]][new_pos[0]] = "X"
    pos_perso = new_pos
    print(num_ob)
   

