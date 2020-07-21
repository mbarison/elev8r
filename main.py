'''
Created on 21-Jul-2020

@author: mbarison
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from Randomizer import Randomizer
from datetime import datetime, timedelta

import pandas as pd

from enum import Enum
from EmployeePool import EmployeePool
from Elevator import Elevator
from Foyer import Foyer

# affiliations
class Agencies(Enum):
    EC = 0

def main():
    # Initialization
    
    date1 = datetime(2020, 9, 1, 6, 30)
    date2 = datetime(2020, 9, 1, 9, 30)

    dt = date2 - date1

    # floorplan
    floorplan = [{"floor": 9,  "agency": Agencies.EC, "employees": 140},
                 {"floor": 10, "agency": Agencies.EC, "employees": 119},
                 {"floor": 11, "agency": Agencies.EC, "employees": 122},
                 {"floor": 12, "agency": Agencies.EC, "employees": 133},
                 {"floor": 13, "agency": Agencies.EC, "employees": 100}]
    
    employee_pool = EmployeePool(floorplan)
    foyer = Foyer()
    
    lift_tracker = {"ticks": []}
    
    elevators = []
    for i in range(1, 9):
        lift_tracker["lift_%d" % i] = []
        elevators.append(Elevator(i))
        
    # Now starts the main loop
    r = Randomizer(dt.seconds, employee_pool.count_employees())
    
    print("Allocating %d employees over %d seconds" % (employee_pool.count_employees(), dt.seconds))
    
    destination = []

    queue_length = {"ticks": [], "length": []}
    

    for tick in range(0, dt.seconds):
        
        print("Tick #%d" % tick)
        
        queue_length["ticks"].append(tick)
        queue_length["length"].append(foyer.get_queue_len())
        
        lift_tracker["ticks"].append(tick)
        
        # check if there is a new arrival
        if r.get_arrival():
            
            # Move employee to the queue
            emp = employee_pool.get_employee()
            foyer.accept(emp, tick)
            
        for lift in elevators:
            # send tick
            lift.update_tick(tick)
            
            lift_tracker["lift_%d" % lift.get_id()].append(lift.get_state())
            
            
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
                    destination.append(emp)
                    
                # if there's employees waiting, call lift
                if foyer.get_queue_len() > 0:
                    lift.call()
        
    
    dfq = pd.DataFrame(queue_length)

    dfq.plot(x="ticks", y="length")
    
    plt.savefig("/tmp/queue_length.png")
    
    dfl = pd.DataFrame(lift_tracker)
    for i in range(1,9):
        dfl.plot(x="ticks", y="lift_%d" % i)
    
        plt.savefig("/tmp/lift_%d.png" % i)
    

if __name__ == '__main__':
    main()
