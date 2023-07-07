import Team

class Season():
    def __init__(self):
        self.year = 0
        self.champion = Team()
        self.runnerUp = Team()
        self.semiFinalsTeamOne = Team()
        self.semiFinalsTeamTwo = Team()
        
    def setup(self, y, c, ru, sft1, sft2):
        self.year = y
        self.champion = c
        self.runnerUp = ru
        self.semiFinalsTeamOne = sft1
        self.semiFinalsTeamTwo = sft2