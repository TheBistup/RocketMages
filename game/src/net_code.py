import socket, log, time
log = log.NetLog()



class Search():
    def __init__(self):
        pass

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
                log.log("Server refused connection. Wait %s seconds before retry." % (str(delay)))
                time.sleep(1)

        print("[!] Got connection to server!")

        if self.sock.recv(1024).decode() == "+--SEND-INIT--+":
            print("Recieved initial character data request")
            self.sock.send(str.encode("%s|%s" % (username, character)))
            self.sock.recv(1024)
            self.sock.send(str.encode("--+end+--"))

            ### Get random start pos from server?

    def get_init(self):
        self.sock.send(str.encode("--+get-init+--"))

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
