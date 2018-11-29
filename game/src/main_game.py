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
        self.key_presses = {"w": 0, "a": 0, "s": 0, "d": 0}
        pygame.display.set_caption("Rocket Mages Alpha")
        self.mainloop()


    def mainloop(self):
        server = net_code.Server("127.0.0.1", 24456, "TrialUsername","basic")
        server_info = server.get_init()  # [map, name, number]
        self.indiv_number = int(server_info[3])
        log.log("Connecting to: %s. Map: %s" % (server_info[0], server_info[1]))
        while not self.crashed:
            self.characters = server.get_chars()
            self.display_characters()

            self.event_handler()
            char = self.process_events()
            server.send_char_info(char)

            self.clock.tick(60) ## settings?
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

    def process_events(self):
        for i in range(0, len(self.characters)):
            if int(self.characters[i][2]) == self.indiv_number:
                char = self.characters[i]

                if self.key_presses["w"] == 1:
                    char[4] -= 3
                    char[5] = "y"
                if self.key_presses["s"] == 1:
                    char[4] += 3
                    char[5] = "-y"
                if self.key_presses["a"] == 1:
                    char[3] -= 3
                    char[5] = "x"
                if self.key_presses["d"] == 1:
                    char[3] += 3
                    char[5] = "-x"

                return char



    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                            exit()
                            quit()
                if event.key == pygame.K_w:
                            self.key_presses["w"] = 1
                if event.key == pygame.K_s:
                            self.key_presses["s"] = 1
                if event.key == pygame.K_a:
                            self.key_presses["a"] = 1
                if event.key == pygame.K_d:
                            self.key_presses["d"] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                            self.key_presses["w"] = 0
                if event.key == pygame.K_s:
                            self.key_presses["s"] = 0
                if event.key == pygame.K_a:
                            self.key_presses["a"] = 0
                if event.key == pygame.K_d:
                            self.key_presses["d"] = 0



Game()
