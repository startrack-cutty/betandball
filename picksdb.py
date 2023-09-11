from dataaccess import DataAccess
from database.dbconnection import DBConnection

dbConnector = DBConnection()



def savePicks(userID, poolID, week, game1winner, game2winner, game3winner, game4winner,
        game5winner, game6winner, game7winner, game8winner, game9winner, game10winner,
        game11winner, game12winner, game13winner, game14winner, game15winner, game16winner):



    # Create sql stmt with variables...

    sqlstmt = "INSERT INTO picks (userID, poolID, week, game1winner, game2winner, game3winner, game4winner, game5winner, game6winner, game7winner, game8winner, game9winner, game10winner, game11winner, game12winner, game13winner, game14winner, game15winner, game16winner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Create second variable to hold data fields for inserting data to the DB.
    values = (userID, poolID, week, game1winner, game2winner, game3winner, game4winner,
                 game5winner, game6winner, game7winner, game8winner, game9winner, game10winner,
                 game11winner, game12winner, game13winner, game14winner, game15winner, game16winner)


    #try:
    # Call method to insert the data and commit to database.
    dbConnector.my_cursor.execute(sqlstmt, values)
    dbConnector.mydb.commit()

    print(f'Inside picksdb.py.  Time to store these picks... {values}')