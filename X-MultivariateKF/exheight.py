
""" EXAMPLE HEIGHT KALMAN FILTER """

import time
import matplotlib.pyplot as plt
from sensors import Sensor, SensorType
from rigidbody import RigidBody1D
from kalman import Kalman1D
from pid import Pid

height = 2.8

t = 0
dt = 0.004   #10ms

velReal = []
velMeas = []
posReal = []
posMeas = []
posRaw  = []
obj  = RigidBody1D(0.900)
Sbar = Sensor(SensorType.POSITION,     0 , 0.5)
Sacc = Sensor(SensorType.ACCELERATION, 0 , 0.1)
kf   = Kalman1D(dt, sigmax=0.1, epsilon = 0.05)
hpidz = Pid(0.42,0.00015,0.005)


Fnet = 0
while t < 8:
	obj.iterate(Fnet, dt=dt)
	if( t % 0.01 < dt): Sbar.iterate(real=obj.pos)
	
	Sacc.iterate(real=obj.acc)	
	kf.iterate(Sbar.value(), Sacc.value())

	targetvz = height - kf.state[0][0]
	if targetvz > 1.2: targetvz = 1.2
	currentvz = kf.state[1][0]	
	p = hpidz.pidUpdate(targetvz, currentvz, dt) # 0 to 1000 -> 0gr to 2800g -> 2.8kg -> 28N
	p += 0.441
	if p > 0.8: p = 0.8
	if(t % 0.1 < dt) : print(p)
	Fnet = Fnet*0.6 + ( p * 20.0 ) * 0.4 
	if Fnet < 0: Fnet = 0
	t += dt

	""" Monitorig """
	posRaw.append(Sbar.value())
	posReal.append(obj.pos)
	posMeas.append(kf.state[0])
	velReal.append(obj.vel)
	velMeas.append(kf.state[1])




plt.figure(figsize=(16, 6))

plt.subplot(1, 1, 1)  # 1 satır, 2 sütun, 1. grafik
plt.plot(velMeas, marker='o')
plt.plot(velReal,color='black')
plt.title('Velocity')
plt.xlabel('Measurement')
plt.ylabel('Velocity (m/s)')
plt.grid(True)

plt.subplot(1, 2, 2)  # 1 satır, 2 sütun, 2. grafik
plt.plot(posRaw,  marker='x', color = 'green')
plt.plot(posMeas, marker='o')
plt.plot(posReal, color='black')
plt.title('Range')
plt.xlabel('Measurement')
plt.ylabel('Range (m)')
plt.grid(True)

plt.show()