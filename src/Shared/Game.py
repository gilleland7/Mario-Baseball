import Stadium
import Team

class Game():
    def __init__(self):
        self.gameNumber = 0
        self.stadium = Stadium()
        self.homeTeam = Team()
        self.awayTeam = Team()
        self.homeScore = 0
        self.awayScore = 0
        
    def setup(self, number, stadium, home, away, hScore, aScore):
        self.gameNumber = number
        self.stadium = stadium
        self.homeTeam = home
        self.awayTeam = away
        self.homeScore = hScore
        self.awayScore = aScore