from dataaccess import DataAccess
from database.dbconnection import DBConnection

dbConnector = DBConnection()



# def addPool(user_name, poolname, buyin):
def addPool(user_id, poolname, buyin):

    # Create sql stmt with variables...
    sqlstmt = "INSERT INTO pools (owner, name, buyin) VALUES (%s, %s, %s)"

    # Create second variable to hold data fields for inserting data to the DB.
    #values = (username, poolname, buyin)
    values = (user_id, poolname, buyin)

    #try:
        # Call method to insert the data and commit to database.
    dbConnector.my_cursor.execute(sqlstmt, values)
    dbConnector.mydb.commit()

    #except:
        #print('Inside userdb.py and exception thrown trying to create user account.')
        #return True
    #else:
    return False