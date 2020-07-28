'''
Created on 21-Jul-2020

@author: mbarison
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from datetime import datetime

import pandas as pd

from enum import Enum

from Event import Event

# affiliations
class Agencies(Enum):
    EC = 0

def main():
    # Initialization
    
    start_date = datetime(2020, 9, 1, 6, 30)
    end_date = datetime(2020, 9, 1, 9, 30)

    
    # floorplan
    floorplan = [{"floor": 9,  "agency": Agencies.EC, "employees": 140},
                 {"floor": 10, "agency": Agencies.EC, "employees": 119},
                 {"floor": 11, "agency": Agencies.EC, "employees": 122},
                 {"floor": 12, "agency": Agencies.EC, "employees": 133},
                 {"floor": 13, "agency": Agencies.EC, "employees": 100}]
    
    event = Event(start_date, end_date, floorplan)
    
    event.run()
    
    
    dfq = event.get_queue_stats() 
    print("Overall queue stats:")
    print(dfq.describe())

    dfq.plot(x="ticks", y="length")
    
    plt.savefig("/tmp/queue_length.png")
    
    dfl = event.get_lift_stats()
    for i in range(1,9):
        dfl.plot(x="ticks", y="lift_%d" % i)
    
        plt.savefig("/tmp/lift_%d.png" % i)
    
    dfe = event.get_employee_stats()
    
    print("Overall Employee stats:")
    print(dfe.describe())
    
    print("First hour:")
    print(dfe[dfe["arrival"]<3600].describe())
    
    print("Second hour:")
    print(dfe[(dfe["arrival"]>3600) & (dfe["arrival"]<7200)].describe())
  
    print("Third hour:")
    print(dfe[dfe["arrival"]>7200].describe())
    

if __name__ == '__main__':
    main()
