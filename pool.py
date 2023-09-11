
'''
    This class manages the pool object.  Users can create pools and other members can
    join pools.
'''

import database.pooldb


class Pool:

    # Attributes
    #setOfUsers = {}
    # createdBy
    # buyInAmount
    # sport
    # members (list of users belonging to the pool)

    #def __init__(self, pool_name, user_name, buyin):
    #    self.pool_name = pool_name
    #    self.user_name = user_name
    #    self.buyin = buyin


    def __init__(self, pool_name, user_id, buyin):
        self.pool_name = pool_name
        self.user_id = user_id
        self.buyin = buyin

    # Methods

    # Retrieves a pool and all users in the pool.
    def getPool(poolName):
        pass


    # This method adds a user to the current pool.
    def joinPool(self, username):
        # If invited to the pool
        #if invite==true:
            #pass
        pass


    # This method allows a user to remove themselves from a pool.
    def leavePool(self, username):
        pass


    # This method allows a pool owner to delete the pool.
    def deletePool(self, poolname):
        pass

    # This method adds a new pool to the database.
    #def addPool(self, username, poolname, buyin):
        #database.pooldb.addPool(username, poolname, buyin)
    #def addPool(self):
    #    print(self.user_name)
    #    print(self.pool_name)
    #    print(self.buyin)
    #    database.pooldb.addPool(self.user_name, self.pool_name, self.buyin)

    def addPool(self):
        print(self.user_id)
        print(self.pool_name)
        print(self.buyin)
        database.pooldb.addPool(self.user_id, self.pool_name, self.buyin)