'''
Created on 28-Aug-2020

@author: mbarison
'''

from Elevator import Elevator
from random import shuffle

class LiftTracker(object):
    '''
    classdocs
    '''


    def __init__(self, elevators=8, verbose=False):
     
        self._elevators = []
        self._lift_stats = {"ticks": []}
        self._verbose = verbose

        for i in range(1, elevators+1):
            self._lift_stats["lift_%d" % i] = []
            self._elevators.append(Elevator(i, verbose=self._verbose))

    def employees_on_lifts(self):
        return sum([i.count_employees() for i in self._elevators])

    def update_tick(self, tick):

        self._lift_stats["ticks"].append(tick)

        for lift in self._elevators:
            # send tick
            lift.update_tick(tick)
                
            self._lift_stats["lift_%d" % lift.get_id()].append(lift.get_state())

    def count_lifts(self):
        return len(self._elevators)

    def count_lifts_ready(self):
        return len([i for i in self._elevators if i.get_state() == Elevator.READY])

    def count_lifts_transit(self):
        return len([i for i in self._elevators if i.get_state() == Elevator.IN_TRANSIT])

    def count_lifts_idle(self):
        return len([i for i in self._elevators if i.get_state() == Elevator.IDLE])

    def count_employees_idle(self):
        return sum([i.count_employees() for i in self._elevators if i.get_state() == Elevator.IDLE])

    def count_lifts_idle(self):
        return len([i for i in self._elevators if i.get_state() == Elevator.HOMEBOUND])

    def accept_employee(self, emp):
        # shuffle elevator list to randomize elevator
        shuffle(self._elevators)

        for lift in self._elevators:
            if lift.get_state() == Elevator.READY:
                lift.send(emp)
                return True

        return False

    def disembark_employee(self):
        for lift in self._elevators:
            if lift.get_state() == Elevator.IDLE and lift.count_employees() > 0:
                emp = lift.get_employee()
                return emp

        return None

    def call_lift(self):
        # assume we call the closest lift (TODO: verify)
        self._elevators.sort(key=lambda x: [0,-1e3][x.get_state() == Elevator.IDLE] + x.get_floor())

        for lift in self._elevators:
            if lift.get_state() == Elevator.IDLE and lift.count_employees() == 0:
                lift.call()
                return True
            elif lift.get_state() != Elevator.IDLE:
                return False

        return False
