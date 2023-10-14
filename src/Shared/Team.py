from .TeamStats import TeamStats
from .Character import Character
from .Stadium import Stadium
from .Division import Division
from .TeamStats import TeamStats

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
    
    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo   
    def setup(self, teamArr, api):
        self.name = teamArr[0]

        player1 = api.get_character(teamArr[1])
        character1 = Character()
        character1.setup(player1, api)
        self.charOne = character1

        player2 = api.get_character(teamArr[2])
        character2 = Character()
        character2.setup(player2, api)
        self.charTwo = character2

        player3 = api.get_character(teamArr[3])
        character3 = Character()
        character3.setup(player3, api)
        self.charThree = character3

        player4 = api.get_character(teamArr[4])
        character4 = Character()
        character4.setup(player4, api)
        self.charFour = character4

        player5 = api.get_character(teamArr[5])
        character5 = Character()
        character5.setup(player5, api)
        self.charFive = character5

        player6 = api.get_character(teamArr[6])
        character6 = Character()
        character6.setup(player6, api)
        self.charSix = character6

        player7 = api.get_character(teamArr[7])
        character7 = Character()
        character7.setup(player7, api)
        self.charSeven = character7

        player8 = api.get_character(teamArr[8])
        character8 = Character()
        character8.setup(player8, api)
        self.charEight = character8

        player9 = api.get_character(teamArr[9])
        character9 = Character()
        character9.setup(player9, api)
        self.charNine = character9

        stats = TeamStats()
        teamStats = api.get_team_stats(self)
        stats.setup(teamStats)
        self.stats = stats

        stadium = Stadium()
        stadium.name = teamArr[11]
        self.stadium = stadium

        division = Division()
        division.name = teamArr[12]
        self.division = division

        self.playerTeam = (teamArr[13] == 1)

        self.logo = teamArr[14]

