'''
Created on 21-Jul-2020

@author: mbarison
'''

from collections import deque

class Foyer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._queue = deque([])
        
    
    def accept(self, employee, tick):
        self._queue.append(employee)
        employee.inFoyer(tick, self.get_queue_len())
        
    def release(self):
        try:
            return self._queue.popleft()
        except:
            return None
        
    def get_queue_len(self):
        return len(self._queue)
    
    def get_queue_ids(self):
        return [e.getId() for e in self._queue]
        
    
        