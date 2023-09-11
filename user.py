# This class is for the creation and management of Football Poolz Users

import database.userdb
class User:

        # Attributes
    favorite_team = ''
    card_number = ''
    expDate = ''
    cvv = ''
    billing_zip = ''

    # Constructor Method
    #def __init__(self,username,email,password,favoriteSport,favoriteTeam,cardNumber,expDate,cvv,billingZip):
    #def __init__(self,username):
    #    self.username = username

    def __init__(self, username, password='', email='', first_name='', last_name='', phone=''):
        self.username = username,
        self.password = password,
        self.email = email,
        self.first_name = first_name,
        self.last_name  = last_name,
        self.phone = phone


        '''
        self.favorite_team = favorite_team,
        self.card_number = card_number,
        self.exp_date = exp_date,
        self.cvv = cvv,
        self.billing_zip = billing_zip
        '''

    # Methods
    #def buyIn(userDict):
    #    print(userDict['paymentInformation']['cardNumber'])

            # Check to see if user exists in the database.
    def checkUsername(self):
        userExists = database.userdb.checkUsername(self.username)
        if userExists:
            return True
        else:
            return False


    #def createAccount(self):
    def createAccount(self, username, password, email, first_name, last_name, phone):
        database.userdb.createAccount(username, password, email, first_name, last_name, phone)

    #def createAccount(username, password, email, first_name, last_name, phone)
        #if userExists:
            #print('Inside user.py.  User exists already.')
            #return True
        #else:
            #print('Inside user.py.  User created successfully.')
            #return  False


    def login(self, username, password):
        database.userdb.login(self, username, password)

    # This method allows a current user to invite someone to join the app
    def inviteUser(self):
            pass

    # This method updates the user's info in the database.
    def updateUser(self):
        pass

    # This allows a user to cancel their membership.
    def deleteUser(self):
        pass

    # This method allows a user to send a message to another user in the app (more than
        # one too.  Need to use *args to allow a send list for text threads.
    def sendMessage(self, message, username):
        pass

    def getUserID(self):
        user_id = database.userdb.getUserID(self.username)
        return user_id