# import stuffss
import pygame
from pygame.locals import *

pygame.init()

# definition of the sizes
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer') # name of the project

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()