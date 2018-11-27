import log
log = log.GameLog()
log.clear()
log.log("Importing modules...")
import net_code, pygame
log.complete()

log.log("Starting game...")

class Game():
    def __init__(self):
        pygame.init()
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((1000, 1000)) ## settings?


    def mainloop():
        while not crashed:
            self.clock.tick(60) ## settings?
