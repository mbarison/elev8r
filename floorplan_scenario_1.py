'''
Created on 25-Aug-2020

@author: mbarison


Scenario 1: 
    Simulate 199 staff going to floors 9-13 and 232 staff going to floors 2-8
    It can be more-or-less an even breakdown between the floors. 

'''

from Agencies import *

# Floor plan
floorplan_1 = [{"floor": 9,  "agency": Agencies.EC, "employees": 39},
               {"floor": 10, "agency": Agencies.EC, "employees": 40},
               {"floor": 11, "agency": Agencies.EC, "employees": 40},
               {"floor": 12, "agency": Agencies.EC, "employees": 40},
               {"floor": 13, "agency": Agencies.EC, "employees": 40}]

floorplan_1.extend([{"floor": 2, "agency": Agencies.Other, "employees": 33},
                    {"floor": 3, "agency": Agencies.Other, "employees": 33},
                    {"floor": 4, "agency": Agencies.Other, "employees": 33},
                    {"floor": 5, "agency": Agencies.Other, "employees": 33},
                    {"floor": 6, "agency": Agencies.Other, "employees": 33},
                    {"floor": 7, "agency": Agencies.Other, "employees": 33},
                    {"floor": 8, "agency": Agencies.Other, "employees": 34}])

print("Using floorplan scenario 1: EC employees: %d Other employees: %d" %
        (sum([i["employees"] for i in floorplan_1 if i["agency"] == Agencies.EC]),
         sum([i["employees"] for i in floorplan_1 if i["agency"] == Agencies.Other])))