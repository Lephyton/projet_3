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


    
def sortie (data, pos_col, pos_ligne):
    print(data[pos_col][pos_ligne])
    if data[pos_col][pos_ligne] == "O" :
        if num_ob == 3 :
            print("Bravoooo !!!! vous avez gagné et vous avez : " + str(num_ob )+ " objets")
            return True
        else:
            print("Désolé !!!! vous avez perdu et vous avez seulement : " + str(num_ob )+ " objets")
            return True
    return False
 






level = Level()
level.read_lab()
level.show_elemt()
perso = Perso()
level.data[1][1] = "X"
pos_perso = [1,1]
continuer = True
while continuer :

    level.show_lab (window)
    choix = perso.choix_du_joueur ()
    new_pos = perso.deplacement_perso(level.data, pos_perso, choix)
    if sortie(level.data, new_pos[1], new_pos[0]):
        continuer = False
    level.data[pos_perso[1]][pos_perso[0]] = " "
    level.data[new_pos[1]][new_pos[0]] = "X"
    pos_perso = new_pos
    print(num_ob)


