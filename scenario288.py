'''
Created on 26-Aug-2020

@author: mbarison

Scenario 2: 
    Simulate 248 staff going to floors 9-13 and 290 staff going to floors 2-8
    It can be more-or-less an even breakdown between the floors. 
    8 persons per lobby.
    8 elevators.

'''

import tempfile, os

from datetime import datetime

from base_scenario import get_tempdir

config = {}

# Start/end dates
config["start_date"] = datetime(2020, 9, 1, 6, 30)
config["end_date"] = datetime(2020, 9, 1, 9, 30)

# Number of repetitions
config["runs"] = 1000

# Floor plan
from floorplan_scenario_2 import floorplan_2

config["floorplan"] = floorplan_2

# Number of elevators
config["elevators"] = 8

# Pen size
config["pen_size"] = 8

# Verbosity
config["verbose"] = False

# Temp files
config = get_tempdir(2, config)