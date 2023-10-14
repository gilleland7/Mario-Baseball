import sqlite3

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Strings import *

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
        self.cursor.execute('SELECT * FROM Team WHERE division = ?;', (division,))
        results = self.cursor.fetchall()
        return results
    
    # id, AB, BA, BB, HBP, K, S, D, T, HR, SAC, RBI, R, OBP, SLG, SB, CS
    def get_batter_stats(self, id):
        self.cursor.execute('SELECT * FROM BatterStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results

    # id, IP, GamesPitched, BB, H, R, ER, HR, ERA, W, L, S, HD, WHIP, K
    def get_pitcher_stats(self, id):
        self.cursor.execute('SELECT * FROM PitchingStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # id, nicePlays, putOuts, errors
    def get_defensive_stats(self, id):
        self.cursor.execute('SELECT * FROM DefensiveStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # id, WAR, battingStats ID, defensiveStats ID, pitchingStats ID
    def get_player_stats(self, id):
        self.cursor.execute('SELECT * FROM PlayerStats WHERE id = ?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # idOne, idTwo, ... idNine
    def get_player_ids_by_team(self, team):
        self.cursor.execute('SELECT charOne, charTwo, charThree, charFour, charFive, charSix, charSeven, charEight, charNine FROM Team WHERE name = ?;', (team,))
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
    def get_previous_game(self, userTeamID, gameNum):
        self.cursor.execute('SELECT * FROM Game WHERE (homeTeam = ? OR awayTeam = ?) AND gameNumber = ?;', (userTeamID, userTeamID, gameNum))
        results = self.cursor.fetchall()
        return results
    
    # id, gameNum, stadium ID, homeTeam name, awayTeam name, homeScore, awayScore
    def get_next_game(self, nextGameNum, userTeamID):
        self.cursor.execute('SELECT * FROM Game WHERE gameNumber = ? AND (homeTeam = ? OR awayTeam = ?);', (nextGameNum, userTeamID, userTeamID))
        results = self.cursor.fetchall()
        return results

    # year
    def get_year(self):
        self.cursor.execute("SELECT Year FROM Season ORDER BY Year DESC LIMIT 1;")   
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
        self.cursor.execute('UPDATE PitchingStats SET IP=?, gamesPitched=?, walks=?, hits=?, runs=?, earnedRuns=?, homeRuns=?, era=?, wins=?, losses=?, saves=?, holds=?, whip=?, strikeouts=?, hitByPitch=? WHERE id=?;', (pitcherStats.IP, pitcherStats.gamesPitched, pitcherStats.walks, pitcherStats.hits, pitcherStats.runs, pitcherStats.earnedRuns, pitcherStats.homeRuns, pitcherStats.era, pitcherStats.wins, pitcherStats.losses, pitcherStats.saves, pitcherStats.holds, pitcherStats.WHIP, pitcherStats.strikeouts, pitcherStats.hitByPitch, pitchingStatsID))
        self.connection.commit()

    def set_defensive_stats(self, defensiveStatsID, playerStats):
        defensiveStats = playerStats.defensiveStats
        self.cursor.execute('UPDATE DefensiveStats SET nicePlays=?, putOuts=?, errors=? WHERE id=?;', (defensiveStats.nicePlays, defensiveStats.putOuts, defensiveStats.errors, defensiveStatsID))
        self.connection.commit()
    
    def update_war(self, playerStatsID, war):
        self.cursor.execute('UPDATE PlayerStats SET WAR=? WHERE id=?;', (war, playerStatsID))
        self.connection.commit()

    # stats ID
    def get_team_stats_id(self, name):
        self.cursor.execute("SELECT stats FROM Team WHERE name = ?;", (name,))   
        results = self.cursor.fetchall()
    
        return results
    
    # ID, overall, wins, losses, ties
    def get_team_stats(self, id):
        self.cursor.execute("SELECT * FROM TeamStats WHERE id = ?;", (id,))   
        results = self.cursor.fetchall()
        return results

    # game ID
    def get_game(self, gameNumber, homeTeam, awayTeam):
        self.cursor.execute("SELECT id FROM Game WHERE gameNumber = ? AND homeTeam = ? AND awayTeam = ?;", (gameNumber, homeTeam, awayTeam))   
        results = self.cursor.fetchall()
        return results

    def set_team_stats(self, teamStats, teamStatsID):
        self.cursor.execute('UPDATE TeamStats SET overall=?, wins=?, losses=?, ties=? WHERE id=?;', (teamStats.overall, teamStats.wins, teamStats.losses, teamStats.ties, teamStatsID))
        self.connection.commit()  

    def set_game_result(self, game, gameID):
        self.cursor.execute('UPDATE Game SET homeScore=?, awayScore=? WHERE id=?;', (game.homeScore, game.awayScore, gameID))
        self.connection.commit() 

    #################################################
    ################## Draft Screen #################
    #################################################

     # [id, name, type, isCaptain, bat, pitch, field, run, overall, png, PlayerStats ID] 
    def get_captains(self):
        self.cursor.execute('SELECT * FROM Character WHERE isCaptain = 1;')
        results = self.cursor.fetchall()
        return results
    
    def add_team(self, teamName, teamStatsID, stadium, div, logo, userTeam):
        self.cursor.execute('INSERT INTO Team (name, stats, stadium, division, logo, playerTeam) VALUES (?,?,?,?,?,?)', (teamName, teamStatsID, stadium, div, logo, userTeam))
        self.connection.commit() 
    
    def create_game(self, gameNum, stadium, homeTeam, awayTeam):
        self.cursor.execute('INSERT INTO Game (gameNumber, stadium, homeTeam, awayTeam) VALUES (?,?,?,?)', (gameNum, stadium, homeTeam, awayTeam))
        self.connection.commit() 
        return self.cursor.lastrowid

    # string name
    def get_stadium(self, name):
        self.cursor.execute('SELECT stadium FROM Team WHERE name=?;', (name,))
        results = self.cursor.fetchall()
        return results
    
    # string name
    def get_division(self, name):
        self.cursor.execute('SELECT division FROM Team WHERE name=?;', (name,))
        results = self.cursor.fetchall()
        return results
    
    def add_player_to_team(self, teamName, characterID, charNumSt):
        # Check to make sure input is clean
        if (charNumSt == "charOne" or charNumSt == "charTwo" or charNumSt == "charThree" or charNumSt == "charFour" or charNumSt == "charFive" or charNumSt == "charSix" or charNumSt == "charSeven" or charNumSt == "charEight" or charNumSt == "charNine"):
            self.cursor.execute(f'UPDATE Team SET {charNumSt} =? WHERE name=?;', (characterID, teamName))
            self.connection.commit() 

    # id, characterOneID, characterTwoID, type
    def get_chemistry(self, name, type):
        self.cursor.execute('SELECT * FROM Chemistry WHERE type=? AND (characterOne=? OR characterTWO=?);', (type, name, name))
        results = self.cursor.fetchall()
        return results
    
    # bool
    def check_if_player_is_on_any_team(self, playerID):
        self.cursor.execute('SELECT * FROM TEAM WHERE charOne = ? OR charTwo = ? OR charThree = ? OR charFour = ? OR charFive = ? OR charSix = ? OR charSeven = ? OR charEight = ? OR charNine = ?;',(playerID, playerID, playerID, playerID, playerID, playerID, playerID, playerID, playerID))
        results = self.cursor.fetchall()
        return results
    
    # string type
    def get_player_type(self, playerID):
        self.cursor.execute('SELECT type FROM Character WHERE name=?;', (playerID,))
        results = self.cursor.fetchall()
        return results

    def set_user_team(self, name):
        self.cursor.execute('UPDATE Team SET playerTeam=1 WHERE name=?;', (name,))
        self.connection.commit() 

    def add_to_team_stats(self):
        self.cursor.execute('INSERT INTO TeamStats (overall, wins, losses, ties) VALUES (?,?,?,?)', (0,0,0,0))
        self.connection.commit() 

    # int id of the last team added
    def get_newest_team_id(self):
        self.cursor.execute('SELECT id FROM TeamStats;')
        results = self.cursor.fetchall()
        team_id = len(results)

        return team_id
    
    #################################################
    ################ Playoffs Screen ################
    #################################################

    # round
    def get_round(self):
        self.cursor.execute('SELECT overallRound FROM Playoffs;')
        results = self.cursor.fetchall()
        return results

    def advance_round(self, newRound, championshipID):
        self.cursor.execute('UPDATE Playoffs SET overallRound=?, championship=?;', (newRound, championshipID))
        self.connection.commit() 

    def end_playoffs(self, champTeamID):
        self.cursor.execute('UPDATE Playoffs SET champion=?;', (champTeamID,))
        self.connection.commit() 
    
    # id, overallRound, roundOneDivisionOne Series ID,  roundOneDivisionTwo Series ID, Championship Series ID, Champion Team ID
    def get_playoffs(self):
        self.cursor.execute('SELECT * FROM Playoffs;')
        results = self.cursor.fetchall()
        return results
    
    # id, round, highSeed, lowSeed, highSeedWins, lowSeedWins, gameOne..., winner
    def get_playoff_series(self, id):
        self.cursor.execute('SELECT * FROM PlayoffSeries WHERE id=?;', (id,))
        results = self.cursor.fetchall()
        return results
    
    # id, round, highSeed, lowSeed, highSeedWins, lowSeedWins, gameOne..., winner
    def get_playoff_series_by_teams(self, teamOne, teamTwo):
        self.cursor.execute("SELECT * FROM PlayoffSeries WHERE (highSeed = ? AND lowSeed = ?) OR (highSeed = ? AND lowSeed = ?);", (teamOne, teamTwo, teamTwo, teamOne))
        results = self.cursor.fetchall()

        return results
    
    # series_id
    def create_playoff_series(self, round, highTeamID, lowTeamID, gameOneID, gameTwoID, gameThreeID, gameFourID, gameFiveID, gameSixID, gameSevenID):
        self.cursor.execute('INSERT INTO PlayoffSeries (round, highSeed, lowSeed, gameOne, gameTwo, gameThree, gameFour, gameFive, gameSix, gameSeven) VALUES (?,?,?,?,?,?,?,?,?,?);', (round, highTeamID, lowTeamID, gameOneID, gameTwoID, gameThreeID, gameFourID, gameFiveID, gameSixID, gameSevenID))
        series_id = self.cursor.lastrowid
        self.connection.commit() 

        return series_id
    
    # int id[]
    def get_division_rankings(self, div):
        self.cursor.execute("SELECT Team.name FROM Team INNER JOIN TeamStats ON TeamStats.id=Team.stats WHERE Team.division = ? ORDER BY TeamStats.wins DESC LIMIT 2;", (div,))
        results = self.cursor.fetchall()
        return results

    def create_playoffs(self, roundOneDivOneID, roundOneDivTwoID):
        self.cursor.execute('INSERT INTO Playoffs (overallRound, roundOneDivisionOne, roundOneDivisionTwo) VALUES (?,?,?);', (1, roundOneDivOneID, roundOneDivTwoID))
        self.connection.commit()

    def update_playoff_series(self, id, winner, amount):
        # Safety check
        if (winner == "highSeed" or wins == "lowSeed"):
            wins = winner + "wins"
            self.cursor.execute(f'UPDATE PlayoffSeries SET {wins}=? WHERE id=?;', (amount, id))
            self.connection.commit()  

    def end_playoff_series(self, winnerID):
        self.cursor.execute("SELECT id FROM PlayoffSeries WHERE highSeed = ? OR lowSeed = ?;", (winnerID, winnerID))
        series_id = self.cursor.fetchall()[0][0]

        self.cursor.execute('UPDATE PlayoffSeries SET winner=? WHERE id=?;', (winnerID, series_id))
        self.connection.commit()  
    
    # wins
    def select_wins(self, teamStatsID):
        self.cursor.execute('SELECT wins FROM TeamStats WHERE id = ?;', (teamStatsID,))
        results = self.cursor.fetchall()
        return results

    # Team ID
    def get_champion(self):
        self.cursor.execute('SELECT champion FROM Playoffs;')
        results = self.cursor.fetchall()
        return results

    # String Team, Team 
    def get_playoff_winners_and_losers(self, team):
        self.cursor.execute("SELECT highSeed, lowSeed FROM PlayoffSeries WHERE winner = ? ORDER BY round DESC;", (team,))
        results = self.cursor.fetchall()

        return results

    #################################################
    ############## End of Season Screen #############
    #################################################

    # name, winner, season
    def get_awards(self, seasonYear):
        self.cursor.execute('SELECT Awards.name, Character.name, Awards.season FROM Awards INNER JOIN Character ON Awards.Winner = Character.id WHERE Awards.season=?;', (seasonYear,))
        results = self.cursor.fetchall()
        return results
    
    def set_awards(self, seasonYear, characterID, awardName):
        self.cursor.execute('INSERT INTO Awards (season, winner, name) VALUES (?,?,?);', (seasonYear, characterID, awardName))
        self.connection.commit()

    def clear_team(self):
        self.cursor.execute('DELETE FROM Team;')
        self.connection.commit()
    
    def clear_defensive_stats(self):
        self.cursor.execute('DELETE FROM DefensiveStats;')
        self.connection.commit()
    
    def clear_pitching_stats(self):
        self.cursor.execute('DELETE FROM PitchingStats;')
        self.connection.commit()

    def clear_batter_stats(self):
        self.cursor.execute('DELETE FROM BatterStats;')
        self.connection.commit()
    
    def clear_player_stats(self):
        self.cursor.execute('DELETE FROM PlayerStats;')
        self.connection.commit()
    
    def clear_playoffs(self):
        self.cursor.execute('DELETE FROM Playoffs;')
        self.connection.commit()
    
    def clear_playoff_series(self):
        self.cursor.execute('DELETE FROM PlayoffSeries;')
        self.connection.commit()
    
    def clear_game(self):
        self.cursor.execute('DELETE FROM Game;')
        self.connection.commit()
    
    def clear_team_stats(self):
        self.cursor.execute('DELETE FROM TeamStats;')
        self.connection.commit()
    
    def set_previous_season(self, champ, runnerUp, divOneLoser, divTwoLoser, year):
        self.cursor.execute('UPDATE Season SET champion = ?, runnerUp = ?, semiFinalsTeamOne = ?, semiFinalsTeamTwo = ? WHERE year = ?;', (champ, runnerUp, divOneLoser, divTwoLoser, year))
        self.connection.commit()
    
    #################################################
    ############## Previous Season Screen ###########
    #################################################

    # year, champion, runnerUp, semiFinalsTeamOne, semiFinalsTeamTwo, currentGameNum
    def get_season(self, year):
        self.cursor.execute('SELECT * FROM Season WHERE year=?;', (year,))
        results = self.cursor.fetchall()
        return results
    
    # [year, champion, runnerUp, semiFinalsTeamOne, semiFinalsTeamTwo, currentGameNum]
    def get_all_seasons(self):
        self.cursor.execute('SELECT * FROM Season')
        results = self.cursor.fetchall()
        return results