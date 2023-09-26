import random
from backendAPI import BackendAPI

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Strings import *
from Shared.Team import Team

WILDCARD = "*"

class MiddlewareAPI():
    def __init__(self):
        self.backend = BackendAPI()
        self.cursor, self.connection = self.backend.connect()
        self.championship_round = 2

    # Example
    def get_all_character_names(self):
        results = self.backend.get_all_character_names()
        return results
    
    #################################################
    ############# Main In Season Screen #############
    #################################################

    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo   
    def get_user_team(self):
       results = self.backend.get_player_team()
       return results[0][0]
    
    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo   
    def get_team_by_name(self, name):
        results = self.backend.get_team(name)
        return results[0][0]

     # returns [name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo]   
    def get_teams_by_division(self, div):
        results = self.backend.get_teams_by_division(div)
        
        return results
    
    # returns [id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID] 
    def get_players_by_team(self, team):
        results = self.backend.get_player_ids_by_team(team)
        players = []

        for id in results[0]:
            player = self.backend.get_player_by_id(id)
            players.append(player)

        return players[0][0]

    # returns id, state, version, season (year)
    def get_franchise(self):
        results = self.backend.get_franchise()
        return results[0]
    
    # returns id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_previous_game(self):
        results = self.get_user_team()
        user_team = results

        results = self.get_year()
        year = results

        results = self.backend.get_season(year)     
        current_game = results[0][5] - 1

        results = self.backend.get_previous_game(user_team, current_game)
        return results[0]
    
    # returns id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_next_game(self):
        results = self.get_user_team()
        user_team = results

        results = self.get_year()
        year = results

        results = self.backend.get_season(year)     
        current_game = results[0][5]

        results = self.backend.get_next_game(current_game, user_team)
        return results[0]
    
    # returns year
    def get_year(self):
        results = self.backend.get_year()
        return results[0][0] 

    #################################################
    ############# Play Game Screen #############
    #################################################

    def update_character_stats(self, character):
        name = character.name
        char_type = character.type
        
        results = self.backend.get_player_by_name(name, char_type)

        id = results[0][0]
        
        stats_id = self.backend.get_player_stats(id)[0][0]

        self.backend.update_war(stats_id, character.stats.war)

        self.backend.set_defensive_stats(stats_id, character.stats)
        self.backend.set_pitching_stats(stats_id, character.stats)
        self.backend.set_batter_stats(stats_id, character.stats)

    def update_team_stats(self, team):
        results = self.backend.get_team_stats(team.name)
        id = results[0][0]

        self.backend.set_team_stats(team.stats, id)

    def set_game_results(self, game):
        results = self.backend.get_game(game.gameNumber, game.homeTeam.name, game.awayTeam.name)
        id = results[0][0]

        self.backend.set_game_result(game, id)

    #################################################
    ############# Draft Screen #############
    #################################################

    # [id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID] 
    def get_captains(self):
        results = self.backend.get_captains()
        return results
    
    def add_team(self, team, division, isPlayer):
        div_id = division.name
        stadium_id = STADIUM_MAPPING[team.name]
        logo = stadium_id + " logo.png"

        self.backend.add_to_team_stats()

        team_id = self.backend.get_newest_team_id()

        self.backend.add_team(team.name, team_id, stadium_id, div_id, logo, isPlayer)

    def add_player_to_team(self, team, player):
        char_id = self.backend.get_player_by_name(player.name, player.type)[0][0]

        team_full = self.backend.get_team(team.name)[0]
        charNumSt = "char"

        if (team_full[1] == None):
            charNumSt += "One"
        elif (team_full[2] == None):
            charNumSt += "Two"
        elif (team_full[3] == None):
            charNumSt += "Three"
        elif (team_full[4] == None):
            charNumSt += "Four"
        elif (team_full[5] == None):
            charNumSt += "Five"
        elif (team_full[6] == None):
            charNumSt += "Six"
        elif (team_full[7] == None):
            charNumSt += "Seven"
        elif (team_full[8] == None):
            charNumSt += "Eight"
        elif (team_full[9] == None):
            charNumSt += "Nine"

        self.backend.add_player_to_team(team.name, char_id, charNumSt)

    # bool
    def check_if_player_is_on_team(self, character):
        char_id = self.backend.get_player_by_name(character.name, character.type)[0][0]
        results = self.backend.check_if_player_is_on_any_team(char_id)

        onTeam = (len(results) > 0)

        return onTeam
    
    # id
    def get_character_id(self, character):
        char_id = self.backend.get_player_by_name(character.name, character.type)[0]

        return char_id[0]
    
    def set_user_team(self, team):
        self.backend.set_user_team(team.name)

    # name
    def get_stadium(self, team):
        stadium = self.backend.get_stadium(team.name)[0]

        return stadium[0]
    
    # name
    def get_division(self, team):
        div = self.backend.get_division(team.name)[0]

        return div[0]
    
    def create_game(self, gameNum, home, away):
        stadium = self.get_stadium(home)
        id = self.backend.create_game(gameNum, stadium, home.name, away.name)
        return id
    
    #################################################
    ############# Playoffs Screen #############
    #################################################

    # round
    def get_round(self):
        results = self.backend.get_round()[0][0]
        return results
    
    # series_id
    def create_series(self, lowerSeed, higherSeed, round):
        gameOne = self.create_game(1, higherSeed, lowerSeed)
        gameTwo = self.create_game(2, higherSeed, lowerSeed)
        gameThree = self.create_game(3, lowerSeed, higherSeed)
        gameFour = self.create_game(4, lowerSeed, higherSeed)
        gameFive = self.create_game(5, lowerSeed, higherSeed)
        gameSix = self.create_game(6, higherSeed, lowerSeed)
        gameSeven = self.create_game(7, higherSeed, lowerSeed)
        
        series_id = self.backend.create_playoff_series(round, higherSeed.name, lowerSeed.name, gameOne, gameTwo, gameThree, gameFour, gameFive, gameSix, gameSeven)
        return series_id

    def advance_round(self):
        playoffs = self.backend.get_playoffs()[0]

        roundOneDivOne = playoffs[2]
        roundOneDivTwo = playoffs[3]

        seriesOne = self.backend.get_playoff_series(roundOneDivOne)[0]
        seriesOneWinner = seriesOne[13]

        seriesTwo = self.backend.get_playoff_series(roundOneDivTwo)[0]
        seriesTwoWinner = seriesTwo[13]
        
        # Get seeding
        teamOne = self.backend.get_team(seriesOneWinner)[0]
        teamOneStatsID = teamOne[10]
        teamOneWins = self.backend.select_wins(teamOneStatsID)[0][0]

        teamTwo = self.backend.get_team(seriesTwoWinner)[0]
        teamTwoStatsID = teamTwo[10]
        teamTwoWins = self.backend.select_wins(teamTwoStatsID)[0][0]

        higherSeed = ""
        lowerSeed = ""

        if (teamOneWins > teamTwoWins):
            higherSeed = teamOne
            lowerSeed = teamTwo
        elif (teamTwoWins > teamOneWins):
            higherSeed = teamTwo
            lowerSeed = teamOne
        else:
            randomNum = random.randrange(1, 100)

            if (randomNum > 50):
                higherSeed = teamOne
                lowerSeed = teamTwo
            else:
                higherSeed = teamTwo
                lowerSeed = teamOne

        # Create Series
        highSeedTeam = Team()
        lowSeedTeam = Team()
        highSeedTeam.name = higherSeed[0]
        lowSeedTeam.name = lowerSeed[0]

        seriesID = self.create_series(highSeedTeam, lowSeedTeam, self.championship_round)

        self.backend.advance_round(self.championship_round, seriesID)

    def update_series(self, winner, loser):
        series = self.get_playoff_series(winner, loser)[0]
    
        series_id = series[0]
        highSeed = series[2]
 
        highSeedWins = series[4]
        lowSeedWins = series[5]

        team = 'lowSeed'
        wins = lowSeedWins + 1
        if (winner.name.upper() == highSeed.upper()):
            team = 'highSeed'
            wins = highSeedWins + 1

        # Need series ID, highSeed or lowSeed, team seed wins
        self.backend.update_playoff_series(series_id, team, wins)

    def end_series(self, winner):
        self.backend.end_playoff_series(winner.name)

    def create_playoffs(self):
        # Division One
        div_one = MUSHROOM_DIVISION

        div_one_teams = self.backend.get_division_rankings(div_one)
        div_one_lower = Team()
        div_one_lower.name = div_one_teams[1][0]

        div_one_higher = Team()
        div_one_higher.name = div_one_teams[0][0]

        div_one_id = self.create_series(div_one_lower, div_one_higher, 1)    

        # Division Two
        div_two = FLOWER_DIVISION

        div_two_teams = self.backend.get_division_rankings(div_two)

        div_two_lower = Team()
        div_two_lower.name = div_two_teams[1][0]

        div_two_higher = Team()
        div_two_higher.name = div_two_teams[0][0]

        div_two_id = self.create_series(div_two_lower, div_two_higher, 1)

        self.backend.create_playoffs(div_one_id, div_two_id)

    def end_playoffs(self, champion):
        self.backend.end_playoffs(champion.name)
      
        results = self.backend.get_playoff_winners_and_losers(champion.name)
        
        runner_up = results[0][0]
        if (runner_up == champion.name):
            runner_up = results[0][1]
 
        div_one_semi = results[1][0]
        if (div_one_semi == champion.name):
            div_one_semi = results[1][1]

        results = self.backend.get_playoff_winners_and_losers(runner_up)
     
        div_two_semi = results[0][0]
        if (div_two_semi == runner_up):
            div_two_semi = results[0][1]
 
        franchise = self.backend.get_franchise()
        year = franchise[0][3]

        self.backend.set_previous_season(champion.name, runner_up, div_one_semi, div_two_semi, year)

    # id, overallRound, roundOneDivisionOne Series ID,  roundOneDivisionTwo Series ID, Championship Series ID, Champion Team ID
    def get_playoffs(self):
        results = self.backend.get_playoffs()[0]
        return results
    
    # id, round, highSeed, lowSeed, highSeedWins, lowSeedWins, gameOne..., winner
    def get_playoff_series(self, teamOne, teamTwo):
        results = self.backend.get_playoff_series_by_teams(teamOne.name, teamTwo.name)[0]
        return results

    # name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo
    def get_champion(self):
        champion = self.backend.get_champion()[0][0]
 
        team = self.backend.get_team(champion)[0]
        return team
    
    #################################################
    ############# End of Season Screen #############
    #################################################

    # name, winner, season
    def get_award_winners(self):
        year = self.get_year()[0][0]
        self.backend.get_awards(year)

    def set_awards(self, winners_awards_dict):
        year = self.get_year()[0][0]

        for winner in winners_awards_dict:
            id = self.backend.get_player_by_name(winner.name, winner.type)[0][0]
            self.backend.set_awards(year, id, winners_awards_dict[winner])

    def reset_season(self):
        self.backend.clear_team()
        self.backend.clear_team_stats()
        self.backend.clear_player_stats()
        self.backend.clear_batter_stats()
        self.backend.clear_defensive_stats()
        self.backend.clear_pitching_stats()
        self.backend.clear_playoffs()
        self.backend.clear_playoff_series()
        self.backend.clear_game()

    #################################################
    ############# Previous Seasons Screen #############
    #################################################

    # year, champion, runnerUp, semiFinalsTeamOne, semiFinalsTeamTwo, currentGameNum
    def get_seasons(self):
        seasons = self.backend.get_season(WILDCARD)
        return seasons