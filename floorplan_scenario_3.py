'''
Created on 26-Aug-2020

@author: mbarison


Scenario 3: 
    Simulate 372 staff going to floors 9-13 and 435 staff going to floors 2-8
    It can be more-or-less an even breakdown between the floors. 

'''

from Agencies import *

# Floor plan
floorplan_3 = [{"floor": 9,  "agency": Agencies.EC, "employees": 74},
               {"floor": 10, "agency": Agencies.EC, "employees": 74},
               {"floor": 11, "agency": Agencies.EC, "employees": 74},
               {"floor": 12, "agency": Agencies.EC, "employees": 74},
               {"floor": 13, "agency": Agencies.EC, "employees": 76}]

floorplan_3.extend([{"floor": 2, "agency": Agencies.Other, "employees": 62},
                    {"floor": 3, "agency": Agencies.Other, "employees": 62},
                    {"floor": 4, "agency": Agencies.Other, "employees": 62},
                    {"floor": 5, "agency": Agencies.Other, "employees": 62},
                    {"floor": 6, "agency": Agencies.Other, "employees": 62},
                    {"floor": 7, "agency": Agencies.Other, "employees": 62},
                    {"floor": 8, "agency": Agencies.Other, "employees": 63}])

print("Using floorplan scenario 3: EC employees: %d Other employees: %d" %
        (sum([i["employees"] for i in floorplan_3 if i["agency"] == Agencies.EC]),
         sum([i["employees"] for i in floorplan_3 if i["agency"] == Agencies.Other])))