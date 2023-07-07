import Team
import Game

class PlayoffSeries():
    def __init__(self):
        self.round = 0
        self.highSeed = Team()
        self.lowSeed = Team()
        self.gameOne = Game()
        self.gameTwo = Game()
        self.gameThree = Game()
        self.gameFour = Game()
        self.gameFive = Game()
        self.gameSix = Game()
        self.gameSeven = Game()
        self.winner = Team()

        
    def setup(self, r, hs, ls, g1, g2, g3, g4, g5, g6, g7, w):
        self.round = r
        self.highSeed = hs
        self.lowSeed = ls
        self.gameOne = g1
        self.gameTwo = g2
        self.gameThree = g3
        self.gameFour = g4
        self.gameFive = g5
        self.gameSix = g6
        self.gameSeven = g7
        self.winner = w