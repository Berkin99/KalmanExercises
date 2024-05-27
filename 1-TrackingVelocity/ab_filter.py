
import radar
import matplotlib.pyplot as plt
 
radar = radar.RadarSIM2D(0, 1, 0, 5)


""" Alpha Beta Filter """
def alpha_beta_test(alpha,beta):
    
    A = alpha # Alpha α
    B = beta # Beta  ß

    range_real = []
    vel_real   = []

    range_m = []
    vel_m = []

    range_last = 0
    range_next = 0
    range_buf = 0

    vel_last = 0
    vel_next = 0
    
    i = 0
    dt= 1

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


""" Low Pass Filter """
def low_pass_test(Gain = float):

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

    while i<100:
        radar.iterate(1)
        range_real.append(radar.get_truerange())
        vel_real.append(radar.get_truevel())

        Zn = radar.get_measurement()

        range_now = (1-Gain)*range_last + Gain*(Zn)
        range_m.append(range_now) 

        vel_now = (range_now - range_last)/dt
        vel_m.append(vel_now)

        range_last = range_now
        vel_last = vel_now

        i+=1

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)  # 1 satır, 2 sütun, 1. grafik
    plt.plot(vel_m, marker='o',color='red')
    plt.plot(vel_real,color='black')
    plt.title('Velocity')
    plt.xlabel('Measurement')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)

    plt.subplot(1, 2, 2)  # 1 satır, 2 sütun, 2. grafik
    plt.plot(range_m, marker='o',color='purple')
    plt.plot(range_real,color='black')
    plt.title('Range')
    plt.xlabel('Measurement')
    plt.ylabel('Range (m)')
    plt.grid(True)
    plt.show()


low_pass_test(0.1)