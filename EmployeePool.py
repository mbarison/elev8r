'''
Created on 21-Jul-2020

@author: mbarison
'''

from Employee import Employee
from collections import deque
import random
import time

class EmployeePool(object):
    '''
    classdocs
    '''


    def __init__(self, floorplan, verbose=False):
        '''
        Constructor
        '''
        self._employees = deque([])
        self._verbose = verbose
        for f in floorplan:
            this_floor = f["floor"]
            this_agency = f["agency"]
            for _ in range(0, f["employees"]):
                new_employee = Employee(self.count_employees(), this_agency, this_floor, self._verbose)
                self._employees.append(new_employee) 
        
        self._seed = time.time()
        if self._verbose:
            print("Employee pool random seed: %d" % self._seed)
                
        random.seed(self._seed)
        random.shuffle(self._employees)
        
    def get_employee(self):
        try:
            return self._employees.popleft()
        except:
            return None
               
               
    def count_employees(self):
        return len(self._employees) 