import sqlite3
from backendAPI import BackendAPI
from Strings import *

class MiddlewareAPI():
    def __init__(self):
        self.backend = BackendAPI()
        self.cursor, self.connection = self.backend.connect()

    # Example
    def get_all_character_names(self):
        results = self.backend.get_all_character_names()
        return results
    
    #################################################
    ############# Main In Season Screen #############
    #################################################

    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo   
    def get_user_team(self):
        self.cursor.execute('SELECT * FROM Team WHERE playerTeam = 1;')
        results = self.cursor.fetchall()
        return results
    
    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo   
    def get_team_by_name(self, name):
        results = self.backend.get_team(name)
        return results

     # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo   
    def get_teams_by_division(self, div):
        results = self.backend.get_teams_by_division(div)
        
        return results
    
    # returns id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID 
    def get_players_by_team(self, team):
        results = self.backend.get_player_ids_by_team(team)
        players = []

        for id in results[0]:
            player = self.backend.get_player_by_id(id)
            players.append(player)

        return players

    # returns id, state, version, season (year)
    def get_franchise(self):
        results = self.backend.get_franchise()
        return results
    
    # returns id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_previous_game(self):
        results = self.get_user_team()
        user_team = results[0][0]

        results = self.get_year()
        year = results[0][0]

        results = self.backend.get_season(year)     
        current_game = results[0][5] - 1

        results = self.backend.get_previous_game(user_team, current_game)
        return results
    
    # returns id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_next_game(self):
        results = self.get_user_team()
        user_team = results[0][0]

        results = self.get_year()
        year = results[0][0]

        results = self.backend.get_season(year)     
        current_game = results[0][5]

        results = self.backend.get_next_game(current_game, user_team)
        return results
    
    # returns year
    def get_year(self):
        self.cursor.execute("SELECT Year FROM Season ORDER BY Year DESC;")   
        results = self.cursor.fetchall()

        return results 

    #################################################
    ############# Play Game Screen #############
    #################################################

    def update_character_stats(self, character):
        name = character.name
        char_type = character.type
        
        self.cursor.execute("SELECT id FROM Character WHERE name = ? AND type = ?;", (name, char_type))   
        results = self.cursor.fetchall()
        id = results[0][0]
        
        stats_id = self.backend.get_player_stats(id)

        self.backend.update_war(stats_id, character.war)

        self.backend.set_defensive_stats(stats_id, character.stats)
        self.backend.set_pitching_stats(stats_id, character.stats)
        self.backend.set_batter_stats(stats_id, character.stats)

    def update_team_stats(self, team):
        self.cursor.execute("SELECT stats FROM Team WHERE name = ?;", (team.name,))   
        results = self.cursor.fetchall()
        id = results[0][0]

        self.backend.set_team_stats(team.stats, id)

    def set_game_results(self, game):
        self.cursor.execute("SELECT id FROM Team WHERE name = ?;", (game.awayTeam.name))   
        results = self.cursor.fetchall()
        away_id = results[0][0]

        self.cursor.execute("SELECT id FROM Team WHERE name = ?;", (game.homeTeam.name))   
        results = self.cursor.fetchall()
        home_id = results[0][0]

        self.cursor.execute("SELECT id FROM Game WHERE gameNumber = ? AND homeTeam = ? AND awayTeam = ?;", (game.gameNumber, home_id, away_id))   
        results = self.cursor.fetchall()
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
        div_id = self.backend.get_division_id(division)[0]
        stadium = STADIUM_MAPPING[team.name]
        stadium_id = self.backend.get_stadium_id(stadium)[0]
        logo = stadium + " logo.png"

        self.backend.cursor.execute('INSERT INTO TeamStats')
        self.backend.connection.commit() 

        self.backend.cursor.execute('SELECT id FROM TeamStats;')
        results = self.cursor.fetchall()
        team_id = len(results)

        self.backend.add_team(team, team_id, stadium_id, div_id, logo, isPlayer)

    def add_player_to_team(self, team, player):
        char_id = self.backend.get_player_by_name(player.name, player.type)[0]

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
        char_id = self.backend.get_player_by_name(character.name, character.type)[0]
        results = self.backend.check_if_player_is_on_any_team(char_id)

        onTeam = (len(results) > 0)

        return onTeam
    
    # id
    def get_character_id(self,character):
        char_id = self.backend.get_player_by_name(character.name, character.type)[0]

        return char_id
    
    def set_user_team(self, team):
        self.backend.set_user_team(team.name)

    # name
    def get_stadium(self, team):
        stadium = self.backend.get_stadium(team.name)[0]

        return stadium
    
    # name
    def get_division(self, team):
        div = self.backend.get_division(team.name)[0]

        return div
    
    def create_game(self, gameNum, home, away):
        stadium = self.get_stadium(home.name)[0]
        self.backend.create_game(gameNum, stadium, home.name, away.name)