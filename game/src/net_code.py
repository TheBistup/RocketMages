import socket, log, time, ast
log = log.NetLog()



class Search():
    def __init__(self):
        self.my_ip = socket.gethostbyname(socket.gethostname()).split(".")
        self.my_ip = str(self.my_ip[0] + self.my_ip[1] + self.my_ip[2])
        self.sock = socket.socket()
        self.search_port = 24456
        log.clear()


    def find(self):
        games = []
        for i in range(0, 256):
            ip = self.my_ip + str(".%s" % (str(i)))
            result = sock.connect_ex(('127.0.0.1', self.search_port)) # TODO: Nope! We need to create a search port open for game finding
            if result == 0:
                log.log("Found game at IP: %s" % (ip))
                games.append(ip)
        return games

class Server():
    def __init__(self, ip, port, username, character):
        log.clear()
        log.log("Server class initialised.")
        self.sock = socket.socket()
        while True:
            try:
                self.sock.connect((ip, port))
                break
            except:
                delay = 2
                log.log("Server refused connection. Wait %s second(s) before retry." % (str(delay)))
                time.sleep(delay)

        if self.sock.recv(1024).decode() == "+--SEND-INIT--+":
            self.sock.send(str.encode("%s|%s" % (username, character)))
            self.sock.recv(1024)
            self.sock.send(str.encode("--+end+--"))

            ### Get random start pos from server?

    def get_init(self):
        self.sock.send(str.encode("--+get-init+--"))
        return self.sock.recv(65536).decode().split("|")

    def get_chars(self):
        self.sock.send(str.encode("--+get-char+--"))
        return ast.literal_eval(self.sock.recv(65536).decode())

    def send_char_info(self, char):
        self.sock.send(str.encode("--+send-char+--"))
        self.sock.recv(256)
        self.sock.send(str.encode(str(char)))
        self.sock.recv(256)

    def send_ent_info(self, ent):
        self.sock.send(str.encode("--+send-entity+--"))
        self.sock.recv(256)
        self.sock.send(str.encode(str(ent)))
        self.sock.recv(256)

    def get_ents(self):
        self.sock.send(str.encode("--+get-entity+--"))
        data = self.sock.recv(65536).decode()
        return ast.literal_eval(data)
