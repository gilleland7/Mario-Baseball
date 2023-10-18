import sqlite3
import csv
import sys
import os
import datetime

# Get current and then parent directories
sys.path.append(".")
from src.Shared import Character

version = 1.0
class Import():
    def __init__(self):
        self.stadiums = ["Bowser Castle","Bowser Jr. Playroom", "Daisy Cruiser", "DK Jungle", "Luigi's Mansion", "Mario Stadium", "Peach Ice Garden", "Wario City", "Yoshi Park"]
        self.divisions = ["Mushroom", "Flower"]
        self.ignore_first_row = True
        characters = self.read_csv()

        self.cursor, self.connection = self.connect()
        self.add_characters_to_database(characters)
        self.add_stadiums()
        self.add_division()
        self.add_franchise_meta_data()

    def connect(self):
        connection = sqlite3.connect('./mario.db')
        cursor = connection.cursor()
        return cursor, connection

    def close(self, connection):
        # Save the changes
        connection.commit()
        connection.close()  

    def add_characters_to_database(self, characters):
        id = 1

        # characters must be added first to set up their IDs for use as foreign keys
        for character in characters:
            self.add__character_stats_to_database(character, id)
            id += 1
        id = 1
        # Chemistry has to be done after character stats so character IDs are established for foreign keys
        for character in characters:
            self.add_character_chemistry(character, id)
            id += 1

    
    def add_character_chemistry(self, character, id):
        # good chemistry
        
        for name in character.good_chemistry: # good chemistry is 1
            self.cursor.execute('SELECT id FROM Chemistry WHERE (characterOne = ? AND characterTwo = ?) OR (characterOne = ? AND characterTwo = ?);',(character.name, name, name, character.name))
            results = self.cursor.fetchall()

            if (len(results) == 0): # Make sure relationship isn't already in database
                self.cursor.execute('SELECT id FROM Character WHERE (name = ?);',(name,))
                results = self.cursor.fetchall()               
                self.cursor.execute('INSERT INTO Chemistry(characterOne, characterTwo, type) VALUES (?,?,1);',(id, results[0][0]))
        
        for name in character.bad_chemistry: # good chemistry is 0
            self.cursor.execute('SELECT id FROM Chemistry WHERE (characterOne = ? AND characterTwo = ?) OR (characterOne = ? AND characterTwo = ?);',(character.name, name, name, character.name))
            results = self.cursor.fetchall()

            if (len(results) == 0): # Make sure relationship isn't already in database
                self.cursor.execute('SELECT id FROM Character WHERE (name = ?);',(name,))
                results = self.cursor.fetchall()
                self.cursor.execute('INSERT INTO Chemistry(characterOne, characterTwo, type) VALUES (?,?,0);',(id, results[0][0]))
        
        self.connection.commit()

    def add__character_stats_to_database(self, character, id):
        # set up game stats
        self.cursor.execute('INSERT INTO BatterStats(id, BA, slg, obp) VALUES (?,0,0,0);',(id,))
        self.cursor.execute('INSERT INTO DefensiveStats(id) VALUES (?);',(id,))
        self.cursor.execute('INSERT INTO PitchingStats(id) VALUES (?);',(id,))
        
        # Player stats
        self.cursor.execute('INSERT INTO PlayerStats(id, battingStats, defensiveStats, pitchingStats) VALUES (?,?,?,?);',(id,id,id,id))

        # Character stats
        self.cursor.execute('INSERT INTO Character(id, name, type, isCaptain, bat, pitch, field, run, weightedOverall, png, stats) VALUES (?,?,?,?,?,?,?,?,?,?,?);',(id, character.name, character.type, character.is_captain, character.hit, character.pitch, character.field, character.run, character.overall, character.png, id))

        self.connection.commit()
    
    def add_stadiums(self):
        for stadium in self.stadiums:
            self.cursor.execute('INSERT INTO Stadium VALUES (?)', (stadium,))
        self.connection.commit()

    def add_division(self):
        for div in self.divisions:
            self.cursor.execute('INSERT INTO Division VALUES (?)', (div,))
        self.connection.commit()

    def add_franchise_meta_data(self):
        today = datetime.date.today()
        year = today.year   

        state = 0 # 0=preseason, 1=inseason, 2=playoffs  

        self.cursor.execute('INSERT INTO Franchise (state, version, year) VALUES (?,?,?)', (state, version, year))
        
        self.cursor.execute('INSERT INTO Season (year) VALUES (?)', (2023,))

        self.connection.commit() 

    # Sample query: cursor.execute('SELECT * FROM Team ORDER BY Conference'):
    def read_csv(self):
        with open('setup/mario_stats_csv.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            characters = []
            for row in reader:
                if (not self.ignore_first_row): # First row is header
                    print("NEW CHARACTER: " + str(row))
                    character = Character.Character()
                    name, type = self.setup_name(row[0])
                    name = name.strip()
                    is_captain = self.setup_is_captain(row[1])
                    bat = int(row[2])
                    pitch = int(row[3])
                    field = int(row[4])
                    run = int(row[5])
                    overall = float(row[6])
                    good_chemistry = self.setup_chemistry(row[7])
                    bad_chemistry = self.setup_chemistry(row[8])

                    character.setupBase(pitch, bat, field, run, overall, name, type, is_captain, good_chemistry, bad_chemistry)
                    characters.append(character)
                else:
                    self.ignore_first_row = False

        csvfile.close()
        return characters

    def setup_name(self, data):
      name = data
      type = "None"
      if ("(" in data):
          array = data.split("(") # removes the first (
          type = array[1][:-1] # removes the final )
          name = array[0]
    
      return name, type
    
    def setup_is_captain(self, data):
        is_captain = 0

        if (data != ""):
            is_captain = 1
        return is_captain

    # data = array
    def setup_chemistry(self, data):
        chemistry = []
       
        split_characters = data.split("|")

        for character in split_characters:
            if (character != ""):
                chemistry.append(character.strip())

        return chemistry

# Run this at start of every script so database updates are clean
def clear_database():
        connection = sqlite3.connect('./mario.db')
        cursor = connection.cursor()

        cursor.execute('DELETE FROM BatterStats;')
        cursor.execute('DELETE FROM DefensiveStats;')
        cursor.execute('DELETE FROM PitchingStats;')
        cursor.execute('DELETE FROM PlayerStats;')

        cursor.execute('DELETE FROM Character;')
        cursor.execute('DELETE FROM Chemistry;')

        cursor.execute('DELETE FROM Stadium;')
        cursor.execute('DELETE FROM Division;')

        cursor.execute('DELETE FROM Franchise;')
        cursor.execute('DELETE FROM Season')

        connection.commit()
        connection.close()

clear_database()
Import()
