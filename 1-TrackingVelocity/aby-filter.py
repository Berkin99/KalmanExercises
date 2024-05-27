
# Tracking the constant velocity of the object

import radar
import matplotlib.pyplot as plt
 
radar = radar.RadarSIM2D(0, 1, 0.03, 1)

range_real = []
vel_real   = []

range_m = []
vel_m = []

range_last = 0
range_next = 0

vel_last = 0
vel_next = 0

acc_last = 0
acc_next = 0

i = 0
dt= 1


A = 0.9  # Alpha α
B = 0.1  # Beta  ß
Y = 0.01  # Gamma 

""" Alpha Beta Gamma Filter """
while i<100:
    radar.iterate(1)
    range_real.append(radar.get_truerange())
    vel_real.append(radar.get_truevel())

    # 1: Get the measurement 
    Zn = radar.get_measurement()

    """ State Update Equations """
    # 2: Current Estimate with State Update Equation    
    range_now   = range_next  + A*(Zn - range_next)
    vel_now     = vel_next    + B*(Zn - range_next)/dt
    acc_now     = acc_next    + Y*(Zn - range_next)/(0.5*dt*dt)

    """ State Extrapolation Equations """
    # 3: Calculating the next state for next State Update Equation
    range_next = range_now + vel_now*dt + acc_now*dt*dt/2  #  x̂n+1,n = x̂n,n + vn,n*dt + an,n*dt^2 /2    
    range_last = range_now  

    vel_next = vel_now + acc_now*dt 
    vel_last = vel_now
    
    acc_next = acc_now
    acc_last = acc_now

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

#     vel_now =  0.9*vel_last + 0.1*(Zn - range_last)/dt
#     vel_m.append(vel_now)

#     range_now = 0.1*range_last + 0.9*(Zn)
#     range_m.append(range_now) 

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