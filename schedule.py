'''
    This class manages the schedule object.  A schedule is a lineup of games for the
    football season.
'''
from game import Game
from team import Team
import database.scheduledb as schedule



class Schedule:

    # Class Object Attributes
    #listOfTeams = Team
    #teamDict = Team
    #game1W1 = Game(teamDict.teams[14]['mascot'],  teamDict.teams[29]['mascot'],  '7/7/23', '8:20 PM', 1)
    #game2W1 = Game(teamDict.teams[22]['mascot'], teamDict.teams[23]['mascot'], '7/7/23', '8:20 PM', 1)


    #week1 = [game1W1, game2W1]

    # Constructon
    def __init__(self, week):
        self.week = week


    # This method retrieves the schedule by week
    def getSchedule(self):
        lineup = schedule.getSchedule(self.week)
        return lineup


    def doSomething(self):
        printSchedule(self)