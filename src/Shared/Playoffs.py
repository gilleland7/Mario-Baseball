import Team
import PlayoffSeries

class Playoffs():
    def __init__(self):
        self.overallRound = 0
        self.roundOneDivisionOne = PlayoffSeries()
        self.roundOneDivisionTwo = PlayoffSeries()
        self.championship = PlayoffSeries()
        self.champion = Team()
        
    def setup(self, round, r1d1, r1d2, ch, champ):
        self.overallRound = round
        self.roundOneDivisionOne = r1d1
        self.roundOneDivisionTwo = r1d2
        self.championship = ch
        self.champion = champ