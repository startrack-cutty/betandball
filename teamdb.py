from database.dbconnection import DBConnection

dbConnector = DBConnection()



# Get teams from the database and print them out...
def getTeams(self):
    dbConnector.my_cursor.execute("SELECT * FROM footballteams")
    result = dbConnector.my_cursor.fetchall()
    #for teams in result:
        #print(teams)
    return result