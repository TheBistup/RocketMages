import time

class GameLog ():
    def __init__(self):
        # Make sure log file exists
        try:
            open("game.log","r").read()
            self.f = open("game.log","a")
        except:
            open("game.log","w").write("ROCKET MAGES GAME LOG")
            self.f = open("game.log","a")

        self.start_time = time.time()

    def clear(self):
        open("game.log","w").write("ROCKET MAGES GAME LOG")

    def log(self, contents):
        self.f.write("\n[%s]: %s" % (time.time()-self.start_time, contents))

    def complete(self):
        self.f.write("DONE!")


class NetLog():
    def __init__(self):
        # Make sure log file exists
        try:
            open("net.log","r").read()
            self.f = open("net.log","a")
        except:
            open("net.log","w").write("ROCKET MAGES NET LOG")
            self.f = open("net.log","a")

        self.start_time = time.time()

    def clear(self):
        open("net.log","w").write("ROCKET MAGES NET LOG")

    def log(self, contents):
        self.f.write("\n[%s]: %s" % (time.time()-self.start_time, contents))

    def complete(self):
        self.f.write("DONE!")
