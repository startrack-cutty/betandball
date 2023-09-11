# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions,
# and settings.


# Try this for catching errors
# import mysql.connector.errors
from user import User
from pool import Pool
from schedule import Schedule
from team import Team
from picks import Picks


def createAccount():
    # This has no purpose. I just didn't know how to move the indentation back for all the
    # code that follows this line.
    if (True):

        # Try to check username here to see if it exists first, before taking user through
        # painful steps of entering a bunch of other information.
        # username = input('Enter a username: ')
        # userCheck = User(username)
        # userCheck.checkUsername(username)
        # print(userCheck)

        username = input('Enter a username: ')
        userExists = True

        # Construct new user object here.
        newUser = User(username)

        # Need to call user.checkUsername here to see if the username exists already.
        userExists = newUser.checkUsername()

        # While the username already exists in the database, give user option to enter a new username.
        while (userExists):
            username = input('This username is already taken.  Please enter another username: ')
            newUser.username = username
            print('Check new username: ' + newUser.username)
            userExists = newUser.checkUsername()

        # Finish getting user credentials since username has now been cleared.
        password = input('Create your password: ')
        email = input('Enter your email: ')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        phone = input('Phone no: ')

        # No need to instantiate a new user here.  We can simply assign the attributes collected, to our existing object.
        # newUser = User(username, password, email, first_name, last_name, phone)
        newUser.password = password
        newUser.email = email
        newUser.first_name = first_name
        newUser.last_name = last_name
        newUser.phone = phone

        '''Try fixing this again where instead of passing in params, I am using self in
        the user class.  I don't understand why it's not working for me, but I had
        to revert to passing in params for this to work.
         I should be able to call this method this way using self to assign in the User class, but it's not working for some reason.
        '''
        # newUser.createAccount()

        # So I am calling it this way to force it to work correctly until I can figure it out.
        newUser.createAccount(username, password, email, first_name, last_name, phone)

        # Checking the values of these variables to see how they're stored and see why above call to createAccount above is not working.
        # print(newUser.username)
        # print(newUser.password)
        # print(newUser.email)
        # print(newUser.first_name)
        # print(newUser.last_name)
        # print(newUser.phone)

        # Set loggedIn to True, as user is now logged in...
        loggedIn = True

        print(f'Welcome to Football Pools!!!')


        # If user logged in successfully here, call method to proceed with more options here.
        openUserMenu(newUser)


def login():

    # Try to log into user's account here.
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # Creating the user object first here...  Gotta figure this out.  Can't keep creating new objects here if user
    # cannot get their usename and password incorrectly.
    login_user = User(username, password)

    # I should not have to pass args here if I instantiated the object in the line above with username and password already.
    # Figure this out...
    login_user.login(username, password)

    # If user logged in successfully here, call method to proceed with more options here.
    openUserMenu(login_user)



def openUserMenu(user):
    print(f'What would you like to do {user.username}?')
    selection = input('1: Create Pool \n'
           '2: Make Picks \n'
           '3: View My Pools \n'
           '4: Join a Pool \n')

    if selection == '1':
        print('Creating Pool...')
        createPool(user)
    elif selection == '2':
        print('Make Your Picks in a sec...')
    elif selection == '3':
        print('Getting your Pools...')
    elif selection == '4':
        pool_name = input("Type in the pool name you'd like to join: ")
        print(pool_name)


def createPool(user):

    user_id = user.getUserID()
    print(f'user_id is {user_id}')
    pool_name = input("Enter your pool name: ")
    buyin = input("What's the buyin amount? ")

    # Have to pass in UserID for username here for this to work.
    # newPool = Pool(pool_name, username, buyin)
    # newPool = Pool(pool_name, 3, buyin)
    newPool = Pool(pool_name, user_id, buyin)

    # Call method to add new pool to the database...
    newPool.addPool()


def makePicks():
    # Create schedule object and teams object
    schedule = Schedule(1)
    teams = Team()

    # Get the schedule and the teams
    lineup = schedule.getSchedule()
    the_teams = teams.getTeams()

    # Create a list to hold the winning teams selected by the user
    winners = []

    # Loop through the schedule, get the teams out of the schedule and display to the user for selecting...
    for game in lineup:
        away_team = game[0]
        home_team = game[1]
        for team in the_teams:
            if (team[0] == away_team):
                team_name = team[1]
                mascot = team[2]
                print(f'1: {team_name} {mascot}')
        for team in the_teams:
            if (team[0] == home_team):
                team_name = team[1]
                mascot = team[2]
                print(' vs ')
                print(f'2: {team_name} {mascot} \n')
                pick = int(input('Make your selection: '))
                if (pick == 1):
                    # Add {away_team} to list of winners here...
                    winners.append({away_team})
                    print(f'Away team selected: {away_team}')
                elif (pick == 2):
                    # Add {home_team} to list of winners here...
                    winners.append({home_team})
                    print(f'Home team selected: {home_team}')

    # Print list of selected winners...
    # for item in winners:
    # print(item)

    # Assign game winners to variables to store in the database.
    # FIGURE OUT HOW TO GET THE INTEGER OUT OF THE SET HERE...
    game1winner = list(winners[0])[0]
    game2winner = list(winners[1])[0]
    game3winner = list(winners[2])[0]
    game4winner = list(winners[3])[0]
    game5winner = list(winners[4])[0]
    game6winner = list(winners[5])[0]
    game7winner = list(winners[6])[0]
    game8winner = list(winners[7])[0]
    game9winner = list(winners[8])[0]
    game10winner = list(winners[9])[0]
    game11winner = list(winners[10])[0]
    game12winner = list(winners[11])[0]
    game13winner = list(winners[12])[0]
    game14winner = list(winners[13])[0]
    game15winner = list(winners[14])[0]
    game16winner = list(winners[15])[0]

    # Create picks object with attributes
    picks = Picks(2, 1, 1, game1winner, game2winner, game3winner, game4winner, game5winner, game6winner, game7winner,
                  game8winner,
                  game9winner, game10winner, game11winner, game12winner, game13winner, game14winner, game15winner,
                  game16winner)

    # Call method to store picks in the database
    picks.savePicks(2, 1, 1, game1winner, game2winner, game3winner, game4winner, game5winner, game6winner, game7winner,
                    game8winner,
                    game9winner, game10winner, game11winner, game12winner, game13winner, game14winner, game15winner,
                    game16winner)

    print('Thanks for participating in Football Poolz...')


#-----------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('Welcome to FootballPoolz.  What would you like to do?')
    selection = input('1: Create Account \n'
           '2: Login \n')

    if selection == '1':
        createAccount()
    elif selection == '2':
        login()












