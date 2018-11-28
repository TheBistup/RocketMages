import socket, log, time
log = log.NetLog()



class Search():
    def __init__(self):
        pass

class Server():
    def __init__(self, ip, port, username, character):
        log.log("Server class initialised.")
        self.sock = socket.socket()
        while True:
            try:
                self.sock.connect((ip, port))
            except:
                delay = 2
                log.log("Server refused connection. Wait %s seconds before retry." % (str(delay)))
                time.sleep(2)

        if self.sock.recv(1024).decode() == "+--SEND-INIT--+":
            log.log("Recieved initial character data request")
            self.sock.send(str.encode("username|character"))

            ### Get random start pos from server?

    def get_init(self):
        self.sock.send(str.encode("--+get-init+--"))
        init_file = ""
        data = ""

        while "--+end+--" not in data:
            data = self.sock.recv(1024).decode()
            init_file += data

        log.log("Got initial server information.")

        open("map.rminfo","w").write(init_file)
        return True


    def get_char_data(self):
        self.sock.send(str.encode("--+get-char+--"))
        char_file = ""
        data = ""

        while "--+end+--" not in data:
            data = self.sock.recv(1024).decode()
            char_file += data

        log.log("Got character info successfully.")

        open("char.rminfo","w").write(char_file)
        return True

    def get_entity_data(self):
        self.sock.send(str.encode("--+get-entity+--"))
        ent_file = ""
        data = ""

        while "--+end+--" not in data:
            data = self.sock.recv(1024).decode()
            ent_file += data

        log.log("Got entity info successfully.")

        open("entity.rminfo","w").write(char_file)
        return True

    def send_char_info(user, data):
        move_to_x = data["move_to"][0]
        move_to_y = data["move_to"][1]
        direction = data["direction"]
        fire_projectile_entity = data["proj_num"]

        self.sock.send(str.encode("--+send-char+--"))
        self.sock.recv(1024)
        self.sock.send(str.encode("%s|%s:%s|%s|%s") % (user,
         move_to_x,
         move_to_y,
         direction,
         fire_projectile_entity))
        log.log("Sent character data")
