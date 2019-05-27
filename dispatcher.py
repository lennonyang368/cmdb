class Dispatcher:
    cmds = {}
    def reg(self,cmd,fn):
        self.cmds[cmd] = fn

    def run(self):
        while True:
            cmd = input('>>').strip()
            if cmd == 'quit':
                break
            self.cmds.get(cmd,self.defaultfunc)()

    def defaultfunc(self):
        print("Unknow command")