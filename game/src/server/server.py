import socket, json, ast
from multiprocessing.dummy import Pool as ThreadPool


class Server():
    def __init__(self):
        '''
        Choose map from config file
        Initialise player data
        Deal with all the requests
        '''

        with open("server_info.json","r") as file:
            data = json.load(file)

        self.server = {}
        self.server["ip"] = data["ip"]
        self.server["port"] = int(data["port"])
        self.server["player_number"] = int(data["player_number"])
        self.server["server_name"] = data["server_name"]
        self.server["map"] = data["default_map"]


        self.sock = socket.socket()
        self.sock.bind((data["ip"], int(data["port"])))
        self.sock.listen(int(data["player_number"]))
        self.clients = []

        print("[!] Self setup complete! Waiting for connections.")
        number = 0
        for i in range(int(data["player_number"])):
            c, addr = self.sock.accept()
            self.clients.append([c, addr, number])
            number += 1

        self.recieve_init()

    def recieve_init(self):
        print("[!] Get init data from clients")
        self.client_data = []
        for i in range(0, len(self.clients)):
            self.clients[i][0].send(str.encode("+--SEND-INIT--+"))

        for i in range(0, len(self.clients)):
            contents = ""

            contents = self.clients[i][0].recv(1024).decode()
            self.clients[i][0].send(b'TICK')
            self.clients[i][0].recv(1024).decode()

            contents = contents.split("|")
            self.client_data.append([contents[0], contents[1], str(i), 10, 10, "x"]) ## where we pick start position.

        print("[!] Finished initial handshake with clients")
        self.mainloop()


    def mainloop(self):
        self.entities = []
        pool = ThreadPool(len(self.clients))
        while True:
            pool.map(self.client_handler, self.clients)
            ## entity handling here please!
            # entity [type, speed, direction, self.indiv_number, radius, ticks, [x, y]]


            new_entities = []
            for i in range(0, len(self.entities)):
                entity = self.entities[i]
                if entity[5] > 0:
                    new_entities.append(entity)
            self.entities = new_entities

            for i in range(0, len(self.entities)):
                entity = self.entities[i]
                if int(entity[5]) > 0:
                    direction = entity[2]
                    if direction == "x":
                        entity[6][0] = int(entity[6][0]) + int(entity[1])
                    elif direction == "-x":
                        entity[6][0] = int(entity[6][0]) - int(entity[1])
                    elif direction == "y":
                        entity[6][1] = int(entity[6][1]) - int(entity[1])
                    elif direction == "-y":
                        entity[6][1] = int(entity[6][1]) + int(entity[1])
                    entity[5] = int(entity[5]) - 1
                    self.entities[i] = entity


    def client_handler(self, client):

        ## self.client_data [[username, character, number, x, y, direction]]
        self.entity = [] ## = [[number, x, y, direction]]

        data = client[0].recv(65536).decode() ## max for packet is 65536
        if data != "":
            #print("[!] Data from: " + str(client[1]) + ": ", data)p
            pass
        if data == "--+get-init+--":
            print("[!] Got request for initial data from " + str(client[1]))
            message = str.encode("%s|%s|%s|%s" % (self.server["map"],
            self.server["server_name"],
            str(self.server["player_number"]),
            client[2]))
            client[0].send(message)

        if data == "--+get-char+--":
            client[0].send(str.encode(str(self.client_data)))

        if data == "--+send-char+--":
            client[0].send(str.encode("TICK"))
            new_data = ast.literal_eval(client[0].recv(65536).decode())
            for i in range(0, len(self.client_data)):
                if self.client_data[i][2] == new_data[2]:
                    self.client_data[i] = new_data
            client[0].send(str.encode("TICK"))

        if data == "--+send-entity+--":
            client[0].send(str.encode("TICK"))
            new_data = ast.literal_eval(client[0].recv(65536).decode())
            client[0].send(str.encode("TICK"))

            self.entities.append(new_data)

        if data == "--+get-entity+--":
            client[0].send(str.encode(str(self.entities)))






Server()
