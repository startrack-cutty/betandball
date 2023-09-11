import mysql.connector

class DBConnection:

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

    my_cursor.execute("SHOW TABLES")
    for table in my_cursor:
        print(table[0])


    # DataAccess Constructor
    def __init__(self):
        pass





