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

import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import math

path = "/Users/elysiachang/Documents/GitHub/project-1-elysia-chang-liliko-uchida/Step 3"

os.chdir(path)
print(os.getcwd())

first_trial = 'twelve.csv'
second_trial = 'fourteen.csv'
third_trial = 'sixteen.csv'
fourth_trial = 'eighteen.csv'
fifth_trial = 'twenty.csv'

# FIRST TRIAL
def file(first_trial):
    with open(first_trial) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: # this changes all to a list - now, change it to an array
            length = row
            first_lengthsArray = np.array(length)
        return first_lengthsArray # last piece of data

file(first_trial)
first_lengthsArray = file(first_trial)

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



# SECOND TRIAL
def file(second_trial):
    with open(second_trial) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: # this changes all to a list - now, change it to an array
            length = row
            second_lengthsArray = np.array(length)
        return second_lengthsArray # last piece of data

file(second_trial)
second_lengthsArray = file(second_trial)


# THIRD TRIAL
def file(third_trial):
    with open(third_trial) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: # this changes all to a list - now, change it to an array
            length = row
            third_lengthsArray = np.array(length)
        return third_lengthsArray # last piece of data

file(third_trial)
third_lengthsArray = file(third_trial)


# FOURTH TRIAL
def file(fourth_trial):
    with open(fourth_trial) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: # this changes all to a list - now, change it to an array
            length = row
            fourth_lengthsArray = np.array(length)
        return fourth_lengthsArray # last piece of data

file(fourth_trial)
fourth_lengthsArray = file(fourth_trial)



# FIFTH TRIAL
#def file(first_trial):
#    with open(first_trial) as csvfile:
#        reader = csv.reader(csvfile, delimiter=',')
#        for row in reader: # this changes all to a list - now, change it to an array
#            length = row
#            first_lengthsArray = np.array(length)
#        return first_lengthsArray # last piece of data
#
#file(first_trial)
#first_lengthsArray = file(first_trial)