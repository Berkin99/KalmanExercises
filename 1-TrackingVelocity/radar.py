import random

class RadarSIM2D: 

    """
    Radar Simulation of moving object with constant velocity 
    * range   : start range of the object (m) 
    * vel     : constant velocity of the object (m/s)
    * std_dev : standart deviation of the measurement (sigma)
    """
    
    def __init__(self, range=float, vel=float, std_dev=float):
        self.startrange = range
        self.objrange = range
        self.objvel = vel
        self.std_dev = std_dev

    """ @param dt : deltatime """
    def iterate(self, dt=float):
        self.objrange += self.objvel * dt

    def get_measurement(self)->float:
        return random.normalvariate(self.objrange,self.std_dev)

    def get_truevel(self)->float:
        return self.objvel 
    
    def get_truerange(self)->float:
        return self.objrange 
    