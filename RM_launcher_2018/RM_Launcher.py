#setup in pygame
import pygame
import launcher_log
import os
import time


pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Rocket Mages Launcher')

clock = pygame.time.Clock()

log = launcher_log.GameLog()
log.clear()

game_open = True

black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
white = (255,255,255)
blue = (30,144,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

image_1 = pygame.image.load('image_1.jpg')
background = pygame.image.load('UI.png')
updates = pygame.image.load('news.png')
backgr = pygame.image.load('background.jpg')

load = False
load_x = 5
#getting texts setup
mediumText = pygame.font.Font("freesansbold.ttf", 60)
smallText = pygame.font.Font("freesansbold.ttf",28)
tinyText = pygame.font.Font("freesansbold.ttf", 12)
font = pygame.font.SysFont(None, 25)

exit_text = smallText.render("Quit",1,(white))
news = mediumText.render("News", 1, black)
launch_text = smallText.render("Launch", 1, (white))


#game loop
while game_open == True:
    display.blit(backgr,(0,0))
#event controller - key press ect...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log.log("game closed...")
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            load = True
            if 694+150 > mouse[0] > 694 and 477+100 > mouse[1] > 477:
                log.log("start button clicked...")
                if load == True:
                    #pygame.draw.rect(display, blue, (3,479,load_x,114))
                    os.chdir("../game/src/")
                    for i in range (0,300):
                        load_x += 1
                        display.blit(backgr,(0,0))
                        pygame.draw.rect(display, blue, (3,479,load_x,114))
                        display.blit(updates,(695,92))
                        display.blit(launch_text,(694+(150/7), 527))
                        display.blit(image_1,(1,1))
                        display.blit(exit_text,(874, 527))
                        display.blit(news,(768, 25))
                        display.blit(fps, (10, 10))
                        pygame.display.update()

                    for i in range (0,373):
                        load_x += 1
                        display.blit(backgr,(0,0))
                        pygame.draw.rect(display, blue, (3,479,load_x,114))
                        display.blit(updates,(695,92))
                        display.blit(launch_text,(694+(150/7), 527))
                        display.blit(image_1,(1,1))
                        display.blit(exit_text,(874, 527))
                        display.blit(news,(768, 25))
                        display.blit(fps, (10, 10))
                        pygame.display.update()

                    os.system("start python main_game.py")
                pygame.quit()
                quit()

            elif 844+150 > mouse[0] > 844 and 477+100 > mouse[1] > 477:
                log.log("Game closed by clicking quit...")
                pygame.quit()
                quit()
            else:
                log.log("Mouse button clicked, but nothing happened...[Error 1]")

    #get mouse pos and highlights if over button
    mouse = pygame.mouse.get_pos()
    if 694+150 > mouse[0] > 694 and 477+100 > mouse[1] > 477:
        pygame.draw.rect(display, bright_green,(694,477,150,118))
        pygame.draw.rect(display, red,(844,477,150,118))
    elif 844+150 > mouse[0] > 840 and 477+100 > mouse[1] > 475:
        pygame.draw.rect(display, bright_red,(844,477,150,118))
        pygame.draw.rect(display, green,(694,477,150,118))
    else:
        pygame.draw.rect(display, green,(694,477,150,118))
        pygame.draw.rect(display, red,(844,477,150,118))

    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))

    display.blit(background,(0,0))
    display.blit(updates,(695,92))
    display.blit(launch_text,(694+(150/7), 527))
    display.blit(image_1,(1,1))
    display.blit(exit_text,(874, 527))
    display.blit(news,(768, 25))
    display.blit(fps, (10, 10))

    clock.tick(144)

    #RM_title()
    pygame.display.update()
