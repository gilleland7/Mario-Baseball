import Team

class TeamStats():
    def __init__(self):
        self.overall = 0.0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
    def setup(self, o, w, l, tie):
        self.overall = o
        self.wins = w
        self.losses = l
        self.ties = tie
        