class DefensiveStats():
    def __init__(self):
        self.nicePlays = 0
        self.putOuts = 0
        self.errors = 0
        
    def setup(self, np, po, e):
        self.nicePlays = np
        self.putOuts = po
        self.errors = e