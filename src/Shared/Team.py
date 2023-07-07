import BatterStats
import DefensiveStats
import PitcherStats

class PlayerStats():
    def __init__(self):
        self.WAR = 0.0
        self.battingStats = BatterStats()
        self.defensiveStats = DefensiveStats()
        self.pitcherStats = PitcherStats()
        
    def setup(self, war, bs, ds, ps):
        self.WAR = war
        self.battingStats = bs
        self.defensiveStats = ds
        self.pitcherStats = ps