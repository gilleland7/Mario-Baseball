import Character
import Season

class Award():
    def __init__(self):
        self.name = ""
        self.winner = Character()
        self.season = Season()

        
    def setup(self, n, w, s):
        self.name = n
        self.winner = w
        self.season = s