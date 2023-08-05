import sqlite3
from backendAPI import BackendAPI

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