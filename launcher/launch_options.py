import pygame, os

class Menu():
    def __init__(self):
        pygame.init()
        self.blue = (60, 130, 242)
        self.light_blue = (107, 163, 255)
        self.display = pygame.display.set_mode((350, 120))
        self.clock = pygame.time.Clock()
        self.title = "launcher"
        self.main_loop()

    def main_loop(self):
        while True:
            self.pos = pygame.mouse.get_pos()
            self.event_manager()
            self.display.fill((255, 255, 255))
            self.draw()
            self.highlight()
            self.text()
            fps = str(int(self.clock.get_fps()))
            pygame.display.set_caption("%s: %s fps" % (self.title, fps))
            pygame.display.update()
            self.clock.tick(60)

    def draw(self):
        pygame.draw.rect(self.display, self.blue, (10, 10, 150, 100))
        pygame.draw.rect(self.display, self.blue, (190, 10, 150, 100))

    def text(self):
        smallText = pygame.font.Font("freesansbold.ttf", 14)
        LAN = smallText.render("Launch LAN server", 1, (255, 255, 255))
        self.display.blit(LAN, (18,55))
        search = smallText.render("Search for a game", 1, (255, 255, 255))
        self.display.blit(search, (203,55))


    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 160 > self.pos[0] > 10 and 110 > self.pos[1] > 10:
                    #LAN
                    try:
                        os.chdir("../game/src/server")
                    except:
                        pass
                    os.system("start python server.py")


                elif 340 > self.pos[0] > 190 and 110 > self.pos[1] > 10:
                    os.chdir("../game/src")
                    search = net_code.Search()
                    print(search.search())

    def highlight(self):
        if 160 > self.pos[0] > 10 and 110 > self.pos[1] > 10:
            pygame.draw.rect(self.display, self.light_blue, (10, 10, 150, 100))

        elif 340 > self.pos[0] > 190 and 110 > self.pos[1] > 10:
            pygame.draw.rect(self.display, self.light_blue, (190, 10, 150, 100))


Menu()
