#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:53:59 2020

@author: lilikouchida
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import cos
from scipy.signal import find_peaks



#CONSTANTS/GIVENS
g = 9.81 #defines the constant g
time = np.arange(0,15,0.025) #creates a new array called time which includes all values
#between 0 and 15 seconds by 0.025.

#INITIAL CONDITIONS
initial_angle = 45
theta0 = np.radians(initial_angle)
omega0 = np.radians(0.0) #initial acceleration

def equation(l):
    omega = np.sqrt(g/l) #in UCM and SHM, the magnitude of omega is constant
    theta = [theta0*cos(omega*t) for t in time] 
    alpha = [-(theta0)*(omega**2)*cos(omega*t) for t in time]
    plt.plot(time, theta) #blue line
    plt.plot(time, alpha) #orange line
    plt.title('Time vs. Theta (blue)+Alpha (orange)')
    plt.show()

equation(3)

s = theta
peaks, _ = find_peaks(s)
np.diff(peaks)

time_between_peaks = [time[i] for i in peaks] #Gives the times at wich the peaks occur

for i in range(len(time_between_peaks)):
    time_interval_array = []
    time_interval = time_between_peaks[i]-time_between_peaks[i-1]
    time_interval_array.apend[time_interval]
    
    
  



