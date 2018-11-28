import socket, json


class Server():
    def __init__(self):
        '''
        Choose map from config file
        Initialise player data
        Deal with all the requests
        '''

        with open("server_info.json","r") as file:
            data = json.load(file)

        self.sock = socket.socket()
        self.sock.bind((data["ip"], int(data["port"])))
        self.sock.listen(int(data["player_number"]))
        self.clients = []

        print("[!] Self setup complete! Waiting for connections.")
        for i in range(int(data["player_number"])):
            c, addr = self.sock.accept()
            self.clients.append([c, addr])

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
            self.client_data.append([contents[0], contents[1], str(i), 0, 0, "x"])

        print("[!] Finished initial handshake with clients")
        while True:
            self.broadcast_init()

    def broadcast_init(self):
        for i in range(0, len(self.clients)):
            data = self.clients[i][0].recv(1024).decode()
            print("[!] Data from: " + str(self.clients[i][1]) + ": ", data)
            if data == "--+get-init+--":
                self.clients[i][0]




Server()
