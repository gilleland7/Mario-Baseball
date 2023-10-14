from .PlayerStats import PlayerStats
from .BatterStats import BatterStats
from .PitcherStats import PitcherStats
from .DefensiveStats import DefensiveStats
from Strings import *

class Character():
    def __init__(self):
        self.pitch = 0
        self.hit = 0
        self.field = 0
        self.run = 0
        self.overall = 0.0
        self.name = ""
        self.type = NONE
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

        if (self.type != "" and self.type is not None):
            self.png = self.name + " (" + self.type + ").png"
        else:
            self.png = self.name + ".png"

    def setup(self, char, api):
        # id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID 

        self.name = char[1]
        self.type = char[2]
        self.is_captain = (char[3] == 1)
        self.hit = char[4]
        self.pitch = char[5]
        self.field = char[6]
        self.run = char[7]
        self.overall = char[8]
        self.png = char[9]

        # STATS
        stats = PlayerStats()
        #id, WAR, battingStats[id, AB, BA, BB, HBP, K, S, D, T, HR, SAC, RBI, R, OBP, SLG, SB, CS], defensiveStats[id, nicePlays, putOuts, errors],
        #  pitchingStats[id, IP, GamesPitched, BB, H, R, ER, HR, ERA, W, L, S, HD, WHIP, K]
        playerStats, hitter, defender, pitcher = api.get_player_stats(char[10])
        stats.war = playerStats[1]

        #ab, ba, bb, hbp, k, s, d, t, hr, sac, RBI, r, SLG, OBP, sb, cs
        batting = BatterStats()
        batting.setup(hitter[1], hitter[2], hitter[3], hitter[4], hitter[5], hitter[6], hitter[7], hitter[8], hitter[9], hitter[10], hitter[11], hitter[12], hitter[13], hitter[14], hitter[15], hitter[16])
        stats.batterStats = batting

        #np, po, e
        defense = DefensiveStats()
        defense.setup(defender[1], defender[2], defender[3])
        stats.defensiveStats = defense

        #ip, gp, bb, h, r, er, hr, e, w, l, s, hd, whip, k, hbp
        pitching = PitcherStats()
        pitching.setup(pitcher[1], pitcher[2], pitcher[3], pitcher[4], pitcher[5], pitcher[6], pitcher[7], pitcher[8], pitcher[9], pitcher[10], pitcher[11], pitcher[12], pitcher[13], pitcher[14], pitcher[15])
        stats.pitcherStats = pitching

        self.stats = stats

        # CHEMISTRY
        chemistry = api.get_chemistry(self)

        for entry in chemistry:
            if (entry[3] == 1):
                if (entry[1] == self.name):
                    self.good_chemistry.append(entry[2])
                else:
                    self.good_chemistry.append(entry[3])
            else:
                if (entry[1] == self.name):
                    self.bad_chemistry.append(entry[2])
                else:
                    self.bad_chemistry.append(entry[3])
        