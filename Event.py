'''
Created on 28-Jul-2020

@author: mbarison
'''

from Randomizer import Randomizer
from datetime import datetime, timedelta
from EmployeePool import EmployeePool
from Foyer import Foyer
from LiftTracker import LiftTracker

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
        self._lift_stats = {"ticks": [], "ready": [], "in_transit": [], "idle": [], "homebound": []}
        self._destination = []
        
    def run(self):
        employee_pool = EmployeePool(self._floorplan, verbose=self._verbose)
        
        employee_initial_count = employee_pool.count_employees()
        
        foyer = Foyer(self._pen_max)   
        lift_tracker = LiftTracker(elevators=self._n_elevators, verbose=self._verbose) 
        
        # Now starts the main loop
        # TODO: let the Randomizer provide employees
        r = Randomizer(self._seconds, employee_pool.count_employees())
    
        print("Run #%.3d Allocating %d employees over %d seconds" % (self._run_number, employee_pool.count_employees(), self._seconds))
    
        tick = 0
        last_q_len = -1

        # don't stop until all employees are at work

        while employee_pool.count_employees() + lift_tracker.employees_on_lifts() + foyer.get_queue_len() + foyer.get_pen_len() > 0:
            tick += 1
            
            if self._verbose:
                print("Tick #%d Employees left: %d on lifts: %d" % (tick, employee_pool.count_employees(), lift_tracker.employees_on_lifts()))

            foyer.update_tick(tick)

            # store data only if there was a state change
            q_len_now = foyer.get_queue_len()+foyer.get_pen_len()
            if q_len_now != last_q_len:
                self._queue_length["ticks"].append(tick)
                self._queue_length["length"].append(q_len_now)
            last_q_len = q_len_now
            
            # check if there is a new arrival
            if r.get_arrival():
                
                # Move employee to the queue
                emp = employee_pool.get_employee()
                foyer.accept(emp, tick)
            
            if self._verbose:
                print("In queue: %s ; In pen: %s" % (foyer.get_queue_ids(), foyer.get_pen_ids()))

            lift_tracker.update_tick(tick)

            self._lift_stats["ticks"].append(tick)

            self._lift_stats["ready"].append(lift_tracker.count_lifts_ready())
            self._lift_stats["in_transit"].append(lift_tracker.count_lifts_transit())
            self._lift_stats["idle"].append(lift_tracker.count_lifts_idle())
            self._lift_stats["homebound"].append(lift_tracker.count_lifts_homebound())

            # if there are employees waiting and lifts ready, send a new employee
            while foyer.get_pen_len() > 0 and lift_tracker.count_lifts_ready() > 0:
                emp = foyer.release()
                assert(emp != None)
                assert(lift_tracker.accept_employee(emp) != False)
                        
            # empty idle lifts
            while lift_tracker.count_employees_idle() > 0:
                emp = lift_tracker.disembark_employee()
                assert(emp != None)
                emp.atWork(tick)
                self._destination.append(emp)
                        
            # if there's employees waiting, call lift
            to_service = foyer.get_pen_len() - (lift_tracker.count_lifts_homebound() + lift_tracker.count_lifts_ready())
            if to_service > 0:
                for _ in range(0, to_service):
                    if not lift_tracker.call_lift():
                        break
                        
        assert(foyer.get_pen_len() == 0)
        assert(foyer.get_queue_len() == 0)
        assert(employee_pool.count_employees() == 0)
        assert(lift_tracker.employees_on_lifts() == 0)
        assert(employee_initial_count == len(self._destination))
        
                        
    def get_queue_stats(self):
        dfq = pd.DataFrame(self._queue_length)
        dfq["run"] = self._run_number
        dfq["hour"]=dfq["ticks"]//3600+1 
        return dfq
    
    def get_lift_stats(self):
        dfl = pd.DataFrame(self._lift_stats)
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
        
    
    