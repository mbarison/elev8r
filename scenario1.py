'''
Created on 25-Aug-2020

@author: mbarison


Scenario 1: 
    Simulate 199 staff going to floors 9-13 and 232 staff going to floors 2-8
    It can be more-or-less an even breakdown between the floors. 
    2 persons per lobby.
    8 elevators.

'''

import tempfile, os

from datetime import datetime

from Agencies import *

# Temp directory (OS dependent)
tempdir = os.path.join(tempfile.gettempdir(), "Scenario_1")

if not os.path.exists(tempdir):
    os.mkdir(tempdir)

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
floorplan = [{"floor": 9,  "agency": Agencies.EC, "employees": 39},
             {"floor": 10, "agency": Agencies.EC, "employees": 40},
             {"floor": 11, "agency": Agencies.EC, "employees": 40},
             {"floor": 12, "agency": Agencies.EC, "employees": 40},
             {"floor": 13, "agency": Agencies.EC, "employees": 40}]

for i in range(2,9):
    floorplan.append({"floor": i, "agency": Agencies.Other, "employees": 29})

config["floorplan"] = floorplan

# Number of elevators
config["elevators"] = 8

# Verbosity
config["verbose"] = False