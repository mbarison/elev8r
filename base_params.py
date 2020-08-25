'''
Created on 24-Aug-2020

@author: mbarison

Set basic parameters

'''

import tempfile, os

from datetime import datetime

from Agencies import *

# Temp directory (OS dependent)
tempdir = tempfile.gettempdir()

config = {"tempdir": tempdir}

# Output files
config["lstats_f"] = os.path.join(tempdir, "lift_stats.csv")
config["qstats_f"] = os.path.join(tempdir, "queue_stats.csv")
config["estats_f"] = os.path.join(tempdir, "employee_stats.csv")

# Start/end dates
config["start_date"] = datetime(2020, 9, 1, 6, 30)
config["end_date"] = datetime(2020, 9, 1, 9, 30)

# Number of repetitions
config["runs"] = 1000

# Floor plan
config["floorplan"] = [{"floor": 9,  "agency": Agencies.EC, "employees": 140},
                       {"floor": 10, "agency": Agencies.EC, "employees": 119},
                       {"floor": 11, "agency": Agencies.EC, "employees": 122},
                       {"floor": 12, "agency": Agencies.EC, "employees": 133},
                       {"floor": 13, "agency": Agencies.EC, "employees": 100}]

# Number of elevators
config["elevators"] = 8

# Verbosity
config["verbose"] = False