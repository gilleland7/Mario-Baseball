# Import flask and datetime module for showing date and time
from flask import Flask
import sys
from middlewareAPI import MiddlewareAPI

from Shared.State import State
from Shared.Team import Team
from Shared.TeamStats import TeamStats

# Get current and then parent directories
sys.path.append(".")
from src import Strings

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing state data
@app.route('/state')
def get_state():
    api = MiddlewareAPI()
    franchiseState = api.get_franchise()
    state = State(franchiseState[1])
    
    # Returning to show in reactjs
    return {
        'state':state.value,
        'version':franchiseState[2],
        'year':franchiseState[3]
        }

# Route for seeing userteam data
@app.route('/userteam')
def get_team():
    api = MiddlewareAPI()
   
    userTeam = api.get_user_team()
    team = Team()
    team.setup(userTeam, api)

    # Returning to show in reactjs
    return {
        'teamLogo':team.logo,
        'teamName':team.name
    }

# Route for seeing last game data
@app.route('/lastgame')
def get_prev_game():
    api = MiddlewareAPI()
   
    #id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    game = api.get_previous_game()
    home = game[3]
    away = game[4]
    homeScore = game[5]
    awayScore = game[6]

    winner = 'tie'
    if (homeScore > awayScore):
        winner = home
    elif (awayScore > homeScore):
        winner = away

    # Returning to show in reactjs
    return {
        'home':home,
        'away':away,
        'homeScore':homeScore,
        'awayScore':awayScore,
        'winner':winner
    }

