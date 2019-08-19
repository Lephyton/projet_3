"""MacGyver game classes"""

import pygame
import random
from pygame.locals import * 
from constantes import *

class Level:
    def __init__(self):
        self.structure = 0

    def read_lab (self):
        """
        this function loads 
        labirynthe from the file lab.txt
        """
        fic = open('lab.txt', 'r') 
        data = fic.readlines()
        fic.close()
        for i in range(len(data)):
            data[i] = list(data[i])
        self.data = data 

    def show_lab (self, window):
        wall = pygame.image.load(img_wall).convert()
        star = pygame.image.load(img_start).convert()
        end = pygame.image.load(img_end).convert()
        floor = pygame.image.load(img_back).convert()
        num_ligne = 0
        for ligne in self.data:
            num_case = 0
            for sprite in ligne:
                x = num_case * size_sprite
                y = num_ligne * size_sprite
                if sprite == '#':
                    window.blit(wall, (x,y))
                elif sprite == 'X':		
                        window.blit(star, (x,y))
                elif sprite == 'O':		   
                        window.blit(end, (x,y))
                num_case += 1
            num_ligne += 1
        pygame.display.flip()


    def show_elemt(self):
        i = 0
        while i < 3:
            x_rand = random.randint(1, (len(self.data)-1))
            y_rand = random.randint(1, (len(self.data)-1))
            print(x_rand, y_rand )
            if self.data[y_rand ][x_rand] == " ":
                self.data[y_rand][x_rand] = "A"
                i +=1
class Perso:
    num_ob = 2

    def deplacement_perso (self, data, pos_perso, choix):
        new_pos = [pos_perso[0], pos_perso[1]]
        if choix == "H" :
            new_pos= [new_pos[0], new_pos[1] -1]
        elif choix == "B" :
            new_pos  = [ new_pos[0], new_pos[1] +1]
        elif choix == "G":
            new_pos =  [new_pos[0] -1, new_pos[1]]
        elif choix == "J" :
            new_pos =  [new_pos[0] +1, new_pos[1]]
            dep = verification_deplacement(data, new_pos[0], new_pos[1])
        if dep == False:
            print("déplacement impossible")
            return pos_perso
        return new_pos

    def verification_deplacement(self, data, pos_col, pos_ligne):
        global num_ob
        n_cols = len(data[0])
        n_lignes = len(data)
        if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
            return False
        elif data[pos_ligne][pos_col] == "A":
            data[pos_ligne][pos_col] = " "
            num_ob += 1
            return True  
        elif data[pos_ligne][pos_col] == "O":
            return True  

        elif data[pos_ligne][pos_col] != " " :
            return False
        else :
            return True

    def choix_du_joueur (self):
        choix = input("Entrer votre choix : H = haut, B = bas, G = gauche, J = droite : ")
        while len(choix)!= 1 or choix not in ["H", "B", "G", "J"] :
            print ("Vous n'avez pas fait un bon choix, faite un choix ")
            choix = input("Entrer à nouveau votre choix : H = haut, B = bas, G = gauche, J = droite :")
        return choix

 
    def sortie (self, data, pos_col, pos_ligne):
        print(data[pos_col][pos_ligne])
        if data[pos_col][pos_ligne] == "O" :
            if num_ob == 3 :
                print("Bravoooo !!!! vous avez gagné et vous avez : " + str(num_ob )+ " objets")
                return True
            else:
                print("Désolé !!!! vous avez perdu et vous avez seulement : " + str(num_ob )+ " objets")
                return True
        return False
 
   