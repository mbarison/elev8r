'''
Created on 20-Jul-2020

@author: mbarison
'''

import random
import time

class Randomizer(object):
    '''
    classdocs
    '''


    def __init__(self, timespan, employees):
        '''
        Constructor
        '''
        self._timespan = timespan
        self._employees = employees
        self.updateProb()
        random.seed(time.time())
        
    def updateProb(self):
        # if timespan is zero, set probability to 1 to flush employee queue
        if self._timespan <= 0:
            self._prob_sec = 1
        else:
            self._prob_sec = 1.*self._employees/self._timespan

                   
    def get_arrival(self):
        
        # double the arrival rate between 7:30 and 8:30
        if self._timespan > 3600 and self._timespan < 7200:
            k_fac = 2
        else:
            k_fac = 1
        
        # check if no employees left
        if self._employees == 0:
            return False
        
        if random.random() < self._prob_sec * k_fac:
            self._employees -= 1
            self._timespan -= 1
            self.updateProb()
            return True
        else:
            self._timespan -= 1
            self.updateProb()
            return False
        
    def get_employees(self):
        return self._employees
        
    
            
        