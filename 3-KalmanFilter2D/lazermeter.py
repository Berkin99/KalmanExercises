
import random

class LazerMeterSIM2D:
    """
    LazerMeter Simulation of moving object with velocity 
    * range   : start range of the object (m) 
    * vel     : start velocity of the object (m/s)
    * acc     : constant acceleration of object (m/s^2)
    * std_dev : standart deviation of the measurement (sigma)
    """
    def __init__(self, range=float, vel=float, acc=float, std_dev=float):
        self.startrange = range
        self.objrange = range
        self.objvel = vel
        self.objacc = acc
        self.std_dev = std_dev

    """ @param dt : deltatime """
    def iterate(self, dt=float):
        self.objrange += self.objvel * dt
        self.objvel += self.objacc * dt

    def get_measurement(self)->float:
        return random.normalvariate(self.objrange,self.std_dev)

    def get_truevel(self)->float:
        return self.objvel 
    
    def get_truerange(self)->float:
        return self.objrange 
    