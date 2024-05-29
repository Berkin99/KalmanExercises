
import lazermeter
import matplotlib.pyplot as plt
 
lazer = lazermeter.LazerMeterSIM2D(0, 0.2, 0, 0.1)

""" 
    Kalman Filter 
    @param Rn = measurement uncertainity
    @param q  = process variance 
"""
def kalman_test(Rn = float , q = float):
    range_real = [0,15]
    vel_real   = []

    range_m    = []
    vel_m      = []

    kalmangain = []

    range_next = 0
    vel_next = 0

    prange_next = 81    # Initialization of next range estimation variance

    i = 0
    dt= 1

    while i<100:
        lazer.iterate(1)
        range_real.append(lazer.get_truerange())
        vel_real.append(lazer.get_truevel())

        # 1: Get the measurement 
        Zn = lazer.get_measurement()

        """ State Update Equations """
        # 2: Current Estimate with State Update Equation
        Kn = (prange_next / (prange_next + Rn) )
        range_now  = range_next  + Kn * (Zn - range_next)
        vel_now    = vel_next
        prange_now = ( 1 - Kn ) * prange_next 

        """ State Extrapolation Equations """
        # 3: Calculating the next state for next State Update Equation
        range_next = range_now + vel_now * dt    
        vel_next = vel_now
        prange_next = prange_now + q # Prediction of next estimation variance with process variance 

        # E: Plot values
        vel_m.append(vel_now)
        range_m.append( range_now ) 
        kalmangain.append(Kn)

        i+=1

    plt.figure(figsize=(16, 6))

    plt.subplot(1, 3, 1)  # 1 satır, 2 sütun, 1. grafik
    plt.plot(vel_m, marker='o',color='green')
    plt.plot(vel_real,color='black')
    plt.title('Velocity')
    plt.xlabel('Measurement')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)

    plt.subplot(1, 3, 2)  # 1 satır, 2 sütun, 2. grafik
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

def kalman_test2D(Rn = float):
    range_real = [0,15]
    vel_real   = []
    range_m    = []
    vel_m      = []

    range_next = 0
    vel_next = 0

    prange_next = 81
    
    i = 0
    dt= 1

    while i<100:
        lazer.iterate(1)
        range_real.append(lazer.get_truerange())
        vel_real.append(lazer.get_truevel())

        # 1: Get the measurement 
        Zn = lazer.get_measurement()

        """ State Update Equations """
        # 2: Current Estimate with State Update Equation
        Kn = (prange_next / (prange_next + Rn) )
        range_now = range_next  + Kn*(Zn - range_next)
        vel_now   = vel_next

        prange_now = (1 - Kn ) * prange_next

        """ State Extrapolation Equations """
        # 3: Calculating the next state for next State Update Equation
        range_next = range_now + vel_now * dt    
        
        vel_next = vel_now
        prange_next = prange_now

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
    range_real = [0,15]
    vel_real   = []

    range_m    = []
    vel_m      = []

    kalmangain = []

    range_next = 0
    vel_next = 0

    prange_next = 81    # Initialization of next range estimation variance

    i = 0
    dt= 1

    while i<100:
        lazer.iterate(1)
        range_real.append(lazer.get_truerange())
        vel_real.append(lazer.get_truevel())

        # 1: Get the measurement 
        Zn = lazer.get_measurement()

        """ State Update Equations """
        # 2: Current Estimate with State Update Equation
        Kn = (prange_next / (prange_next + Rn) )
        range_now  = range_next  + Kn * (Zn - range_next)
        vel_now    = vel_next
        prange_now = ( 1 - Kn ) * prange_next 

        """ State Extrapolation Equations """
        # 3: Calculating the next state for next State Update Equation
        range_next = range_now + vel_now * dt    
        vel_next = vel_now
        prange_next = prange_now # Prediction of next estimation variance

        # E: Plot values
        vel_m.append(vel_now)
        range_m.append( range_now ) 
        kalmangain.append(Kn)

        i+=1

    plt.figure(figsize=(16, 6))

    plt.subplot(1, 3, 1)  # 1 satır, 2 sütun, 1. grafik
    plt.plot(vel_m, marker='o',color='green')
    plt.plot(vel_real,color='black')
    plt.title('Velocity')
    plt.xlabel('Measurement')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)

    plt.subplot(1, 3, 2)  # 1 satır, 2 sütun, 2. grafik
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


""" Low Pass Filter """
def low_pass_test(Gain = float):

    range_real = [0,15]
    vel_real   = []

    range_m = []
    vel_m = []

    range_last = 0

    i = 0
    dt= 1

    while i<100:
        lazer.iterate(1)
        range_real.append(lazer.get_truerange())
        vel_real.append(lazer.get_truevel())

        Zn = lazer.get_measurement()

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

kalman_test(5, 12)
# low_pass_test(0.1)