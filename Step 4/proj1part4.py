#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:34:04 2020
@author: lilikouchida
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:23:06 2020
@author: elysiachang
"""

#import os
#import numpy as np
#import matplotlib.pyplot as plt
#
#path = "/Users/elysiachang/Documents/GitHub/project-1-elysia-chang-liliko-uchida/Step 3"
#
#
##MAIN SCRIPT
#lengthsList = [0.3048,0.3556,0.4064,0.4572,0.508] #in meters to stay 
#                                                  #consistent with metric units.
#                                                  # Lengths in inches are 12, 14, 16, 18, 20
#lengthsArray = np.array(lengthsList)
#T = 2.0045*(lengthsArray**0.5)+0.0077             #Based on the eq'n from reading. 
#                                                  #Period is in seconds.
#
#plt.plot(lengthsArray, T)
#plt.ylabel('Period (s)')
#plt.xlabel('Lengths (m)')
#
#os.chdir(path)
#print(os.getcwd())
#
#fin = open("twelve.csv", "r", encoding="utf8") # opens the csv file
#
## find something that reads in CSV
## split lines
#
#fin.close() # closes the original text file
#
#
#####################################################################################################
#IMPORT STATEMENTS
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks




###############################################################################################
#GETTING CSV FILES
path = "/Users/lilikouchida/Desktop/school/ES2/project-1-elysia-chang-liliko-uchida/Step 3"

os.chdir(path)
print(os.getcwd())

first_trial = 'twelve.csv'
second_trial = 'fourteen.csv'
third_trial = 'sixteen.csv'
fourth_trial = 'eighteen.csv'
fifth_trial = 'twenty.csv'

###############################################################################################

#CUSTOM FUNCTIONS

#These functions convert the CSV files into arrays.
first_trial_array = np.genfromtxt('twelve.csv',delimiter=',')
second_trial_array = np.genfromtxt('fourteen.csv',delimiter=',')
third_trial_array = np.genfromtxt('sixteen.csv',delimiter=',')
fourth_trial_array = np.genfromtxt('eighteen.csv',delimiter=',')
fifth_trial_array = np.genfromtxt('twenty.csv',delimiter=',')







###############################################################################################
#PLOTS
#Acceleration vs. Time 
#Trial 1
x1 = first_trial_array[:,3]/1000 
y1 = first_trial_array[:,0]
plt.plot(x1,y1,".-",)
plt.title('Trial 1 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('x acceleration')
plt.show()

y11 = first_trial_array[:,2]
plt.plot(x1,y11,".-",)
plt.title('Trial 1 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z acceleration')
plt.show()


#Trial 2

x2 = second_trial_array[:,3]/1000 
y2 = second_trial_array[:,0]
plt.plot(x2,y2,".-")
plt.title('Trial 2 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('x acceleration')
plt.show()

y22 = first_trial_array[:,2]
plt.plot(x1,y22,".-",)
plt.title('Trial 2 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z acceleration')
plt.show()


#Trial 3
x3 = third_trial_array[:,3]/1000 
y3 = third_trial_array[:,0]
plt.plot(x3,y3,".-")
plt.title('Trial 3 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('x acceleration')
plt.show()

y33 = first_trial_array[:,2]
plt.plot(x1,y33,".-",)
plt.title('Trial 3 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z acceleration')
plt.show()


#Trial 4
x4 = fourth_trial_array[:,3]/1000 
y4 = fourth_trial_array[:,0]
plt.plot(x4,y4,".-")
plt.title('Trial 4 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('x acceleration')
plt.show()

y44 = first_trial_array[:,2]
plt.plot(x1,y44,".-",)
plt.title('Trial 4 w/ YZAcceleration')
plt.xlabel('Time')
plt.ylabel('Z acceleration')
plt.show()

#Trial 5
x5 = fifth_trial_array[:,3]/1000 
y5 = fifth_trial_array[:,0]
plt.plot(x5,y5,".-")
plt.title('Trial 5 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('x acceleration')
plt.show()

y2 = first_trial_array[:,2]
plt.plot(x1,y2,".-",)
plt.title('Trial 5 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z acceleration')
plt.show()

###############################################################################################
#CALCULATIONS
#CALCULATE/GRAPH THETA
#Trial 1
def find_tilt_x(first_trial_array):
    y = first_trial_array[:,0]
    x = np.sqrt(first_trial_array[:,1]**2 + first_trial_array[:,2]**2)
    tilt_x = np.arctan2(y, x)
    return tilt_x

tilt_x = find_tilt_x(first_trial_array)

def find_tilt_y(first_trial_array):
    y = first_trial_array[:,1]
    x = np.sqrt(first_trial_array[:,0]**2 + first_trial_array[:,2]**2)
    tilt_y = np.arctan2(y, x)
    return tilt_y


def find_tilt_z(first_trial_array):
    y = np.sqrt(first_trial_array[:,0]**2 + first_trial_array[:,1]**2)
    x = first_trial_array[:,2]
    tilt_z = np.arctan2(y, x)
    return tilt_z

tilt_x = find_tilt_x(first_trial_array)
tilt_y = find_tilt_y(first_trial_array)
tilt_z = find_tilt_z(first_trial_array)

#plt.plot(first_trial_array[:,3], tilt_x)
plt.plot(first_trial_array[:,3], tilt_z)
plt.title('z tilt (theta) vs. time')
plt.xlabel('Time')
plt.ylabel('theta')

#CALCULATING THE PERIOD
x = tilt_z
peaks, _ = find_peaks(x) #returns the indices in the tilt_z array that correspond w. peaks
a=first_trial_array[:,3] 
times = a.tolist() #converts the times in trial 1 to its own list.
times_of_peaks=list()
for i in peaks:
    time = times[i]
    times_of_peaks.append(time)
    
    
    


