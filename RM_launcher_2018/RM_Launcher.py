#setup in pygame
import pygame

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Rocket Mages Launcher')

clock = pygame.time.Clock()

open = True

#loading title text image
title_text = pygame.image.display('title_text.png')
def RM_t():
    display.blit(title_text(400,500))

#game loop
while open = True:
    pygame.display.update()
    clock.tick(60)
#event controller - key press ect...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            open = False
