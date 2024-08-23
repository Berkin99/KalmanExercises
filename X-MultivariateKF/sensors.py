
import random

class SensorType:
    UNDEFINED    = 0
    POSITION     = 1
    VELOCITY     = 2
    ACCELERATION = 3

class Sensor:
    def __init__(self, stype = SensorType, start = 0.0, std_dev = 0.0):
        self.type = stype
        self.real = start;
        self.std_dev = std_dev
        self.lasti = 0
        self.lastrandom = 0

    def iterate(self, real = float):
        self.real = real
        i = random.random()
        self.lasti = self.lasti * (1 - i) + i * i
        self.lastrandom = self.lastrandom * self.lasti + random.random() * self.std_dev*2 * (1 - self.lasti)

    def value(self)->float:
        return random.normalvariate(self.real, self.lastrandom)