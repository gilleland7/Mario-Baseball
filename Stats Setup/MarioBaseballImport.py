import sqlite3
import csv
import sys
import os

# Get current and then parent directories
current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
 
# Append parent directory to path
sys.path.append(parent_path)

import Character

class Import():
    def __init__(self):
        self.ignore_first_row = True
        characters = self.read_csv()
        self.cursor, self.connection = self.connect()

    def connect(self):
        connection = sqlite3.connect('../mario.db')
        cursor = connection.cursor()
        return cursor, connection

    def close(self, connection):
        # Save the changes
        connection.commit()
        connection.close()    

    # Sample query: cursor.execute('SELECT * FROM Team ORDER BY Conference'):
    def read_csv(self):
        with open('mario_stats_csv.csv', newline='') as csvfile:
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

                    character.setup(pitch, bat, field, run, overall, name, type, is_captain, good_chemistry, bad_chemistry)
                    characters.append(character)
                else:
                    self.ignore_first_row = False

        csvfile.close()
        return characters

    def setup_name(self, data):
      name = data
      type = None
      if ("(" in data):
          array = data.split("(") # removes the first (
          type = array[1][:-1] # removes the final )
          name = array[0]
    
      return name, type
    
    def setup_is_captain(self, data):
        is_captain = 0

        if (data is not ""):
            is_captain = 1
        return is_captain

    # data = array
    def setup_chemistry(self, data):
        chemistry = []
       
        split_characters = data.split("|")

        for character in split_characters:
            chemistry.append(character.strip())

        return chemistry

Import()