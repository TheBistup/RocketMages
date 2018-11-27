#setup in pygame
import pygame


pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Rocket Mages Launcher')

clock = pygame.time.Clock()

open = True

black = (0,0,0)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)


background = pygame.image.load('background.jpg')
title_text = pygame.image.load('title_text.png')

#getting texts setup
font = pygame.font.SysFont(None, 25)



#loads background
display.blit(background,(0,0))



#loading title text image
title_x = 185
title_y = 20

def RM_title():
    display.blit(title_text,(title_x,title_y))



#game loop
while open == True:
    pygame.display.update()
    display.blit(background,(0,0))
#event controller - key press ect...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            open = False

    #get mouse pos and highlights if over button
    mouse = pygame.mouse.get_pos()
    if 200+150 > mouse[0] > 200 and 450+100 > mouse[1] > 450:
        pygame.draw.rect(display, bright_green,(200,450,150,100))
        pygame.draw.rect(display, red,(650,450,150,100))
    elif 650+150 > mouse[0] > 650 and 450+100 > mouse[1] > 450:
        pygame.draw.rect(display, bright_red,(650,450,150,100))
        pygame.draw.rect(display, green,(200,450,150,100))
    else:
        pygame.draw.rect(display, green,(200,450,150,100))
        pygame.draw.rect(display, red,(650,450,150,100))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    launch_text = smallText.render("Launch", 1, (255,255,255))
    display.blit(launch_text,(225, 500))

    exit_text = smallText.render("Quit",1,(255,255,255))
    display.blit(exit_text,(675, 500))

    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    display.blit(fps, (10, 10))

    clock.tick(120)

    RM_title()


    pygame.display.update()
