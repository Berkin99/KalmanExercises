
# Tracking the constant velocity of the object

import radar
import matplotlib.pyplot as plt
 
radar = radar.RadarSIM2D(0, 1, 5)



range_m = []
vel_m = []

range_last = 0
vel_last = 0
vel_est = 0

i = 0
dt= 1

while i<100:
    radar.iterate(1)
    range_now = radar.get_measurement()
    range_m.append( range_now ) 
    # vel_now = (range_now - range_last) / dt 
    vel_now = vel_last*0.8 + ((range_now - range_last) / dt)*0.2 

    vel_m.append(vel_now)

    range_last = range_now
    vel_last = vel_now

    vel_est = vel_est*0.95 + vel_now*0.05

    i+=1

print(vel_est)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 1 satır, 2 sütun, 1. grafik
plt.hist(vel_m, bins=100, density=True, alpha=0.6, color='g')

plt.subplot(1, 2, 2)  # 1 satır, 2 sütun, 2. grafik
plt.plot(range_m, marker='o')
plt.title('Sim')
plt.xlabel('Measurement')
plt.ylabel('Range (m)')
plt.grid(True)
plt.show()