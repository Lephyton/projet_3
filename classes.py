"""MacGyver game classes"""

import pygame
import random
from pygame.locals import * 

from constants import *

class Level:

    """
    classe for reading and displaying the maze and all
    the elements inside:(Macgyver, keeper, objects).
    """
    def __init__(self, wall, macg, keep, floor, gift_1, gift_2, gift_3):
        self.structure = 0
        self.wall = pygame.transform.scale2x(pygame.image.load(img_wall).convert())
        self.macg =pygame.image.load(img_start).convert()
        self.keep = pygame.image.load(img_end).convert()
        self.floor = pygame.transform.scale2x(pygame.image.load(img_back).convert())
        self.gift_1  = pygame.image.load(img_object_1).convert() 
        self.gift_2  = pygame.image.load(img_object_2).convert()
        self.gift_3  = pygame.image.load(img_object_3).convert()

    def read_lab (self):
       
        #reading maze file
        with open('lab.txt', 'r') as fic :
            data = fic.readlines()
            fic.close()
        for i in enumerate(data):
            data[i] = list(data[i])
        self.data = data 

    def show_lab (self, window):

        #loads maze from the file lab.txt
        num_ligne = 0
        for ligne in self.data:
            num_case = 0
            for sprite in ligne:
                #Have calculated the actual position in pixels
                x = num_case * size_sprite
                y = num_ligne * size_sprite
                #X = Macgaver, # = wall, (A,B,C) = objects, O = Keeper " " = floor 
                maping_sprites = {"X": self.macg, "#": self.wall, "A": self.gift_2, "B": self.gift_1, "C": self.gift_3, "O": self.keep, " ": self.floor  }
                if sprite in maping_sprites:
                    window.blit(self.floor,(x,y))
                    window.blit(maping_sprites[sprite],(x,y))
                num_case += 1
            num_ligne += 1
        pygame.display.flip()

    def show_elemt(self, window):   
        #function to display objects randomly 
        gifts = {0:"A", 1:"B", 2:"C"}  
        i = 0
        while i < 3:
            x_rand = random.randint(1, (len(self.data)-1))
            y_rand = random.randint(1, (len(self.data)-1))
            if self.data[y_rand ][x_rand] == " ":
                self.data[y_rand][x_rand] = gifts[i]
                i +=1


class Order:

    """move management class and end conditions check"""
    num_ob = 0 #counter of objects

    def order_move (self, data, pos_perso, choice):

        #motion control function
        new_pos = [pos_perso[0], pos_perso[1]]
        if choice == "H" :
            new_pos= [new_pos[0], new_pos[1] -1]
        elif choice == "B" :
            new_pos  = [ new_pos[0], new_pos[1] +1]
        elif choice == "G":
            new_pos =  [new_pos[0] -1, new_pos[1]]
        elif choice == "J" :
            new_pos =  [new_pos[0] +1, new_pos[1]]
        dep = self.verif_order(data, new_pos[0], new_pos[1])
        if dep == False:
            print("déplacement impossible")
            return pos_perso
        return new_pos

    def verif_order(self, data, pos_col, pos_ligne):

        """
        function of verification of movements 
        and collection of objects
        """
        n_cols = len(data[0])
        n_lignes = len(data)
        if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
            return False
        elif data[pos_ligne][pos_col] in ["A", "B", "C"]:
            data[pos_ligne][pos_col] = " "
            self.num_ob += 1
            return True  
        elif data[pos_ligne][pos_col] == "O":
            return True  
        elif data[pos_ligne][pos_col] != " " :
            return False
        else :
            return True

    def player_choice (self):
        """
        recovery and verification of the player's choice
        """
        choice = input("Entrer votre choix : H = haut, B = bas, G = gauche, J = droite : ")
        while len(choice)!= 1 or choice not in ["H", "B", "G", "J"] :
            print ("Vous n'avez pas fait un bon choix, faite un choix ")
            choice = input("Entrer à nouveau votre choix : H = haut, B = bas, G = gauche, J = droite :")
        return choice

 
    def game_over (self, data, pos_col, pos_ligne):

        """
        check the condition of end of the game: if all 
        the objects are collected and Macgyver presents himself to 
        the goalkeeper he wins if he does not lose
        """
        if data[pos_col][pos_ligne] == "O" :
            if self.num_ob == 3 :
                print("Bravoooo !!!! vous avez gagné et vous avez : " + str(self.num_ob )+ " objets")
                return True
            else:
                print("Désolé !!!! vous avez perdu et vous avez seulement : " + str(self.num_ob)+ " objets")
                return True
        return False
 
   