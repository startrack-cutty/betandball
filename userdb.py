from dataaccess import DataAccess
from database.dbconnection import DBConnection

dbConnector = DBConnection()


def createAccount(username, password, email, first_name, last_name, phone):

    # Create sql stmt with variables...
    sqlstmt = "INSERT INTO users (username, password, email, first_name, last_name, phone) VALUES (%s, %s, %s, %s, %s, %s)"

    # Create second variable to hold data fields for inserting data to the DB.
    values = (username, password, email, first_name, last_name, phone)


    #try:
        # Call method to insert the data and commit to database.
    dbConnector.my_cursor.execute(sqlstmt, values)
    dbConnector.mydb.commit()

    #except:
        #print('Inside userdb.py and exception thrown trying to create user account.')
        #return True
    #else:
    return False
    #print('Leaving userdb.py')


# This method logs a user into the system.
def login(self, username, password):

    sqlstmt = """SELECT * FROM users where username = '%s' AND password = '%s'""" % (username, password)
    print(sqlstmt)
    try:
        dbConnector.my_cursor.execute(sqlstmt)
        result = dbConnector.my_cursor.fetchall()
        if result:
            print(f'Welcome back {username}')
            for user in result:
                print(user)
        else:
            print('You have entered an incorrect username or password.')
    except:
        print('Inside userdb.py and some exception was thrown.')
    # RETURN A TRUE OR FALSE VALUE HERE FROM THIS METHOD TO LET CALLER KNOW IF USER FOUND IN THE DATABASE...




def checkUsername(username):
    sqlstmt = """SELECT * FROM users where username = '%s'""" % (username)
    try:
        dbConnector.my_cursor.execute(sqlstmt)
        result = dbConnector.my_cursor.fetchall()
        if result:
            print(f'Inside userdb.py.  This user exists...')
            for user in result:
                print(user)
            return True
        else:
            return False
    except:
        print('Inside userdb.py and some exception was thrown.  Maybe user exists.')
        return True

def getUserID(username):
    sqlstmt = """SELECT user_id FROM users where username = '%s'""" % (username)
    try:
        dbConnector.my_cursor.execute(sqlstmt)
        result = dbConnector.my_cursor.fetchall()
        print(result)
        if result:
            print(f'Returning user_id now...')
            for user in result:
                user_id = user[0]
                print(user_id)
            return user_id
        else:
            return False
    except:
        print('Inside userdb.py, trying to get userID.  Exception thrown.')
        return True

    #return user_id