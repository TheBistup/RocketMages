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
        pygame.display.set_caption("Rocket Mages Alpha")
        self.mainloop()


    def mainloop(self):
        server = net_code.Server("127.0.0.1", 24456, "TrialUsername","basic")
        server.get_init()
        while not self.crashed:
            self.clock.tick(60) ## settings?
            self.event_handler()


    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

Game()
