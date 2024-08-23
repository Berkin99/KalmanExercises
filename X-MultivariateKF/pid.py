# PIDSIM

def constrain(x, min_val, max_val):
    return min(max(x, min_val), max_val)

class Pid:

    MAX_VAL = 800

    def __init__(self,kp,ki,kd) -> None:
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.lasterror = 0
        self.integral = 0

        self.limit         = self.MAX_VAL
        self.limitIntegral = self.MAX_VAL

    def pidUpdate(self,desired,measured,dt):
        output = 0
        error = desired - measured
        output += error * self.kp

        self.integral += self.ki * error * dt
        self.integral = constrain(self.integral,-self.limitIntegral,self.limitIntegral)
        output += self.integral

        derivative = ( error - self.lasterror ) / dt
        self.lasterror = error
        output += derivative * self.kd
        return constrain(output,-self.limit,self.limit)

    def pidSetLimit(self,limit):
        self.limit = limit

    def pidSetLimitIntegral(self,limit):
        self.limitIntegral = limit
    