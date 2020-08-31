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

    config = {"tempdir": tempdir}

    # Output files
    config["lstats_f"] = os.path.join(tempdir, "lift_stats.csv")
    config["qstats_f"] = os.path.join(tempdir, "queue_stats.csv")
    config["estats_f"] = os.path.join(tempdir, "employee_stats.csv") 

    return config
