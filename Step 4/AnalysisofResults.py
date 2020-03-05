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
def file1(first_trial):
    first_lengthsArray = np.loadtxt(first_trial, delimiter=',')
    return first_lengthsArray

first_lengthsArray = file1(first_trial)

# SECOND TRIAL
def file2(second_trial):
    second_lengthsArray = np.loadtxt(second_trial, delimiter=',')
    return second_lengthsArray

second_lengthsArray = file2(second_trial)

# THIRD TRIAL
def file3(third_trial):
    third_lengthsArray = np.loadtxt(third_trial, delimiter=',')
    return third_lengthsArray

third_lengthsArray = file3(third_trial)

# FOURTH TRIAL
def file4(fourth_trial):
    fourth_lengthsArray = np.loadtxt(fourth_trial, delimiter=',')
    return fourth_lengthsArray

fourth_lengthsArray = file4(fourth_trial)

# FIFTH TRIAL
def file5(fifth_trial):
    fifth_lengthsArray = np.loadtxt(fifth_trial, delimiter=',')
    return fifth_lengthsArray

fifth_lengthsArray = file5(fifth_trial)



# FIRST TRIAL
#def file1(first_trial):
#    first = np.loadtxt(first_trial, delimiter=',')
#    first_lengthsArray = np.empty((4))
#    with open(first_trial) as csvfile:
#        reader = csv.reader(csvfile, delimiter=',')
#        for row in reader: # this changes all to a list - now, change it to an array
#            length = row
#            print(length)
#            first_lengthsArray = np.append(first_lengthsArray, np.array(length), axis=0)
#    return first # last piece of data

#file1(first_trial)
#first_lengthsArray = file1(first_trial)

#x = first_lengthsArray[:,3]
#y = first_lengthsArray[:,0]
#first_lengthsArray.plt()
#plt.title('Twelve!')
#plt.ylabel('Period (s)')
#plt.xlabel('Lengths (m)')
#plt.show()

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
#def file2(second_trial):
#    with open(second_trial) as csvfile:
#        reader = csv.reader(csvfile, delimiter=',')
#        for row in reader: # this changes all to a list - now, change it to an array
#            length = row
#            second_lengthsArray = np.array(length)
#        return second_lengthsArray # last piece of data
#
#file2(second_trial)
#second_lengthsArray = file2(second_trial)
#
#
## THIRD TRIAL
#def file3(third_trial):
#    with open(third_trial) as csvfile:
#        reader = csv.reader(csvfile, delimiter=',')
#        for row in reader: # this changes all to a list - now, change it to an array
#            length = row
#            third_lengthsArray = np.array(length)
#        return third_lengthsArray # last piece of data
#
#file3(third_trial)
#third_lengthsArray = file3(third_trial)
#
#
## FOURTH TRIAL
#def file4(fourth_trial):
#    with open(fourth_trial) as csvfile:
#        reader = csv.reader(csvfile, delimiter=',')
#        for row in reader: # this changes all to a list - now, change it to an array
#            length = row
#            fourth_lengthsArray = np.array(length)
#        return fourth_lengthsArray # last piece of data
#
#file4(fourth_trial)
#fourth_lengthsArray = file4(fourth_trial)
#
#
#
## FIFTH TRIAL
#def file5(fifth_trial):
#    with open(fifth_trial) as csvfile:
#        reader = csv.reader(csvfile, delimiter=',')
#        for row in reader: # this changes all to a list - now, change it to an array
#            length = row
#            fifth_lengthsArray = np.array(length)
#        return fifth_lengthsArray # last piece of data
#
#file5(fifth_trial)
#fifth_lengthsArray = file5(fifth_trial)