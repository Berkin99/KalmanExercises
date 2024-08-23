
from barometer import BaroeterSIM
import matplotlib.pyplot as plt
 

"""
Object start z          = 2 m
Object velocity z       = 0 m/s
Object acceleration z   = 0 m/s^2
Barometer stddev = 0.15
"""

barsigma = 0.08 #meters
bar = BaroeterSIM(2, 0, 0.8, barsigma)

def kalman_test(Rn = float , q = float):
    measurements = []

    range_real = []
    vel_real   = []

    range_m    = []
    vel_m      = []

    kalmangain = []

    range_next = 2
    vel_next = 0

    prange_next = 0.15    # Initialization of next range estimation variance
    pvel_next = 0.0001

    i = 0
    dt= 0.01    # delta time = 0.01 seconds = 10ms

    while i < 100:
        bar.iterate(dt)
        range_real.append(bar.get_truerange())
        vel_real.append(bar.get_truevel())

        # 1: Get the measurement 
        Zn = bar.get_measurement()
        measurements.append(Zn)

        """ State Update Equations """
        # 2: Current Estimate with State Update Equation
        Kn  =  (prange_next / (prange_next + Rn) )
        Kn2 =  (pvel_next / (pvel_next + Rn))

        range_now  = range_next  + Kn  * (Zn - range_next)
        vel_now    = vel_next    + Kn2 * (Zn - range_next)/dt

        prange_now = ( 1 - Kn ) * prange_next 
        pvel_now = (1 - Kn2) * pvel_next

        """ State Extrapolation Equations """
        # 3: Calculating the next state for next State Update Equation
        range_next = range_now + vel_now*dt  + 0  
        vel_next = vel_now + 0 

        prange_next = prange_now + dt * dt * pvel_now + q 
        pvel_next = pvel_now + q * dt

        # E: Plot values
        vel_m.append(vel_now)
        range_m.append( range_now ) 
        kalmangain.append(Kn)

        i += 1

    plt.figure(figsize=(16, 6))

    plt.subplot(1, 3, 1)  # 1 satır, 2 sütun, 1. grafik
    plt.plot(vel_m, marker='o',color='green')
    plt.plot(vel_real,color='black')
    plt.title('Velocity')
    plt.xlabel('Measurement')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)

    plt.subplot(1, 3, 2)  # 1 satır, 2 sütun, 2. grafik
    plt.plot(measurements, marker='x',alpha = 1, color = 'green')
    plt.plot(range_m, marker='o')
    plt.plot(range_real,color='black')
    plt.title('Range')
    plt.xlabel('Measurement')
    plt.ylabel('Range (m)')
    plt.grid(True)

    plt.subplot(1, 3, 3) 
    plt.plot(kalmangain,color = 'orange')
    plt.title('KalmanGain')
    plt.xlabel('Measurement')
    plt.ylabel('Gain')
    plt.grid(True)
    
    plt.show()

kalman_test(barsigma ,0.0000)