#Route for seeing teams data
@app.route('/teams')
def get_teams():
    api = MiddlewareAPI()
   
    teams = api.get_all_teams()   
    teamList = []   
    teamCharacterValues = {}

    userTeam = api.get_user_team()[0]
    index = 0
    teamIndex = 0

    for teamData in teams:
        team = Team()
        team.setup(teamData, api)
        teamList.append(team.name)
        characterValues = []
        #id, name, type, isCaptain, bat, pitch, field, run, overall, png, goodChemistry, badChemistry, PlayerStats ID 
        char1 = team.charOne

        characterValues.append([char1.name, char1.type, char1.is_captain, char1.hit, char1.pitch, char1.field, char1.run, 
                               char1.overall, char1.png, char1.good_chemistry, char1.bad_chemistry, 
                               [char1.stats.war, [char1.stats.batterStats.pa, char1.stats.batterStats.atBats, 
													                          char1.stats.batterStats.hits, char1.stats.batterStats.doubles, 
													                          char1.stats.batterStats.triples, char1.stats.batterStats.homeRuns,
                                                    char1.stats.batterStats.rbi, char1.stats.batterStats.runs, 
                                                    char1.stats.batterStats.strikeouts, char1.stats.batterStats.walks, 
                                                    char1.stats.batterStats.hitByPitch, char1.stats.batterStats.sacrifices, char1.stats.batterStats.average, 
                                                    char1.stats.batterStats.obp, char1.stats.batterStats.slg, 
                                                    char1.stats.batterStats.ops, char1.stats.batterStats.stolenBases, char1.stats.batterStats.caughtStealing], 
                                                    [char1.stats.pitcherStats.IP, char1.stats.pitcherStats.gamesPitched, 
                                                     char1.stats.pitcherStats.walks, char1.stats.pitcherStats.hits, 
                                                     char1.stats.pitcherStats.runs, char1.stats.pitcherStats.earnedRuns, char1.stats.pitcherStats.homeRuns, 
                                                     char1.stats.pitcherStats.era, char1.stats.pitcherStats.wins, char1.stats.pitcherStats.losses, 
                                                     char1.stats.pitcherStats.saves, char1.stats.pitcherStats.holds, char1.stats.pitcherStats.WHIP, 
                                                     char1.stats.pitcherStats.strikeouts, char1.stats.pitcherStats.hitByPitch], 
                                                     [char1.stats.defensiveStats.nicePlays, char1.stats.defensiveStats.putOuts, char1.stats.defensiveStats.errors]]]) 
        char2 = team.charTwo
        characterValues.append([char2.name, char2.type, char2.is_captain, char2.hit, char2.pitch, char2.field, char2.run, 
                               char2.overall, char2.png, char2.good_chemistry, char2.bad_chemistry, 
                               [char2.stats.war, [char2.stats.batterStats.pa, char2.stats.batterStats.atBats, 
													                          char2.stats.batterStats.hits, char2.stats.batterStats.doubles, 
													                          char2.stats.batterStats.triples, char2.stats.batterStats.homeRuns,
                                                    char2.stats.batterStats.rbi, char2.stats.batterStats.runs, 
                                                    char2.stats.batterStats.strikeouts, char2.stats.batterStats.walks, 
                                                    char2.stats.batterStats.hitByPitch, char2.stats.batterStats.sacrifices, char2.stats.batterStats.average, 
                                                    char2.stats.batterStats.obp, char2.stats.batterStats.slg, 
                                                    char2.stats.batterStats.ops, char2.stats.batterStats.stolenBases, char2.stats.batterStats.caughtStealing], 
                                                    [char2.stats.pitcherStats.IP, char2.stats.pitcherStats.gamesPitched, 
                                                     char2.stats.pitcherStats.walks, char2.stats.pitcherStats.hits, 
                                                     char2.stats.pitcherStats.runs, char2.stats.pitcherStats.earnedRuns, char2.stats.pitcherStats.homeRuns, 
                                                     char2.stats.pitcherStats.era, char2.stats.pitcherStats.wins, char2.stats.pitcherStats.losses, 
                                                     char2.stats.pitcherStats.saves, char2.stats.pitcherStats.holds, char2.stats.pitcherStats.WHIP, 
                                                     char2.stats.pitcherStats.strikeouts, char2.stats.pitcherStats.hitByPitch], 
                                                     [char2.stats.defensiveStats.nicePlays, char2.stats.defensiveStats.putOuts, char2.stats.defensiveStats.errors]]]) 
        char3 = team.charThree
        characterValues.append([char3.name, char3.type, char3.is_captain, char3.hit, char3.pitch, char3.field, char3.run, 
                               char3.overall, char3.png, char3.good_chemistry, char3.bad_chemistry, 
                               [char3.stats.war, [char3.stats.batterStats.pa, char3.stats.batterStats.atBats, 
													                          char3.stats.batterStats.hits, char3.stats.batterStats.doubles, 
													                          char3.stats.batterStats.triples, char3.stats.batterStats.homeRuns,
                                                    char3.stats.batterStats.rbi, char3.stats.batterStats.runs, 
                                                    char3.stats.batterStats.strikeouts, char3.stats.batterStats.walks, 
                                                    char3.stats.batterStats.hitByPitch, char3.stats.batterStats.sacrifices, char3.stats.batterStats.average, 
                                                    char3.stats.batterStats.obp, char3.stats.batterStats.slg, 
                                                    char3.stats.batterStats.ops, char3.stats.batterStats.stolenBases, char3.stats.batterStats.caughtStealing], 
                                                    [char3.stats.pitcherStats.IP, char3.stats.pitcherStats.gamesPitched, 
                                                     char3.stats.pitcherStats.walks, char3.stats.pitcherStats.hits, 
                                                     char3.stats.pitcherStats.runs, char3.stats.pitcherStats.earnedRuns, char3.stats.pitcherStats.homeRuns, 
                                                     char3.stats.pitcherStats.era, char3.stats.pitcherStats.wins, char3.stats.pitcherStats.losses, 
                                                     char3.stats.pitcherStats.saves, char3.stats.pitcherStats.holds, char3.stats.pitcherStats.WHIP, 
                                                     char3.stats.pitcherStats.strikeouts, char3.stats.pitcherStats.hitByPitch], 
                                                     [char3.stats.defensiveStats.nicePlays, char3.stats.defensiveStats.putOuts, char3.stats.defensiveStats.errors]]]) 
    
        char4 = team.charFour
        characterValues.append([char4.name, char4.type, char4.is_captain, char4.hit, char4.pitch, char4.field, char4.run, 
                               char4.overall, char4.png, char4.good_chemistry, char4.bad_chemistry, 
                               [char4.stats.war, [char4.stats.batterStats.pa, char4.stats.batterStats.atBats, 
													                          char4.stats.batterStats.hits, char4.stats.batterStats.doubles, 
													                          char4.stats.batterStats.triples, char4.stats.batterStats.homeRuns,
                                                    char4.stats.batterStats.rbi, char4.stats.batterStats.runs, 
                                                    char4.stats.batterStats.strikeouts, char4.stats.batterStats.walks, 
                                                    char4.stats.batterStats.hitByPitch, char4.stats.batterStats.sacrifices, char4.stats.batterStats.average, 
                                                    char4.stats.batterStats.obp, char4.stats.batterStats.slg, 
                                                    char4.stats.batterStats.ops, char4.stats.batterStats.stolenBases, char4.stats.batterStats.caughtStealing], 
                                                    [char4.stats.pitcherStats.IP, char4.stats.pitcherStats.gamesPitched, 
                                                     char4.stats.pitcherStats.walks, char4.stats.pitcherStats.hits, 
                                                     char4.stats.pitcherStats.runs, char4.stats.pitcherStats.earnedRuns, char4.stats.pitcherStats.homeRuns, 
                                                     char4.stats.pitcherStats.era, char4.stats.pitcherStats.wins, char4.stats.pitcherStats.losses, 
                                                     char4.stats.pitcherStats.saves, char4.stats.pitcherStats.holds, char4.stats.pitcherStats.WHIP, 
                                                     char4.stats.pitcherStats.strikeouts, char4.stats.pitcherStats.hitByPitch], 
                                                     [char4.stats.defensiveStats.nicePlays, char4.stats.defensiveStats.putOuts, char4.stats.defensiveStats.errors]]]) 
    
        char5 = team.charFive
        characterValues.append([char5.name, char5.type, char5.is_captain, char5.hit, char5.pitch, char5.field, char5.run, 
                               char5.overall, char5.png, char5.good_chemistry, char5.bad_chemistry, 
                               [char5.stats.war, [char5.stats.batterStats.pa, char5.stats.batterStats.atBats, 
													                          char5.stats.batterStats.hits, char5.stats.batterStats.doubles, 
													                          char5.stats.batterStats.triples, char5.stats.batterStats.homeRuns,
                                                    char5.stats.batterStats.rbi, char5.stats.batterStats.runs, 
                                                    char5.stats.batterStats.strikeouts, char5.stats.batterStats.walks, 
                                                    char5.stats.batterStats.hitByPitch, char5.stats.batterStats.sacrifices, char5.stats.batterStats.average, 
                                                    char5.stats.batterStats.obp, char5.stats.batterStats.slg, 
                                                    char5.stats.batterStats.ops, char5.stats.batterStats.stolenBases, char5.stats.batterStats.caughtStealing], 
                                                    [char5.stats.pitcherStats.IP, char5.stats.pitcherStats.gamesPitched, 
                                                     char5.stats.pitcherStats.walks, char5.stats.pitcherStats.hits, 
                                                     char5.stats.pitcherStats.runs, char5.stats.pitcherStats.earnedRuns, char5.stats.pitcherStats.homeRuns, 
                                                     char5.stats.pitcherStats.era, char5.stats.pitcherStats.wins, char5.stats.pitcherStats.losses, 
                                                     char5.stats.pitcherStats.saves, char5.stats.pitcherStats.holds, char5.stats.pitcherStats.WHIP, 
                                                     char5.stats.pitcherStats.strikeouts, char5.stats.pitcherStats.hitByPitch], 
                                                     [char5.stats.defensiveStats.nicePlays, char5.stats.defensiveStats.putOuts, char5.stats.defensiveStats.errors]]]) 
        char6 = team.charSix
        characterValues.append([char6.name, char6.type, char6.is_captain, char6.hit, char6.pitch, char6.field, char6.run, 
                               char6.overall, char6.png, char6.good_chemistry, char6.bad_chemistry, 
                               [char6.stats.war, [char6.stats.batterStats.pa, char6.stats.batterStats.atBats, 
													                          char6.stats.batterStats.hits, char6.stats.batterStats.doubles, 
													                          char6.stats.batterStats.triples, char6.stats.batterStats.homeRuns,
                                                    char6.stats.batterStats.rbi, char6.stats.batterStats.runs, 
                                                    char6.stats.batterStats.strikeouts, char6.stats.batterStats.walks, 
                                                    char6.stats.batterStats.hitByPitch, char6.stats.batterStats.sacrifices, char6.stats.batterStats.average, 
                                                    char6.stats.batterStats.obp, char6.stats.batterStats.slg, 
                                                    char6.stats.batterStats.ops, char6.stats.batterStats.stolenBases, char6.stats.batterStats.caughtStealing], 
                                                    [char6.stats.pitcherStats.IP, char6.stats.pitcherStats.gamesPitched, 
                                                     char6.stats.pitcherStats.walks, char6.stats.pitcherStats.hits, 
                                                     char6.stats.pitcherStats.runs, char6.stats.pitcherStats.earnedRuns, char6.stats.pitcherStats.homeRuns, 
                                                     char6.stats.pitcherStats.era, char6.stats.pitcherStats.wins, char6.stats.pitcherStats.losses, 
                                                     char6.stats.pitcherStats.saves, char6.stats.pitcherStats.holds, char6.stats.pitcherStats.WHIP, 
                                                     char6.stats.pitcherStats.strikeouts, char6.stats.pitcherStats.hitByPitch], 
                                                     [char6.stats.defensiveStats.nicePlays, char6.stats.defensiveStats.putOuts, char6.stats.defensiveStats.errors]]])

        char7 = team.charSeven
        characterValues.append([char7.name, char7.type, char7.is_captain, char7.hit, char7.pitch, char7.field, char7.run, 
                               char7.overall, char7.png, char7.good_chemistry, char7.bad_chemistry, 
                               [char7.stats.war, [char7.stats.batterStats.pa, char7.stats.batterStats.atBats, 
													                          char7.stats.batterStats.hits, char7.stats.batterStats.doubles, 
													                          char7.stats.batterStats.triples, char7.stats.batterStats.homeRuns,
                                                    char7.stats.batterStats.rbi, char7.stats.batterStats.runs, 
                                                    char7.stats.batterStats.strikeouts, char7.stats.batterStats.walks, 
                                                    char7.stats.batterStats.hitByPitch, char7.stats.batterStats.sacrifices, char7.stats.batterStats.average, 
                                                    char7.stats.batterStats.obp, char7.stats.batterStats.slg, 
                                                    char7.stats.batterStats.ops, char7.stats.batterStats.stolenBases, char7.stats.batterStats.caughtStealing], 
                                                    [char7.stats.pitcherStats.IP, char7.stats.pitcherStats.gamesPitched, 
                                                     char7.stats.pitcherStats.walks, char7.stats.pitcherStats.hits, 
                                                     char7.stats.pitcherStats.runs, char7.stats.pitcherStats.earnedRuns, char7.stats.pitcherStats.homeRuns, 
                                                     char7.stats.pitcherStats.era, char7.stats.pitcherStats.wins, char7.stats.pitcherStats.losses, 
                                                     char7.stats.pitcherStats.saves, char7.stats.pitcherStats.holds, char7.stats.pitcherStats.WHIP, 
                                                     char7.stats.pitcherStats.strikeouts, char7.stats.pitcherStats.hitByPitch], 
                                                     [char7.stats.defensiveStats.nicePlays, char7.stats.defensiveStats.putOuts, char7.stats.defensiveStats.errors]]])
    
        char8 = team.charEight
        characterValues.append([char8.name, char8.type, char8.is_captain, char8.hit, char8.pitch, char8.field, char8.run, 
                               char8.overall, char8.png, char8.good_chemistry, char8.bad_chemistry, 
                               [char8.stats.war, [char8.stats.batterStats.pa, char8.stats.batterStats.atBats, 
													                          char8.stats.batterStats.hits, char8.stats.batterStats.doubles, 
													                          char8.stats.batterStats.triples, char8.stats.batterStats.homeRuns,
                                                    char8.stats.batterStats.rbi, char8.stats.batterStats.runs, 
                                                    char8.stats.batterStats.strikeouts, char8.stats.batterStats.walks, 
                                                    char8.stats.batterStats.hitByPitch, char8.stats.batterStats.sacrifices, char8.stats.batterStats.average, 
                                                    char8.stats.batterStats.obp, char8.stats.batterStats.slg, 
                                                    char8.stats.batterStats.ops, char8.stats.batterStats.stolenBases, char8.stats.batterStats.caughtStealing], 
                                                    [char8.stats.pitcherStats.IP, char8.stats.pitcherStats.gamesPitched, 
                                                     char8.stats.pitcherStats.walks, char8.stats.pitcherStats.hits, 
                                                     char8.stats.pitcherStats.runs, char8.stats.pitcherStats.earnedRuns, char8.stats.pitcherStats.homeRuns, 
                                                     char8.stats.pitcherStats.era, char8.stats.pitcherStats.wins, char8.stats.pitcherStats.losses, 
                                                     char8.stats.pitcherStats.saves, char8.stats.pitcherStats.holds, char8.stats.pitcherStats.WHIP, 
                                                     char8.stats.pitcherStats.strikeouts, char8.stats.pitcherStats.hitByPitch], 
                                                     [char8.stats.defensiveStats.nicePlays, char8.stats.defensiveStats.putOuts, char8.stats.defensiveStats.errors]]])
        
        char9 = team.charNine
        characterValues.append([char9.name, char9.type, char9.is_captain, char9.hit, char9.pitch, char9.field, char9.run, 
                               char9.overall, char9.png, char9.good_chemistry, char9.bad_chemistry, 
                               [char9.stats.war, [char9.stats.batterStats.pa, char9.stats.batterStats.atBats, 
													                          char9.stats.batterStats.hits, char9.stats.batterStats.doubles, 
													                          char9.stats.batterStats.triples, char9.stats.batterStats.homeRuns,
                                                    char9.stats.batterStats.rbi, char9.stats.batterStats.runs, 
                                                    char9.stats.batterStats.strikeouts, char9.stats.batterStats.walks, 
                                                    char9.stats.batterStats.hitByPitch, char9.stats.batterStats.sacrifices, char9.stats.batterStats.average, 
                                                    char9.stats.batterStats.obp, char9.stats.batterStats.slg, 
                                                    char9.stats.batterStats.ops, char9.stats.batterStats.stolenBases, char9.stats.batterStats.caughtStealing], 
                                                    [char9.stats.pitcherStats.IP, char9.stats.pitcherStats.gamesPitched, 
                                                     char9.stats.pitcherStats.walks, char9.stats.pitcherStats.hits, 
                                                     char9.stats.pitcherStats.runs, char9.stats.pitcherStats.earnedRuns, char9.stats.pitcherStats.homeRuns, 
                                                     char9.stats.pitcherStats.era, char9.stats.pitcherStats.wins, char9.stats.pitcherStats.losses, 
                                                     char9.stats.pitcherStats.saves, char9.stats.pitcherStats.holds, char9.stats.pitcherStats.WHIP, 
                                                     char9.stats.pitcherStats.strikeouts, char9.stats.pitcherStats.hitByPitch], 
                                                     [char9.stats.defensiveStats.nicePlays, char9.stats.defensiveStats.putOuts, char9.stats.defensiveStats.errors]]]) 
        
        teamCharacterValues[team.name] = characterValues

        if (team.name == userTeam):
            teamIndex = index
        
        index = index + 1
    
    # Returning to show in reactjs
    return {
        'teams':teamList,
        'playerValues':teamCharacterValues,
        'teamIndex':teamIndex
    }

