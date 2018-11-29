import log
log = log.GameLog()
log.clear()
log.log("Importing modules...")
import net_code, pygame
log.complete()

log.log("Starting game...")

class Game():
    def __init__(self):
        self.crashed = False
        pygame.init()
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((400, 400)) ## settings?
        self.images = {}
        pygame.display.set_caption("Rocket Mages Alpha")
        self.mainloop()


    def mainloop(self):
        server = net_code.Server("127.0.0.1", 24456, "TrialUsername","basic")
        server_info = server.get_init()  # [map, name, number]
        self.indiv_number = int(server_info[3])
        log.log("Connecting to: %s. Map: %s" % (server_info[0], server_info[1]))
        while not self.crashed:
            self.clock.tick(60) ## settings?
            self.event_handler()
            self.characters = server.get_chars()
            self.display_characters()

            pygame.display.update()

    def display_characters(self):
        # self.client_data: [[username, character, number, x, y, direction]]
        for i in range(0, len(self.characters)):
            char = self.characters[i]
            image = str("../assets/characters/%s_%s.png" % (char[1], char[5]))

            try:
                image = self.images[image]
            except KeyError:
                self.images[image] = pygame.image.load(image)
                image = self.images[image]

            self.display.blit(image, (int(char[3]), int(char[4])))

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

Game()
