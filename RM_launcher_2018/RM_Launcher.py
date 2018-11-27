#setup in pygame
import pygame

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Rocket Mages Launcher')

clock = pygame.time.Clock()

open = True

#loads background
background = pygame.image.load('background.jpg')
def BG():
    display.blit(background,(0,0))
title_x = 85
title_y = 20
#loading title text image
title_text = pygame.image.load('title_text.png')
def RM_title():
    display.blit(title_text,(title_x,title_y))

#game loop
while open == True:
    pygame.display.update()
    clock.tick(60)
#event controller - key press ect...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            open = False
    RM_title()
