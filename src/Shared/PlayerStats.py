from .DefensiveStats import DefensiveStats
from .PitcherStats import PitcherStats
from .BatterStats import BatterStats

class PlayerStats():  
    def __init__(self):
        self.war = 0.0
        self.defensiveStats = DefensiveStats()
        self.pitcherStats = PitcherStats()
        self.batterStats = BatterStats()
        
    def setup(self, WAR, d, p , b):
        self.war = WAR
        self.defensiveStats = d
        self.pitcherStats = p
        self.batterStats = b