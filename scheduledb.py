from dataaccess import DataAccess
from database.dbconnection import DBConnection

dbConnector = DBConnection()



def getSchedule(week):

    sqlstmt = """SELECT * FROM schedule where week = '%s'""" % (week)
    print(sqlstmt)

    dbConnector.my_cursor.execute(sqlstmt)
    result = dbConnector.my_cursor.fetchall()

    #for game in result:
        #print(game)

    return(result)