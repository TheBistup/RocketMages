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

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((data["ip"], int(data["port"])))
        self.sock.listen(int(data["player_number"]))
        self.clients = []

        print("[!] Self setup complete! Waiting for connections.")
        for i in range(int(data["player_number"])):
            c, addr = self.sock.accept()
            self.clients.append([c, addr])

        self.recieve_init()

    def recieve_init(self):
        self.client_data = []
        for i in range(0, len(self.clients)):
            self.clients[i][0].send(str.encode("+--SEND-INIT--+"))

        for i in range(0, len(self.clients)):
            contents = ""
            data = ""

            while "--+end+--" not in data:
                data = self.clients[i][0].recv(1024).decode()
                contents += data

            print("[!] Got data from client: ", str(i))
            contents = contents.split("|")
            self.client_data.append([contents[0], contents[1], str(i), 0, 0, "x"])




Server()
