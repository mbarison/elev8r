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


    def __init__(self, start_date, end_date, floorplan, elevators=8, run_number=0, pen_max=8, verbose=False):
        '''
        Constructor
        '''
        self._start_date = start_date
        self._end_date = end_date
        self._floorplan = floorplan
        self._run_number = run_number
        self._n_elevators = elevators
        self._pen_max = pen_max
        self._verbose = verbose
        self._seconds = (self._end_date - self._start_date).seconds
        self._queue_length = {"ticks": [], "length": []}
        self._lift_tracker = {"ticks": []}
        self._destination = []
        
    def run(self):
        employee_pool = EmployeePool(self._floorplan, verbose=self._verbose)
        foyer = Foyer(self._pen_max)
    
        elevators = []
        for i in range(1, self._n_elevators+1):
            self._lift_tracker["lift_%d" % i] = []
            elevators.append(Elevator(i, verbose=self._verbose))
        
        def employees_on_lifts():
            return sum([i.count_employees() for i in elevators])
        
        # Now starts the main loop
        # TODO: let the Randomizer provide employees
        r = Randomizer(self._seconds, employee_pool.count_employees())
    
        print("Run #%.3d Allocating %d employees over %d seconds" % (self._run_number, employee_pool.count_employees(), self._seconds))
    
        tick = 0
        last_q_len = -1
        # don't stop until all employees are at work
        while employee_pool.count_employees() + employees_on_lifts() > 0:
            tick += 1
            
            if self._verbose:
                print("Tick #%d" % tick)
            
            # store data only if there was a state change
            if foyer.get_queue_len() != last_q_len:
                self._queue_length["ticks"].append(tick)
                self._queue_length["length"].append(foyer.get_queue_len())
                last_q_len = foyer.get_queue_len()
            
            self._lift_tracker["ticks"].append(tick)
        
            foyer.update_tick(tick)

            # check if there is a new arrival
            if r.get_arrival():
                
                # Move employee to the queue
                emp = employee_pool.get_employee()
                foyer.accept(emp, tick)
            
            if self._verbose:
                print("In queue: %s ; In pen: %s" % (foyer.get_queue_ids(), foyer.get_pen_ids()))

            for lift in elevators:
                # send tick
                lift.update_tick(tick)
                
                self._lift_tracker["lift_%d" % lift.get_id()].append(lift.get_state())
                
                
                # if there are employees waiting and lifts ready, send a new employee
                if lift.get_state() == Elevator.READY:
                    if foyer.get_pen_len() > 0:
                        emp = foyer.release()
                        if emp:
                            lift.send(emp)
                        
                # empty idle lifts
                if lift.get_state() == Elevator.IDLE:
                    if lift.count_employees() > 0:
                        emp = lift.get_employee()
                        emp.atWork(tick)
                        self._destination.append(emp)
                        
                    # if there's employees waiting, call lift
                    # TODO: do not call too many lifts
                    if foyer.get_pen_len() > 0:
                        lift.call()
                        
                        
    def get_queue_stats(self):
        dfq = pd.DataFrame(self._queue_length)
        dfq["run"] = self._run_number
        dfq["hour"]=dfq["ticks"]//3600+1 
        return dfq
    
    def get_lift_stats(self):
        dfl = pd.DataFrame(self._lift_tracker)
        dfl["run"] = self._run_number
        dfl["hour"]=dfl["ticks"]//3600+1 
        return dfl
    
    def get_employee_stats(self):
        data_dct = {"id": [], "agency": [], "arrival": [], "waiting_time": [], "lift": [], "place": [], "floor": []}
        for e in self._destination:
            data_dct["id"].append(e.getId())
            data_dct["agency"].append(e.getAffiliation())
            data_dct["arrival"].append(e.getArrivalTime())
            data_dct["waiting_time"].append(e.getWaitingTime())
            data_dct["lift"].append(e.getLift())
            data_dct["place"].append(e.getPlaceInQ())
            data_dct["floor"].append(e.getFloor())
        dfe = pd.DataFrame(data_dct)
        dfe["run"] = self._run_number
        dfe["hour"]=dfe["arrival"]//3600+1 
        return dfe.sort_values(by=["arrival"])
        
    
    