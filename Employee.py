'''
Created on 21-Jul-2020

@author: mbarison
'''

class Employee(object):
    '''
    classdocs
    '''


    def __init__(self, affiliation, floor):
        '''
        Constructor
        '''
        self._affiliation = affiliation
        self._floor = floor
        self._in_foyer = -1
        self._on_lift = -1
        self._at_work = -1
        
    def inFoyer(self, tick):
        self._in_foyer = tick
        
    def onLift(self, tick):
        self._on_lift = tick
        
    def atWork(self, tick):
        self._at_work = tick
        
    def getFloor(self):
        return self._floor
    
    def getArrivalTime(self):
        return self._in_foyer
    
    def getWaitingTime(self):
        return self._on_lift - self._in_foyer
        