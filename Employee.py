'''
Created on 21-Jul-2020

@author: mbarison
'''

class Employee(object):
    '''
    classdocs
    '''


    def __init__(self, eid, affiliation, floor, verbose=False):
        '''
        Constructor
        '''
        self._id = eid
        self._affiliation = affiliation
        self._floor = floor
        self._in_foyer = -1
        self._in_pen = -1
        self._on_lift = -1
        self._at_work = -1
        self._used_lift = -1
        self._q_pos = -1
        self._verbose = verbose
        
    def inFoyer(self, tick, q_pos):
        self._in_foyer = tick
        self._q_pos = q_pos
        if self._verbose:
            print("Employee #%0.4d arrived in Foyer pos: %2d at tick: %d" % (self._id, self._q_pos, self._in_foyer))
  
    def inPen(self, tick):
        self._in_pen = tick
        if self._verbose:
            print("Employee #%0.4d arrived in Pen at tick: %d" % (self._id, self._in_pen))

    def onLift(self, tick, lid):
        self._on_lift = tick
        self._used_lift = lid
        if self._verbose:
            print("Employee #%0.4d on Lift: %2d at tick: %d" % (self._id, self._used_lift, self._on_lift))
        
    def atWork(self, tick):
        self._at_work = tick
        if self._verbose:
            print("Employee #%0.4d on Floor: %2d at tick: %d" % (self._id, self._floor, self._at_work))
        
    def getFloor(self):
        return self._floor
    
    def getArrivalTime(self):
        return self._in_foyer
    
    def getQueueTime(self):
        return self._in_pen - self._in_foyer

    def getPenTime(self):
        return self._on_lift - self._in_pen

    def getWaitingTime(self):
        return self._on_lift - self._in_foyer
    
    def getLift(self):
        return self._used_lift
        
    def getPlaceInQ(self):
        return self._q_pos
    
    def getId(self):
        return self._id

    def getAffiliation(self):
        return self._affiliation.value