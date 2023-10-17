class BatterStats():
    def __init__(self):
        self.atBats = 0
        self.pa = 0
        self.average = 0.0
        self.walks = 0
        self.hitByPitch = 0
        self.strikeouts = 0
        self.hits = 0
        self.doubles = 0
        self.triples = 0.0
        self.homeRuns = 0
        self.sacrifices = 0
        self.rbi = 0
        self.runs = 0
        self.slg = 0.0
        self.obp = 0.0
        self.ops = 0.0
        self.stolenBases = 0
        self.caughtStealing = 0
        
    def setup(self, ab, ba, bb, hbp, k, h, d, t, hr, sac, RBI, r, OBP, SLG, sb, cs, pa):
        self.atBats = ab
        self.pa = pa
        self.average = ba
        self.walks = bb
        self.hitByPitch = hbp
        self.strikeouts = k
        self.hits = h
        self.doubles = d
        self.triples = t
        self.homeRuns = hr
        self.sacrifices = sac
        self.rbi = RBI
        self.runs = r
        self.slg = SLG
        self.obp = OBP
        self.ops = SLG + OBP
        self.stolenBases = sb
        self.caughtStealing = cs