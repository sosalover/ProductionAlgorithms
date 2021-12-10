stoplight_change_cost = 5
import numpy as np
import Car

def total_time_at_intersection(locations):
    c = 0
    for i in range(len(locations)):
        for j in range(locations[i]):
            c += locations[i][j]._time_elapsed
    return c


def valid_configuration(q):
    left_lanes = [[None, None], [None, None], [None, None], [None, None]]
    right_lanes = [[None, None], [None, None], [None, None], [None, None]]
    for i in range(4):
        left_lanes[i][0] = q[i * 2][0]
        left_lanes[i][1] = q[i * 2][1]
        right_lanes[i][0] = q[i * 2 + 1][0]
        right_lanes[i][1] = q[i * 2 + 1][1]
    #
    for i in range(len(left_lanes)):
        a = i * 2
        # LEFT LANE, LEFT TURN CHECK
        if left_lanes[i][1]:
            if q[(a + 2) % 8][0] or q[(a + 2) % 8][1] or q[(a + 3) % 8][0] or q[(a + 4) % 8][0] or q[(a + 4) % 8][1] or \
                    q[(a + 5) % 8][0] or q[(a + 5) % 8][1] or q[(a + 6) % 8][0] or q[(a + 6) % 8][1] or q[(a + 7) % 8][
                0] or q[(a + 7) % 8][1]:
                return False
        # LEFT LANE, STRAIGHT CHECK
        if left_lanes[i][0]:
            if q[(a + 2) % 8][0] or q[(a + 2) % 8][1] or q[(a + 3) % 8][0] or q[(a + 3) % 8][1] or q[(a + 6) % 8][0] or \
                    q[(a + 6) % 8][1] or q[(a + 7) % 8][0]:
                return False

    for j in range(len(right_lanes)):
        a = j * 2 + 1
        # RIGHT LANE, RIGHT TURN CHECK
        if right_lanes[j][1]:
            if q[(a + 3) % 8][1] or q[(a + 5) % 8][0] or q[(a + 6) % 8][0]:
                return False
        # RIGHT LANE, STRAIGHT CHECK
        if right_lanes[j][0]:
            if q[(a + 1) % 8][0] or q[(a + 1) % 8][1] or q[(a + 2) % 8][0] or q[(a + 2) % 8][1] or q[(a + 3) % 8][1] or \
                    q[(a + 5) % 8][0] or q[(a + 5) % 8][1] or q[(a + 6) % 8][0]:
                return False
    return True


def possible_configurations_of_stoplights():
    possible_configs = []
    x = [True, False]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        for j in range(2):
                                            for k in range(2):
                                                for l in range(2):
                                                    for m in range(2):
                                                        for n in range(2):
                                                            for o in range(2):
                                                                for p in range(2):
                                                                    test = [[x[a], x[b]], [x[c], x[d]], [x[e], x[f]],
                                                                            [x[g], x[h]], [x[i], x[j]], [x[k], x[l]],
                                                                            [x[m], x[n]], [x[o], x[p]]]
                                                                    if valid_configuration(test):
                                                                        possible_configs.append(test)
    return possible_configs


class Intersection:
    _locations = None
    _rate_of_cars_to_add = None
    _stoplights =  None
    def __init__ (self, rate_of_cars_to_add, s):
        self._locations = [[], [],[],[],[],[],[],[]]
        self._rate_of_cars_to_add = rate_of_cars_to_add
        self._stoplights = s
    def set_locations (self,q):
        self._locations = q
    def set_stoplights(self,s):
        self._stoplights = s
    
    # ARBITRARILY STARTING WITH CARS IN L0, L1, L4, L5 GREEN LIGHT.
    # _INVARIANT FOR _stoplights : NO CRASHES
    
    
    def add_random_car(self, dest_prop):
        car = Car.Car(np.random.randint(0,8), dest_prop)
        self.add_car(car)
        return
    
    def add_car(self, car):
        self._locations[car._location].append(car)
        return
    def change_light(self, i,j, green):
        self._stoplights[i][j] = green
    def green(self, car):
        destination = car._destination
        location = car._location
        ##RIGHT_LANE DESTINATION
        if (destination % 2 == 0):
            ##STRAIGHT
            if (location == (destination + 5) % 8):     
                return self._stoplights[location][0]
            ##RIGHT-TURN
            if (location == (destination + 7) % 8):
                return self._stoplights[location][1]
        ##LEFT_LANE DESTINATION
        else:
            ##STRAIGHT
            if (location == (destination + 3) % 8):
                return self._stoplights[location][0]
            ##LEFT-TURN
            if (location == (destination + 1) % 8):
                return self._stoplights[location][1]
    def stoplight_update(self):
          ##TODO this is just random rn
        for i in range(8):
            for j in range(2):
                self._stoplights[i][j] = not self._stoplights[i][j]
    def stoplight_cost(self, before, after):
        ##TODO. right now just add an arbitrary cost if you have to switch stoplight
        cost = 0
        different = False
        for i in range(8):
            if before [i] != after [i]:
                different = True
        if different:
            cost = stoplight_change_cost
        return cost
    ##Return current config total cost - next config total cost
    def next_step_progress(self, before, after):
        stop_cost = self.stoplight_cost(before, after)
        current_locations = self._locations
        next_locations = self._locations.copy()
        current_cost = total_time_at_intersection(current_locations)



def main():
    test_valid_config()
    ##print(possible_configurations_of_stoplights())
    print(len(possible_configurations_of_stoplights()))
    test_green()
#     for i in range (200):
#         if np.random.randint(0,8) == 8:
#             print("HAHAHA")
    ##TESTS
def test_valid_config():
    q0 = [[True, False],[True, True],[False, False],[False, False],[True, False],[True, True],[False, False],[False, False]]
    print("q0 True = " + str(valid_configuration(q0)))
    q1 = [[True, False],[True, True],[True, False],[False, False],[True, False],[True, True],[False, False],[False, False]]
    print("q1 False = " + str(valid_configuration(q1)))
    q2 = [[False, False],[False, False],[False, False],[False, False],[False, False],[False, False],[False, False],[False, False]]
    print("q2 True = " + str(valid_configuration(q2)))
    q3 = [[False, True],[False, False],[False, False],[True, False],[False, False],[False, False],[False, False],[False, False]]
    print ("q3 False = " + str(valid_configuration(q3)))
def test_green():
    c = Car.testCar(1,0,4)
    s = ([[False, False],[True, False],[False, False],[False, False],[False, False],[False, False],[False, False],[False, False]])
    i = Intersection(0,s)
    print("True = " + str(i.green(c)))
    s = ([[True, True],[False, True],[False, False],[False, False],[False, False],[False, False],[False, False],[False, False]])
    i1 = Intersection(0,s)
    print("False = " + str(i1.green(c)))
    c = Car.testCar(4,0,3)
    s = (([[True, False],[True, True],[False, False],[False, False],[False, True],[True, True],[False, False],[False, False]]))
    i2 = Intersection (0,s)
    print("True = " + str(i2.green(c)))
    c = Car.testCar(4,0,3)
    s = (([[True, False],[True, True],[False, False],[False, False],[True, False],[True, True],[False, False],[False, False]]))
    i3 = Intersection (0,s)
    print("False = " + str(i3.green(c)))
if __name__ == "__main__":
    main()
