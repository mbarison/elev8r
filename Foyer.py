'''
Created on 21-Jul-2020

@author: mbarison
'''

from collections import deque

class Foyer(object):
    '''
    classdocs
    '''


    def __init__(self, pen_max=8):
        '''
        Constructor
        '''
        self._queue = deque([])
        self._pen   = deque([])
        self._pen_max = pen_max
        
    
    def accept(self, employee, tick):
        self._queue.append((employee, tick+5)) # seconds delay through gates
        employee.inFoyer(tick, self.get_queue_len())

    def update_tick(self, tick):
        # Move employees from queue to pen if there is space
        tmp_q = deque([i for i in self._queue if i[1] <= tick])

        while self.get_pen_len() < self._pen_max and len(tmp_q) > 0:
            e, t = tmp_q.popleft()
            self._queue.remove((e, t))
            e.inPen(t) 
            self._pen.append(e)

        
    def release(self):
        if self.get_pen_len() > 0:
            return self._pen.popleft()
        
        return None
        
    def get_queue_len(self):
        return len(self._queue)
    
    def get_pen_len(self):
        return len(self._pen)

    def get_queue_ids(self):
        return [e[0].getId() for e in self._queue]

    def get_pen_ids(self):
        return [e.getId() for e in self._pen]
        
    
        