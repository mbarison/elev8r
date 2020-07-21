'''
Created on 21-Jul-2020

@author: mbarison
'''

from Employee import Employee
import random
import time

class EmployeePool(object):
    '''
    classdocs
    '''


    def __init__(self, floorplan):
        '''
        Constructor
        '''
        self._employees = []
        for f in floorplan:
            this_floor = f["floor"]
            this_agency = f["agency"]
            for e in range(0, f["employees"]):
                new_employee = Employee(this_agency, this_floor)
                self._employees.append(new_employee) 
                
        random.seed(time.time())
        random.shuffle(self._employees)
        
    def get_employee(self):
        try:
            return self._employees.pop()
        except:
            return None
               
               
    def count_employees(self):
        return len(self._employees) 