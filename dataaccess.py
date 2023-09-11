import mysql.connector
from team import Team

class DataAccess:
    '''DO NOT USE TIS CLASS ANYMORE.  THERE IS A NEW CLASS CALLED DBCONNECTION LOCATED
    IN THE NEW PACKAGE, DATABASE...'''

    # Database connection is an attritube of the DataAccess class.  Anyone who instantiates
    # this class automatically gets a connection to the database.
    mydb = mysql.connector.connect(
            user="root",
            password="Killseneca1!",
            host="localhost",
            database = "footballpoolz"
        )

    # Create cursor
    my_cursor = mydb.cursor()

    # DataAccess Constructor
    def __init__(self):
        pass


    #def showTables(self):
    #my_cursor.execute("SHOW TABLES")
    #for table in my_cursor:
                #    print(table[0])


    # Insert all Teams into the teams table.
    '''teams = Team
    for key, value in teams.teams.items():
        #print(key, value['name'], value['mascot'])
        firstname = value['name']
        lastname = value['mascot']
        #nflteams = ''.join(str([firstname, lastname]))
        #print(nflteams)
        print(firstname, lastname)
    '''

