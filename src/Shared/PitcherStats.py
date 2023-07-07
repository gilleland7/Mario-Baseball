class PitcherStats():
    def __init__(self):
        self.IP = 0
        self.gamesPitched = 0
        self.walks = 0
        self.hits = 0
        self.runs = 0
        self.earnedRuns = 0
        self.homeRuns = 0
        self.era = 0.0
        self.wins = 0
        self.losses = 0
        self.saves = 0
        self.holds = 0
        self.WHIP = 0.0
        self.strikeouts = 0
        
    def setup(self, ip, gp, bb, h, r, er, hr, e, w, l, s, hd, whip, k):
        self.IP = ip
        self.gamesPitched = gp
        self.walks = bb
        self.hits = h
        self.runs = r
        self.earnedRuns = er
        self.homeRuns = hr
        self.era = er
        self.wins = w
        self.losses = l
        self.saves = s
        self.holds = hd
        self.WHIP = whip
        self.strikeouts = k