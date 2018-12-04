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
        self.entities = []
        self.x = 0; self.y = 0
        self.direction = "x"
        self.key_presses = {"w": 0, "a": 0, "s": 0, "d": 0,
                            "b": 0, "n": 0, "m": 0} ## projectile buttons

        self.b_timer = 0; self.n_timer = 0; self.m_timer = 0

        # entity [type, speed, direction, self.indiv_number, radius, ticks]

        self.title = "Rocket Mages Alpha"
        pygame.display.set_caption(self.title)
        self.mainloop()


    def mainloop(self):
        server = net_code.Server("127.0.0.1", 24456, "TrialUsername","basic")
        server_info = server.get_init()  # [map, name, number]
        self.indiv_number = int(server_info[3])


        log.log("Connecting to: %s. Map: %s" % (server_info[0], server_info[1]))
        while not self.crashed:
            self.binds = {
            "b": ["nerph_rebel", "5", self.direction, self.indiv_number, 5, 60, [self.x, self.y]],
            "n": ["large_rocket", "5", self.direction, self.indiv_number, 5, 300, [self.x, self.y]],
            "m": ["massive_shuriken", "5", self.direction, self.indiv_number, 5, 50, [self.x, self.y]],
            "h": ["kim_ballistic", "5", self.direction, self.indiv_number, 5, 100, [self.x, self.y]]
             }

            self.characters = server.get_chars()
            self.display_map(server_info[0])
            self.display_characters()

            self.event_handler()
            char = self.process_events()
            server.send_char_info(char)

            if self.b_timer > 0:
                self.b_timer -= 1
            if self.n_timer > 0:
                self.n_timer -= 1
            if self.m_timer > 0:
                self.m_timer -= 1

            entity = self.process_entities()
            if entity != []:
                server.send_ent_info(entity)

            self.entities = server.get_ents()
            self.display_entities()


            self.clock.tick(60) ## settings?
            fps = str(int(self.clock.get_fps()))
            pygame.display.set_caption("%s: %s fps" % (self.title, fps))
            pygame.display.update()

    def display_entities(self):
        # entity [type, speed, direction, self.indiv_number, radius, ticks, [x, y]]
        for i in range(0, len(self.entities)):
            entity = self.entities[i]
            image = str("../assets/objects/%s.png" % (entity[0]))

            try:
                image = self.images[image]
            except KeyError:
                self.images[image] = pygame.image.load(image)
                image = self.images[image]

            if entity[2] == "-x":
                image = pygame.transform.rotate(image, 180)
            if entity[2] == "y":
                image = pygame.transform.rotate(image, 90)
            if entity[2] == "-y":
                image = pygame.transform.rotate(image, -90)

            self.display.blit(image, (entity[6][0], entity[6][1]))


    def display_map(self, map):
        image = str("../assets/maps/%s.png" % (map))

        try:
            image = self.images[image]
        except KeyError:
            self.images[image] = pygame.image.load(image)
            image = self.images[image]

        self.display.blit(image, (0, 0))

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
                    char[5] = "-y"
                    self.y = char[4]
                    self.direction = "y"
                if self.key_presses["s"] == 1:
                    char[4] += 3
                    char[5] = "y"
                    self.y = char[4]
                    self.direction = "-y"
                if self.key_presses["a"] == 1:
                    char[3] -= 3
                    char[5] = "x"
                    self.x = char[3]
                    self.direction = "-x"
                if self.key_presses["d"] == 1:
                    char[3] += 3
                    char[5] = "-x"
                    self.x = char[3]
                    self.direction = "x"

                self.x = char[3]
                self.y = char[4]

                return char

    def process_entities(self):

        entity = []
        if self.key_presses["b"] == 1 and self.b_timer == 0:
            entity = self.binds["b"]
            self.b_timer = 30
        elif self.key_presses["n"] == 1 and self.n_timer == 0:
            entity = self.binds["n"]
            self.n_timer = 600
        elif self.key_presses["m"] == 1 and self.m_timer == 0:
            entity = self.binds["m"]
            self.m_timer = 100

        return entity

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

                if event.key == pygame.K_b:
                    self.key_presses["b"] = 1
                if event.key == pygame.K_n:
                    self.key_presses["n"] = 1
                if event.key == pygame.K_m:
                    self.key_presses["m"] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.key_presses["w"] = 0
                if event.key == pygame.K_s:
                    self.key_presses["s"] = 0
                if event.key == pygame.K_a:
                    self.key_presses["a"] = 0
                if event.key == pygame.K_d:
                    self.key_presses["d"] = 0

                if event.key == pygame.K_b:
                    self.key_presses["b"] = 0
                if event.key == pygame.K_n:
                    self.key_presses["n"] = 0
                if event.key == pygame.K_m:
                    self.key_presses["m"] = 0



Game()
