import random

number_of_destinations = 8
number_of_locations = 8

class Car:
    _location = None
    _time_elapsed = 0
    _destination = None
    
    def __init__ (self, location, dest_prop):
        self._location = location
        self._time_elapsed = 0
        
        random_prop = random.random() * dest_prop * 2
        
        ##RIGHT LANE 
        if self._location % 2 == 1:
            ##straight
            if random_prop >= .5:
                self._destination = (self._location + 3) % number_of_destinations
            ##right-turn
            else:
                self._destination = (self._location + 1) % number_of_destinations
            ##right-turn
        ##LEFT LANE
        else: 
            ##straight
            if random_prop >= .5:
                self._destination = (self._location + 5) % number_of_destinations
            ##left-turn
            else:
                self._destination = (self._location + 7) % number_of_destinations
    def add_time(self, i):
        self._elapsed_time = self._elapsed_time + i
        return
class testCar:
    _location = None
    _time_elapsed = None
    _destination = None
    def __init__ (self, loc, time, dst):
        self._location = loc
        self._time_elapsed = time
        self._destination = dst
##TESTS   
def main():
    c0 = Car(4, .5)
    print (c0._destination)
    
    c1 = Car(1, .5)
    print (c1._destination)
        
    
if __name__ == "__main__":
    main()