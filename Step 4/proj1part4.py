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
import math

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
plt.title('Trial 2')
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
plt.title('Trial 3')
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
plt.title('Trial 4')
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
plt.title('Trial 5')
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
#CALCULATE THETA
#Trial 1
f = first_trial_array[:,2]
zacc1_list = f.tolist() #Converts the z acceleration column in trial 1
#data to a list
zacc1_array = np.array(zacc1_list) #Converts just the z accelerations for trial 1 to a single row array.
f1 = first_trial_array[:,0]
xacc1_list = f1.tolist() 
xacc1_array = np.array(xacc1_list) #Now we have two, single row arrays (one for x acceleration, one for 
#z acceleration) which we can perform calculations on.
sqrt = (math.sqrt((zacc1_array**2)+(xacc1_array**2)))
sqrt_array = np.array(sqrt)
sin_inverse = sqrt_array/zacc1_array
sin_inverse_array = np.array(sin_inverse)
theta = math.asin(sin_inverse_array)

#CALCULATE PERIOD 
#Trial 1
#a = first_trial_array[:,0]
#accx1 = a.tolist()
#for i in accx1:
#    if accx1[i-1]>accx1[i]<accx1[i+1]:
#        peak = accx1[i]
#        time = first_trial_array[i,3]
#        print (time)
#        
        
###############################################################################################

        









#def find_tilt_y(first_lengthsArray):
#    y = first_lengthsArray[1]
#    x = math.sqrt(first_lengthsArray[0]**2 + first_lengthsArray[2]**2)
#    tilt_y = math.atan2(y, x)
#    return tilt_y
#
#def find_tilt_z(first_lengthsArray):
#    y = math.sqrt(first_lengthsArray[0]**2 + first_lengthsArray[1]**2)
#    x = first_lengthsArray[2]
#    tilt_z = math.atan2(y, x)
#    return tilt_z

#def new_array(first_lengthsArray):
    #time = first_lengthsArray[3]
#    y = first_lengthsArray[:,0]
#    x = math.sqrt((first_lengthsArray[1])**2 + (first_lengthsArray[2])**2)
#    tilt_x = math.atan2(y, x)
#    return tilt_x
#
#new_array(first_lengthsArray)

#file(first_trial) # call the function
#first_lengthsArray = file(first_trial) # properly return variables into functions

#accx_first_trial = first_lengthsArray[:,0]
#accx_first_trial_array = np.array(accx_first_trial)
#time_first_trial = first_lengthsArray[:,3]
#time_first_trial_array = np.array(time_first_trial)
#
#
#plt.plot(accx_first_trial_array, time_first_trial_array)

#def new_array(trial):
#    newArray = trial*2
#    return newArray
#
#print(new_array(first_trial))

#def new_array(lengthsArray):
#    y = acc_x
#    x = math.sqrt(acc_y**2 + acc_z**2)
#    tilt_x = math.atan2(y, x)









