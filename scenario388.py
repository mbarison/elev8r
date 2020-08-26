'''
Created on 26-Aug-2020

@author: mbarison


Scenario 3: 
    Simulate 372 staff going to floors 9-13 and 435 staff going to floors 2-8
    It can be more-or-less an even breakdown between the floors. 
    8 persons per lobby.
    8 elevators.

'''

import tempfile, os

from datetime import datetime

# Temp directory (OS dependent)
tempdir = os.path.join(tempfile.gettempdir(), "Scenario_1_8_8")

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
from floorplan_scenario_3 import floorplan_3

config["floorplan"] = floorplan_3

# Number of elevators
config["elevators"] = 8

# Pen size
config["pen_size"] = 8

# Verbosity
config["verbose"] = False