import Team

class PlayerStats():
    def __init__(self):
        self.team = Team()
        self.overall = 0.0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
    def setup(self, t, o, w, l, tie):
        self.team = t
        self.overall = o
        self.wins = w
        self.losses = l
        self.ties = tie
        