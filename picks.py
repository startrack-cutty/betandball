import database.picksdb


class Picks:

    def __init__(self, userID, poolID, week, game1winner, game2winner, game3winner, game4winner,
                 game5winner, game6winner, game7winner, game8winner, game9winner, game10winner,
                 game11winner, game12winner, game13winner, game14winner, game15winner, game16winner):
        self.userID = userID,
        self.week = week,
        self.game1winner = game1winner,
        self.game2winner = game2winner,
        self.game3winner = game3winner,
        self.game4winner = game4winner,
        self.game5winner = game5winner,
        self.game6winner = game6winner,
        self.game7winner = game7winner,
        self.game8winner = game8winner,
        self.game9winner = game9winner,
        self.game10winner = game10winner,
        self.game11winner = game11winner,
        self.game12winner = game12winner,
        self.game13winner = game13winner,
        self.game14winner = game14winner,
        self.game15winner = game15winner,
        self.game16winner = game16winner


    # DO NOT NEED ALL THESE PARAMETERS.  USE WHAT'S IN THE CONSTRUCTOR WHEN CREATING THE OBJECT.
    #def savePicks(self, userID, poolID, week, game1winner, game2winner, game3winner, game4winner,
                 #game5winner, game6winner, game7winner, game8winner, game9winner, game10winner,
                 #game11winner, game12winner, game13winner, game14winner, game15winner, game16winner):

    def savePicks(self,userID, poolID, week, game1winner, game2winner, game3winner, game4winner, game5winner, game6winner, game7winner, game8winner,
                      game9winner, game10winner, game11winner, game12winner, game13winner, game14winner, game15winner, game16winner):
        print('In picks.py... Store Picks in the database...')
        #database.picksdb.savePicks(self.userID, self.week, self.game1winner, self.game2winner, self.game3winner, self.game4winner,
                 #self.game5winner, self.game6winner, self.game7winner, self.game8winner, self.game9winner, self.game10winner,
                 #self.game11winner, self.game12winner, self.game13winner, self.game14winner, self.game15winner, self.game16winner)
        database.picksdb.savePicks(userID, poolID, week, game1winner, game2winner, game3winner,
                                   game4winner,
                                   game5winner, game6winner, game7winner, game8winner,
                                   game9winner, game10winner,
                                   game11winner, game12winner, game13winner, game14winner,
                                   game15winner, game16winner)