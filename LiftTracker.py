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
        self._verbose = verbose

        for i in range(1, elevators+1):
            self._elevators.append(Elevator(i, verbose=self._verbose))

    def employees_on_lifts(self):
        return sum([i.count_employees() for i in self._elevators])

    def update_tick(self, tick):

        for lift in self._elevators:
            # send tick
            lift.update_tick(tick)
       
        if self._verbose:
            self.status_flags()


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

    def count_lifts_homebound(self):
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

    def status_flags(self):

        def leds(ls, cond):
            lst = enumerate([[0,1][i.get_state() == cond] for i in ls])
            bitmap = 0
            for i,j in lst:
                bitmap += j<<i
            return "{0:b}".format(bitmap).zfill(len(self._elevators))

        sl = sorted(self._elevators, key=lambda x: x.get_id())
        print("Lifts READY      :", leds(sl, Elevator.READY))
        print("Lifts IDLE       :", leds(sl, Elevator.IDLE))
        print("Lifts IN_TRANSIT :", leds(sl, Elevator.IN_TRANSIT))
        print("Lifts HOMEBOUND  :", leds(sl, Elevator.HOMEBOUND))