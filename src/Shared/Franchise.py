import State

class Franchise():
    def __init__(self):
        self.state = State.INSEASON
        self.version = 0
        self.year = 0
        
    def setup(self, s, v, y):
        self.version = v
        self.year = y

        if (s == 0):
            self.state = State.PRESEASON
        elif (s == 1):
            self.state = State.INSEASON
        elif (s == 2):
            self.state = State.PLAYOFFS
        
