import sqlite3

class BackendAPI():
    def __init__(self):
        self.cursor, self.connection = self.connect()
      
    # Generic connect and close methods
    def connect(self):
        connection = sqlite3.connect('./mario.db')
        cursor = connection.cursor()
        return cursor, connection

    def close(self, connection):
        # Save the changes
        connection.commit()
        connection.close()

    # Example
    def get_all_character_names(self):
        self.cursor.execute('SELECT name, type FROM Character;')
        results = self.cursor.fetchall()
        return results
    
    #################################################
    ############# Main In Season Screen #############
    #################################################

    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo
    def get_all_teams(self):
        self.cursor.execute('SELECT * FROM Team;')
        results = self.cursor.fetchall()
        return results
    
    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo
    def get_team(self, name):
        self.cursor.execute('SELECT * FROM Team WHERE name = ?;', (name,))
        results = self.cursor.fetchall()
        return results
    
    # returns name, CharOneID, ... CharNineID, TeamStatsID, Stadium, Division, PlayerTeam (int), logo
    def get_player_team(self):
        self.cursor.execute('SELECT * FROM Team WHERE playerTeam = ?;', (1,))
        results = self.cursor.fetchall()
        return results

    # id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID 
    def get_teams_by_division(self, division):
        self.cursor.execute('SELECT * FROM Team WHERE division = ?;', (division))
        results = self.cursor.fetchall()
        return results
    
    # id, AB, BA, BB, HBP, K, S, D, T, HR, SAC, RBI, R, OBP, SLG, SB, CS
    def get_batter_stats(self, id):
        self.cursor.execute('SELECT * FROM BatterStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results

    # id, IP, GamesPitched, BB, H, R, ER, HR, ERA< W, L, S, HD, WHIP, K
    def get_pitcher_stats(self, id):
        self.cursor.execute('SELECT * FROM PitchingStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # id, IP, GamesPitched, BB, H, R, ER, HR, ERA, W, L, S, HD, WHIP, K
    def get_defensive_stats(self, id):
        self.cursor.execute('SELECT * FROM DefensiveStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # id, WAR, battingStats ID, defensiveStats ID, pitchingStats ID
    def get_player_stats(self, id):
        self.cursor.execute('SELECT * FROM PlayerStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID 
    def get_player_by_id(self, id):
        self.cursor.execute('SELECT * FROM Character WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results

    # id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID 
    def get_player_by_name(self, name, chType):
        self.cursor.execute('SELECT * FROM Character WHERE name = ? AND type = ?;', (name, chType))
        results = self.cursor.fetchall()
        return results
    
    # id, state, version, season (year)
    def get_franchise(self):
        self.cursor.execute('SELECT * FROM Franchise;')
        results = self.cursor.fetchall()
        return results

    # id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_previous_game(self, userTeamID):
        self.cursor.execute('SELECT * FROM Game WHERE (homeTeam = ? OR awayTeam = ?);', (userTeamID, userTeamID))
        results = self.cursor.fetchall()
        return results
    
    # id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_next_game(self, nextGameNum, userTeamID):
        self.cursor.execute('SELECT * FROM Game WHERE gameNumber = ? AND (homeTeeam = ? OR awayTeam = ?);', (nextGameNum, userTeamID, userTeamID))
        results = self.cursor.fetchall()
        return results
    
    #################################################
    ################# Play Game Screen ##############
    #################################################

    def set_batter_stats(self, batterStatsID, playerStats):
        batterStats = playerStats.batterStats
        self.cursor.execute('UPDATE BatterStats SET atBats=?, BA=?, walks=?, hbp=?, strikeouts=?, singles=?, doubles=?, triples=?, homeruns=?, sacrifices=?, rbi=?, runs=?, obp=?, slg=?, stolenbases=?, caughtStealing=? WHERE id=?;', (batterStats.atBats, batterStats.average, batterStats.walks, batterStats.hitByPitch, batterStats.strikeouts, batterStats.singles, batterStats.doubles, batterStats.triples, batterStats.homeRuns, batterStats.sacrifices, batterStats.rbi, batterStats.runs, batterStats.obp, batterStats.slg, batterStats.stolenBases, batterStats.caughtStealing, batterStatsID))
        self.connection.commit()

    def set_pitching_stats(self, pitchingStatsID, playerStats):
        pitcherStats = playerStats.pitcherStats
        self.cursor.execute('UPDATE BatterStats SET IP=?, gamesPitched=?, walks=?, hits=?, runs=?, earnedRuns=?, homeRuns=?, era=?, wins=?, losses=?, saves=?, holds=?, whip=?, strikeouts=?, hitByPitch=? WHERE id=?;', (pitcherStats.IP, pitcherStats.gamesPitched, pitcherStats.walks, pitcherStats.hits, pitcherStats.runs, pitcherStats.earnedRuns, pitcherStats.homeRuns, pitcherStats.era, pitcherStats.wins, pitcherStats.losses, pitcherStats.saves, pitcherStats.holds, pitcherStats.WHIP, pitcherStats.strikeouts, pitcherStats.hitByPitch, pitchingStatsID))
        self.connection.commit()

    def set_defensive_stats(self, defensiveStatsID, playerStats):
        defensiveStats = playerStats.defensiveStats
        self.cursor.execute('UPDATE DefensiveStats SET nicePlays=?, putOuts=?, errors=? WHERE id=?;', (defensiveStats.nicePlays, defensiveStats.putOuts, defensiveStats.errors, defensiveStatsID))
        self.connection.commit()
    
    def update_war(self, playerStatsID, war):
        self.cursor.execute('UPDATE PlayerStats SET WAR=? WHERE id=?;', (war, playerStatsID))
        self.connection.commit()

    def set_team_stats(self, teamStats, teamStatsID):
        self.cursor.execute('UPDATE Team SET overall=?, wins=?, losses=?, ties=? WHERE id=?;', (teamStats.overall, teamStats.wins, teamStats.losses, teamStats.ties, teamStatsID))
        self.connection.commit()  

    def set_game_result(self, game, gameID):
        self.cursor.execute('UPDATE Game SET homeScore=?, awayScore=? WHERE id=?;', (game.homeScore, game.awayScore, gameID))
        self.connection.commit()  

