from .TeamStats import TeamStats
from .Character import Character
from .Stadium import Stadium
from .Division import Division

class Team():
    def __init__(self):
        self.name = ""
        self.charOne = Character()
        self.charTwo = Character()
        self.charThree = Character()
        self.charFour = Character()
        self.charFive = Character()
        self.charSix = Character()
        self.charSeven = Character()
        self.charEight = Character()
        self.charNine = Character()
        self.stats = TeamStats()
        self.stadium = Stadium()
        self.division = Division()
        self.playerTeam = False
        self.logo = ""
        
    def setup(self, n, c1, c2, c3, c4, c5, c6, c7, c8, c9, st, stad, div, pt, l):
        self.name = n
        self.charOne = c1
        self.charTwo = c2
        self.charThree = c3
        self.charFour = c4
        self.charFive = c5
        self.charSix = c6
        self.charSeven = c7
        self.charEight = c8
        self.charNine = c9
        self.stats = st
        self.stadium = stad
        self.division = div
        self.playerTeam = pt
        self.logo = l