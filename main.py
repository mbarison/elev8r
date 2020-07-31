'''
Created on 21-Jul-2020

@author: mbarison
'''

from datetime import datetime

import pandas as pd

from enum import Enum

from Event import Event

# affiliations
class Agencies(Enum):
    EC = 0

def main(start_date, end_date, floorplan, n_runs, verbose=False):
    
    dfqs = []
    dfls = []
    dfes = []
    
    for r in range(1, n_runs+1):
        event = Event(start_date, end_date, floorplan, r, verbose=verbose)
    
        event.run()
    
        dfq = event.get_queue_stats() 
        dfqs.append(dfq)

        dfe = event.get_employee_stats()
        dfes.append(dfe)
    
        dfl = event.get_lift_stats()
        dfls.append(dfl)
    
    dfl = pd.concat(dfls)    
    dfl.to_csv("/tmp/lift_stats.csv", index=False)
    
    dfq = pd.concat(dfqs)
    dfq.to_csv("/tmp/queue_stats.csv", index=False)
 
    dfe = pd.concat(dfes)
    dfe.to_csv("/tmp/employee_stats.csv", index=False)    

if __name__ == '__main__':
    
    start_date = datetime(2020, 9, 1, 6, 30)
    end_date = datetime(2020, 9, 1, 9, 30)

    floorplan = [{"floor": 9,  "agency": Agencies.EC, "employees": 140},
                 {"floor": 10, "agency": Agencies.EC, "employees": 119},
                 {"floor": 11, "agency": Agencies.EC, "employees": 122},
                 {"floor": 12, "agency": Agencies.EC, "employees": 133},
                 {"floor": 13, "agency": Agencies.EC, "employees": 100}]
    
    main(start_date, end_date, floorplan, 1000, False)
