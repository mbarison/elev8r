'''
Created on 28-Jul-2020

@author: mbarison
'''

from Randomizer import Randomizer
from datetime import datetime, timedelta
from EmployeePool import EmployeePool
from Elevator import Elevator
from Foyer import Foyer

import pandas as pd

class Event(object):
    '''
    classdocs
    '''


    def __init__(self, start_date, end_date, floorplan, run_number=0, verbose=False):
        '''
        Constructor
        '''
        self._start_date = start_date
        self._end_date = end_date
        self._floorplan = floorplan
        self._run_number = run_number
        self._verbose = verbose
        self._seconds = (self._end_date - self._start_date).seconds
        self._queue_length = {"ticks": [], "length": []}
        self._lift_tracker = {"ticks": []}
        self._destination = []
        
    def run(self):
        employee_pool = EmployeePool(self._floorplan)
        foyer = Foyer()
    
        elevators = []
        for i in range(1, 9):
            self._lift_tracker["lift_%d" % i] = []
            elevators.append(Elevator(i))
        
        # Now starts the main loop
        r = Randomizer(self._seconds, employee_pool.count_employees())
    
        print("Run #%.3d Allocating %d employees over %d seconds" % (self._run_number, employee_pool.count_employees(), self._seconds))
    
        
        for tick in range(0, self._seconds):
            
            if self._verbose:
                print("Tick #%d" % tick)
            
            self._queue_length["ticks"].append(tick)
            self._queue_length["length"].append(foyer.get_queue_len())
            
            self._lift_tracker["ticks"].append(tick)
        
            # check if there is a new arrival
            if r.get_arrival():
                
                # Move employee to the queue
                emp = employee_pool.get_employee()
                foyer.accept(emp, tick)
            
            for lift in elevators:
                # send tick
                lift.update_tick(tick)
                
                self._lift_tracker["lift_%d" % lift.get_id()].append(lift.get_state())
                
                
                # if there are employees waiting and lifts ready, send a new employee
                if lift.get_state() == Elevator.READY:
                    if foyer.get_queue_len() > 0:
                        emp = foyer.release()
                        lift.send(emp)
                        
                # empty idle lifts
                if lift.get_state() == Elevator.IDLE:
                    if lift.count_employees() > 0:
                        emp = lift.get_employee()
                        emp.atWork(tick)
                        self._destination.append(emp)
                        
                    # if there's employees waiting, call lift
                    if foyer.get_queue_len() > 0:
                        lift.call()
                        
                        
    def get_queue_stats(self):
        dfq = pd.DataFrame(self._queue_length)
        dfq["run"] = self._run_number
        return dfq
    
    def get_lift_stats(self):
        dfl = pd.DataFrame(self._lift_tracker)
        dfl["run"] = self._run_number
        return dfl
    
    def get_employee_stats(self):
        data_dct = {"arrival": [], "waiting_time": []}
        for e in self._destination:
            data_dct["arrival"].append(e.getArrivalTime())
            data_dct["waiting_time"].append(e.getWaitingTime())
        dfe = pd.DataFrame(data_dct)
        dfe["run"] = self._run_number
        return dfe
        
    
    