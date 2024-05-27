
# Tracking the constant velocity of the object

import radar
import matplotlib.pyplot as plt
 
radar = radar.RadarSIM2D(0, 1, 0, 5)

range_real = []
vel_real   = []

range_m = []
vel_m = []

range_last = 0
range_next = 0

vel_last = 0
vel_next = 0

i = 0
dt= 1


A = 0.25 # Alpha α
B = 0.02 # Beta  ß


""" Alpha Beta Filter """
while i<100:
    radar.iterate(1)
    range_real.append(radar.get_truerange())
    vel_real.append(radar.get_truevel())

    # 1: Get the measurement 
    Zn = radar.get_measurement()

    """ State Update Equations """
    # 2: Current Estimate with State Update Equation    
    range_now = range_next + A*(Zn - range_next)
    vel_now = vel_next + B*(Zn - range_next)/dt

    """ State Extrapolation Equations """
    # 3: Calculating the next state for next State Update Equation
    range_next = range_now + vel_now*dt #  x̂n+1,n = x̂n,n + vn,n*dt 
    range_last = range_now   

    vel_next = vel_now
    vel_last = vel_now

    # E: Plot values
    vel_m.append(vel_now)
    range_m.append( range_now ) 

    i+=1

""" Low Pass Filter """
# while i<100:
#     radar.iterate(1)
#     range_real.append(radar.get_truerange())
#     vel_real.append(radar.get_truevel())

#     Zn = radar.get_measurement()

#     range_now = 0.9*range_last + 0.1*(Zn)
#     range_m.append(range_now) 

#     vel_now =  0.2*vel_last + 0.8*(range_now - range_last)/dt
#     vel_m.append(vel_now)

#     range_last = range_now
#     vel_last = vel_now

#     i+=1

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 1 satır, 2 sütun, 1. grafik
plt.plot(vel_m, marker='o',color='green')
plt.plot(vel_real,color='black')
plt.title('Velocity')
plt.xlabel('Measurement')
plt.ylabel('Velocity (m/s)')
plt.grid(True)

plt.subplot(1, 2, 2)  # 1 satır, 2 sütun, 2. grafik
plt.plot(range_m, marker='o')
plt.plot(range_real,color='black')
plt.title('Range')
plt.xlabel('Measurement')
plt.ylabel('Range (m)')
plt.grid(True)
plt.show()