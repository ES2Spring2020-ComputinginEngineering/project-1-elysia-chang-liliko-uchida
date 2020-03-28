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


#********************************************

#CONSTANTS/GIVENS
#Defines constants which will be used in calculations.
g = 9.81 
time = np.arange(0,15,0.025) 
l = 1

#********************************************

#INITIAL CONDITIONS
#Defines state values. #Omega in this case is angular frequency NOT angular velocity
initial_angle = 10
theta0 = np.radians(initial_angle)
omega0 = np.radians(0.0) 

#********************************************

#PLOTTING VALUES

#Equations for omega and theta shown in calculations notes.
#omega = angular frequency
#omega1 = instantaneous angular velocity
omega = np.sqrt(g/l) 
theta = [theta0*cos(omega*t) for t in time] 
alpha = [-(theta0)*(omega**2)*cos(omega*t) for t in time]
omega1 = [(theta0*cos(omega*t))/time for t in time]
plt.plot(time, theta) #blue line
plt.plot(time, alpha) #orange line
plt.title('Time vs. Theta (blue)+Alpha (orange)')
plt.show()

plt.plot(time, omega1)
plt.show()
#********************************************

#CALCULATING THE PERIOD

#returns an array of indices at which maximum values for theta occur.
s = theta
peaks, _ = find_peaks(s)
np.diff(peaks)

#Gives the times at which the peaks occur
time_between_peaks = [time[i] for i in peaks] 

#creates a list which holds the values of delta t between each peak.
#then pops the first element off of the list because the value is negative
#thus an outlier because the last time was subtracted from the first time
#which is unwanted.
time_interval_list = []
for i in range(len(time_between_peaks)):
    time_interval = time_between_peaks[i]-time_between_peaks[i-1]
    time_interval_list.append(time_interval) 
time_interval_list.pop(0)
sum = 0
for i in range(len(time_interval_list)):
    sum = sum + time_interval_list[i]
average_period = sum/(len(time_interval_list))
    



    
    
  



