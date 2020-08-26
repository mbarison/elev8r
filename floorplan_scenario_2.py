'''
Created on 26-Aug-2020

@author: mbarison

Scenario 2: 
    Simulate 248 staff going to floors 9-13 and 290 staff going to floors 2-8
    It can be more-or-less an even breakdown between the floors. 

'''

from Agencies import *

# Floor plan
floorplan_2 = [{"floor": 9,  "agency": Agencies.EC, "employees": 49},
             {"floor": 10, "agency": Agencies.EC, "employees": 49},
             {"floor": 11, "agency": Agencies.EC, "employees": 49},
             {"floor": 12, "agency": Agencies.EC, "employees": 49},
             {"floor": 13, "agency": Agencies.EC, "employees": 52}]

floorplan_2.extend([{"floor": 2, "agency": Agencies.Other, "employees": 41},
                  {"floor": 3, "agency": Agencies.Other, "employees": 41},
                  {"floor": 4, "agency": Agencies.Other, "employees": 41},
                  {"floor": 5, "agency": Agencies.Other, "employees": 41},
                  {"floor": 6, "agency": Agencies.Other, "employees": 41},
                  {"floor": 7, "agency": Agencies.Other, "employees": 41},
                  {"floor": 8, "agency": Agencies.Other, "employees": 44}])

print("Using floorplan scenario 2: EC employees: %d Other employees: %d" %
        (sum([i["employees"] for i in floorplan_2 if i["agency"] == Agencies.EC]),
         sum([i["employees"] for i in floorplan_2 if i["agency"] == Agencies.Other])))