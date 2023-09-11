'''
    This class is for the team object.
'''

from database.dbconnection import DBConnection
import database.teamdb

dbConnector = DBConnection()

class Team:


    # Attributes
    wins = 0  #Stored in DB
    losses = 0  #Stored in DB
    logo = 0
    name = ''
    mascot = ''
    stadiumName = ''


    # Constructor with team name, logo, etc.
    def __init__(self):
       pass


   # Methods

    # Retrieve the teams from the database...
    def getTeams(self):
        result = database.teamdb.getTeams(self)
        return result

