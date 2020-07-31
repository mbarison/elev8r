'''
Created on 18-Jul-2020

@author: mbarison
'''

from random import randint
from collections import deque

class Elevator(object):
    '''
    Simulates the behaviour of an elevator
    '''

    # Static states
    READY = 0
    IN_TRANSIT = 1
    IDLE = 2
    HOMEBOUND = 3

    EMPLOYEE_LIMIT = 1

    def __init__(self, lid, verbose=False):
        '''
        Constructor
        '''
        self._state = Elevator.READY
        self._employees = deque([])
        self._floor_q = deque([1])
        self._current_floor = 1
        self._eta_q = deque([0])
        self._time = -1
        self._id = lid
        self._verbose = verbose
        
    def get_id(self):
        return self._id
        
    def get_state(self):
        return self._state
    
    def get_floor(self):
        return self._current_floor
    
    def update_tick(self, tick):
        self._tick = tick
        
        # check if a change of state is needed
        if len(self._eta_q) > 0  and self._tick >= self._eta_q[0]:
            self._eta_q.popleft()
            self._current_floor = self._floor_q.popleft()
            
            if self._state == Elevator.IN_TRANSIT:
                self._state = Elevator.IDLE
            elif self._state == Elevator.HOMEBOUND:
                self._state = Elevator.READY
    
    def call(self):
        if self._state == Elevator.IDLE:
            self._state = Elevator.HOMEBOUND
            self._floor_q.append(1)
            self._eta_q.append(self.transit_time(1))
            return True
        else:
            return False
        
    def send(self, employee):
        if self._state == Elevator.READY:
            floor = employee.getFloor()
            self._state = Elevator.IN_TRANSIT
            self._floor_q.append(floor)
            employee.onLift(self._tick, self._id)
            self._employees.append(employee)
            self._eta_q.append(self.transit_time(floor))
            assert len(self._employees) <= Elevator.EMPLOYEE_LIMIT
            if self._verbose:
                print("Lift %d send Employee #%0.4d to floor %d eta: %d" % (self._id, employee.getId(), floor, self._eta_q[0]))
            return True
        else:
            return False
        
    def get_employee(self):
        try:
            e = self._employees.popleft()
            if self._verbose:
                print("Lift %d Employee #%0.4d arrived at floor %d tick: %d" % (self._id, e.getId(), self._current_floor, self._tick))
            return e
        except:
            return None
        
    def count_employees(self):
            return len(self._employees)
        
    def transit_time(self, floor):
        t = 0
        
        if floor == 1:
            t = randint(10, 20)
        else:
            for _ in range(0, floor-self._current_floor):
                t += randint(5,10)
                
        #if self._verbose:
        #    print("Lift %d Current floor:%d, Next floor:%d, Transit time: %d, eta: %d" % 
        #          (self._id, self._current_floor, floor, t, self._tick + t))

        return self._tick + t