'''
Created on 21-Jul-2020

@author: mbarison
'''

class Foyer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._queue = []
        
    
    def accept(self, employee, tick):
        employee.inFoyer(tick)
        self._queue.append(employee)
        
    def release(self):
        try:
            return self._queue.pop()
        except:
            return None
        
    def get_queue_len(self):
        return len(self._queue)
        
    
        