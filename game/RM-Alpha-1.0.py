import pygame
import os

def Setup():
    displaySettings = (800,600)
    gameCaption = "RocketMages: Alpha 1.0"
    gameDisplay = pygame.display.set_mode(displaySettings)
    
    pygame.init()
    pygame.display.set_caption(gameCaption)
    clock = pygame.time.Clock()
    Play(gameDisplay, clock)

def Play(gameDisplay, clock):
    crashed = False
    os.chdir("assets\\")
    mapImage = pygame.image.load("map_magic_trial_1.png")
    def startMap(mapImage):
        gameDisplay.blit(mapImage, (0,0))
    
    characterImage = pygame.image.load("character_wizard_default_1.png")

    startX = 300
    startY = 500
    
    charX = 0
    charY = 0

    direction = "x"
    
    def animateChar(x, y, d):
        if d == "x":
            gameDisplay.blit(characterImage, (x,y))
        elif d == "-x":
            gameDisplay.blit(characterImage, (x,y))
        elif d == "y":
            gameDisplay.blit(characterImage, (x,y))
        else:
            gameDisplay.blit(characterImage, (x,y))
    
    
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    charX -= 3
                    direction = "x"
                if event.key == pygame.K_RIGHT:
                    charX += 3
                    direction = "-x"
                if event.key == pygame.K_UP:
                    charY -= 3
                    direction = "y"
                if event.key == pygame.K_DOWN:
                    charY += 3
                    direction = "-y"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    charX = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    charY = 0

                    
        startX += charX
        startY += charY
        if startX > 760:
            startX = 760
        elif startX < 0:
            startX = 0
        elif startY > 560:
            startY = 560
        elif startY < 0:
            startY = 0
        else:
            pass
            
        startMap(mapImage)
        animateChar(startX, startY, direction)
        pygame.display.update()
        clock.tick(60)

    

Setup()