# Route for seeing state data
@app.route('/divisions')
def get_divisions():
    api = MiddlewareAPI()
    divisions = [Strings.MUSHROOM_DIVISION, Strings.FLOWER_DIVISION]

    div_one_teams_raw = api.get_teams_by_division(divisions[0])
    div_one_teams = []

    for div_one_team in div_one_teams_raw:
        team = Team()
        team.name = div_one_team[0]
        stats = TeamStats()

        # id, overall, wins, losses, ties
        team_stats = api.get_team_stats(team)
        stats.setup(team_stats)
        team.stats = stats
        
        div_one_teams.append(team)
    
    div_two_teams_raw = api.get_teams_by_division(divisions[1])
    div_two_teams = []

    for div_two_team in div_two_teams_raw:
        team = Team()
        team.name = div_two_team[0]
        stats = TeamStats()

        # id, overall, wins, losses, ties
        team_stats = api.get_team_stats(team)
        stats.setup(team_stats)
        team.stats = stats

        div_two_teams.append(team)
    
    # Order them by winning %
    div_one_teams.sort(key=lambda x: x.stats.winning_percentage, reverse=True)
    div_two_teams.sort(key=lambda x: x.stats.winning_percentage, reverse=True)

    div_one_data = []
    gb_most = div_one_teams[0].stats.wins-div_one_teams[0].stats.losses

    for team in div_one_teams:
        gb = (gb_most-(team.stats.wins-team.stats.losses))/2
        if (gb == 0):
            gb = "-"
        div_one_data.append([team.name, team.stats.wins, team.stats.losses, team.stats.ties, gb])
    
    div_two_data = []
    gb_most = div_two_teams[0].stats.wins-div_two_teams[0].stats.losses

    for team in div_two_teams:
        gb = (gb_most-(team.stats.wins-team.stats.losses))/2
        if (gb == 0):
            gb = "-"
        div_two_data.append([team.name, team.stats.wins, team.stats.losses, team.stats.ties, gb])

    # Returning to show in reactjs
    return {
        'divisions':divisions,
        'divisionOneTeams': div_one_data,
        'divisionTwoTeams': div_two_data
    }
     
# Running app
if __name__ == '__main__':
    app.run()