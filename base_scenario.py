'''
Created on 31-Aug-2020

@author: mbarison
'''

import tempfile, os

def get_tempdir(scen, cfg):

    # Update config with temp directory (OS dependent)
    tempdir = os.path.join(tempfile.gettempdir(), "Scenario_%d_%d_%d" % 
        (scen, cfg["pen_size"], cfg["elevators"]))

    if not os.path.exists(tempdir):
        os.mkdir(tempdir)

    cfg["tempdir"] = tempdir

    # Output files
    cfg["lstats_f"] = os.path.join(tempdir, "lift_stats.csv")
    cfg["qstats_f"] = os.path.join(tempdir, "queue_stats.csv")
    cfg["estats_f"] = os.path.join(tempdir, "employee_stats.csv") 

    return cfg
