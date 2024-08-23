
import random

class BaroeterSIM:
    """
    Barometer Simulation  
    * range   : start range z of the object (m) 
    * vel     : start velocity z of the object (m/s)
    * acc     : constant acceleration z of object (m/s^2)
    * std_dev : standart deviation of the measurement (sigma)
    """
    
    def __init__(self, range_z=float, vel=float, acc=float, std_dev=float):
        self.startrange = range_z
        self.objrange = range_z
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
    