#setup in pygame
import pygame
import launcher_log
import os


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

bright_red = (255,0,0)
bright_green = (0,255,0)

image_1 = pygame.image.load('image_1.jpg')
background = pygame.image.load('UI.png')
#title_text = pygame.image.load('title_text.png')
#gathering info for news paragraph


#getting texts setup
mediumText = pygame.font.Font("freesansbold.ttf", 60)
smallText = pygame.font.Font("freesansbold.ttf",28)
tinyText = pygame.font.Font("freesansbold.ttf", 12)
font = pygame.font.SysFont(None, 25)

news_file = open('news.txt','r')
news_info = str(news_file.read())
label = []
for line in news_info:
    label.append(tinyText.render(news_info, 1, black))
    
exit_text = smallText.render("Quit",1,(white))
news = mediumText.render("News", 1, black)
launch_text = smallText.render("Launch", 1, (white))



#game loop
while game_open == True:
    display.blit(background,(0,0))
#event controller - key press ect...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log.log("game closed...")
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 200+150 > mouse[0] > 200 and 450+100 > mouse[1] > 450:
                log.log("start button clicked...")
                os.chdir("../game/src/")
                os.system("start python main_game.py")
                pygame.quit()
                quit()
            elif 650+150 > mouse[0] > 650 and 450+100 > mouse[1] > 450:
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

    #display.blit(news_para,(695,95))
    display.blit(launch_text,(694+(150/7), 527))
    display.blit(image_1,(1,1))
    display.blit(exit_text,(874, 527))
    display.blit(news,(768, 25))
    for line in range(len(label)):
        display.blit(label(line),(695,95+(line*fontsize)+(15*line)))
    display.blit(fps, (10, 10))

    clock.tick(144)

    #RM_title()
    pygame.display.update()
