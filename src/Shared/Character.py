import PlayerStats

class Character():
    def __init__(self):
        self.pitch = 0
        self.hit = 0
        self.field = 0
        self.run = 0
        self.overall = 0.0
        self.name = ""
        self.type = ""
        self.is_captain = 0
        self.good_chemistry = [] # Good chemistry = 1
        self.bad_chemistry = [] # Bad chemistry = 0
        self.png = ""
        self.stats = PlayerStats()
        
    def setup(self, p, h, f, r, o, n, t, ic, gc, bc):
        self.pitch = p
        self.hit = h
        self.field = f
        self.run = r
        self.overall = o
        self.name = n
        self.type = t
        self.is_captain = ic
        self.good_chemistry = gc
        self.bad_chemistry = bc

        if (self.type is not "" and self.type is not None):
            self.png = self.name + " (" + self.type + ").png"
        else:
            self.png = self.name + ".png"