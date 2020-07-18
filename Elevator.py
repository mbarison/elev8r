'''
Created on 18-Jul-2020

@author: mbarison
'''

from random import randint

class Elevator(object):
    '''
    Simulates the behaviour of an elevator
    '''

    # Static states
    READY = 0
    IN_TRANSIT = 1
    IDLE = 2
    HOMEBOUND = 3


    def __init__(self, params):
        '''
        Constructor
        '''
        self._state = Elevator.READY
        self._floor_q = [1]
        self._eta_q = []
        
        
    def get_state(self):
        return self._state
    
    
    def call(self):
        if self._state = Elevator.IDLE:
            self._state = Elevator.HOMEBOUND
            self._floor_q.append(1)
            self._eta_q.append(self.transit_time(1))
            return True
        else:
            return False
        
    def send(self, floor):
        if self._state = Elevator.READY:
            self._state = Elevator.IN_TRANSIT
            self._floor_q.append(floor)
            self._eta_q.append(self.transit_time(floor))
            return True
        else:
            return False
        
    def transit_time(self, floor):
        pass