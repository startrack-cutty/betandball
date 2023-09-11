'''
    This class is for the game object.
'''

class Game:

 # Attributes
   homeScore = 0
   awayScore = 0
   currentQuarter = 0
   timeLeft = None
   dateOfGame = None
   startTime = None

   def __init__(self, homeTeam, awayTeam, dateOfGame, startTime, week):
       self.homeTeam = homeTeam
       self.awayTeam = awayTeam
       self.dateOfGame = dateOfGame
       self.startTime = startTime
       self.week = week
