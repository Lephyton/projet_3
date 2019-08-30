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


def main():
    # pygame initialization
    pygame.init()

    # Open the Pygame window
    window = pygame.display.set_mode((SISE_WINDOW, SISE_WINDOW))

    # Icon
    icon = pygame.image.load(IMAGE_ICONE)
    pygame.display.set_icon(icon)

    # title
    pygame.display.set_caption(TITLE)

    level = Level()
    level.read_lab()
    level.show_elemt(window)
    order = Order()
    level.data[0][0] = "X"
    pos_perso = [0, 0]

    play = True
    # Main loop
    while play:
        level.show_lab(window)
        choice = " "
        event = pygame.event.wait()
        print(event)
        if event.type == QUIT:
            play = False
        if not event.type == KEYDOWN:
            continue
        if event.key == K_RIGHT:
            choice = "J"
        if event.key == K_LEFT:
            choice = "G"
        if event.key == K_UP:
            choice = "H"
        if event.key == K_DOWN:
            choice = "B"
        print(choice)
        new_pos = order.order_move(level.data, pos_perso, choice)
        if order.game_over(level.data, new_pos[1], new_pos[0]):
            play = False
        level.data[pos_perso[1]][pos_perso[0]] = " "
        level.data[new_pos[1]][new_pos[0]] = "X"
        pos_perso = new_pos
        print(order.num_ob)


if __name__ == "__main__":

    main()
