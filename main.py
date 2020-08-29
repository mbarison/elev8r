'''
Created on 21-Jul-2020

@author: mbarison
'''

import pandas as pd

from datetime import datetime
from Event import Event


def main(config):

    start_date = config["start_date"]
    end_date   = config["end_date"]
    floorplan  = config["floorplan"]
    n_runs     = config["runs"]
    elevators  = config["elevators"]
    verbose    = config.get("verbose", False)
    qstat_f    = config["qstats_f"]
    estat_f    = config["estats_f"]
    lstat_f    = config["lstats_f"]
    pen_size   = config["pen_size"]

    print("Starting %d Runs, %d elevators, pen size: %d" % (n_runs, elevators, pen_size))

    t0 = datetime.now()

    dfqs = []
    dfls = []
    dfes = []
    
    for r in range(1, n_runs+1):
        event = Event(start_date, end_date, floorplan, elevators, r, pen_size, verbose=verbose)
    
        event.run()
    
        dfq = event.get_queue_stats() 
        dfqs.append(dfq)

        dfe = event.get_employee_stats()
        dfes.append(dfe)
    
        dfl = event.get_lift_stats()
        dfls.append(dfl)
    
    print("%d Runs completed in %s" % (n_runs, str(datetime.now()-t0)))

    dfl = pd.concat(dfls)    
    dfl.to_csv(lstat_f, index=False)
    
    dfq = pd.concat(dfqs)
    dfq.to_csv(qstat_f, index=False)
 
    dfe = pd.concat(dfes)
    dfe.to_csv(estat_f, index=False)    

if __name__ == '__main__':    
    from base_params import config
    main(config)
