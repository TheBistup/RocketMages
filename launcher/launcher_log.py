import time

class GameLog ():
    def __init__(self):
        # Make sure log file exists
        try:
            open("launcher.log","r").read()
            self.f = open("launcher.log","a")
        except:
            open("launcher.log","w").write("ROCKET MAGES GAME LOG")
            self.f = open("launcher.log","a")

        self.start_time = time.time()

    def clear(self):
        open("launcher.log","w").write("ROCKET MAGES GAME LOG")

    def log(self, contents):
        self.f.write("\n[%s]: %s" % (time.time()-self.start_time, contents))

    def complete(self):
        self.f.write("DONE!")
