#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:23:06 2020

@author: elysiachang
"""

# IMPORT STATEMENTS
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
#fifth_trial = 'twenty.csv'

# *******************************

# FUNCTIONS
# Creating a script that can parse in and read data files
# Below are the respective functions that turns each line into a row in an array

#first_trial_array = np.genfromtxt('twelve.csv',delimiter=',')
#second_trial_array = np.genfromtxt('fourteen.csv',delimiter=',')
#third_trial_array = np.genfromtxt('sixteen.csv',delimiter=',')
#fourth_trial_array = np.genfromtxt('eighteen.csv',delimiter=',')
#fifth_trial_array = np.genfromtxt('twenty.csv',delimiter=',')

# FIRST TRIAL
def file1(first_trial):
    first_trial_array = np.loadtxt(first_trial, delimiter=',', dtype=int)
    return first_trial_array

first_trial_array = file1(first_trial)

# SECOND TRIAL
def file2(second_trial):
    second_trial_array = np.loadtxt(second_trial, delimiter=',', dtype=int)
    return second_trial_array

second_trial_array = file2(second_trial)

# THIRD TRIAL
def file3(third_trial):
    third_trial_array = np.loadtxt(third_trial, delimiter=',', dtype=int)
    return third_trial_array

third_trial_array = file3(third_trial)

# FOURTH TRIAL
def file4(fourth_trial):
    fourth_trial_array = np.loadtxt(fourth_trial, delimiter=',', dtype=int)
    return fourth_trial_array

fourth_trial_array = file4(fourth_trial)

# FIFTH TRIAL
#def file5(fifth_trial):
#    fifth_trial_array = np.loadtxt(fifth_trial, delimiter=',', dtype=int)
#    return fifth_trial_array
#
#fifth_trial_array = file5(fifth_trial)

# *******************************

# PLOTS
# Acceleration vs Time Graphs

# TRIAL 1
x1 = first_trial_array[:,3]/1000 
y1 = first_trial_array[:,0]
plt.plot(x1,y1,".-",)
plt.title('Trial 1 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('X Acceleration')
plt.show()

y11 = first_trial_array[:,2]
plt.plot(x1,y11,".-",)
plt.title('Trial 1 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z Acceleration')
plt.show()

# TRIAL 2
x2 = second_trial_array[:,3]/1000 
y2 = second_trial_array[:,0]
plt.plot(x2,y2,".-")
plt.title('Trial 2 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('X Acceleration')
plt.show()

y22 = first_trial_array[:,2]
plt.plot(x1,y22,".-",)
plt.title('Trial 2 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z Acceleration')
plt.show()

# TRIAL 3
x3 = third_trial_array[:,3]/1000 
y3 = third_trial_array[:,0]
plt.plot(x3,y3,".-")
plt.title('Trial 3 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('X Acceleration')
plt.show()

y33 = first_trial_array[:,2]
plt.plot(x1,y33,".-",)
plt.title('Trial 3 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z Acceleration')
plt.show()

# TRIAL 4
x4 = fourth_trial_array[:,3]/1000 
y4 = fourth_trial_array[:,0]
plt.plot(x4,y4,".-")
plt.title('Trial 4 w/ X Acceleration')
plt.xlabel('Time')
plt.ylabel('X Acceleration')
plt.show()

y44 = first_trial_array[:,2]
plt.plot(x1,y44,".-",)
plt.title('Trial 4 w/ Z Acceleration')
plt.xlabel('Time')
plt.ylabel('Z Acceleration')
plt.show()

## TRIAL 5
#x5 = fifth_trial_array[:,3]/1000 
#y5 = fifth_trial_array[:,0]
#plt.plot(x5,y5,".-")
#plt.title('Trial 5 w/ X Acceleration')
#plt.xlabel('Time')
#plt.ylabel('X Acceleration')
#plt.show()
#
#y2 = first_trial_array[:,2]
#plt.plot(x1,y2,".-",)
#plt.title('Trial 5 w/ Z Acceleration')
#plt.xlabel('Time')
#plt.ylabel('Z Acceleration')
#plt.show()

# These are the 5 graphs for the 5 lengths that show time vs acceleration
# Must double-click and save these graphs to our Google Doc

# *******************************

# PENDULUM ANGLE
# Calculating the pendulum angle from the accelerations at each time
# Uses similar logic to the Bubble Level

# These are functions that find the X, Y, Z tilts and returns them as a stored value

# TRIAL 1 - X, Y, Z Tilts
def first_find_tilt_x(first_trial_array):
    y = first_trial_array[:,0]
    x = np.sqrt(first_trial_array[:,1]**2 + first_trial_array[:,2]**2)
    first_tilt_x = np.arctan2(y, x)
    return first_tilt_x

first_tilt_x = first_find_tilt_x(first_trial_array)

def first_find_tilt_y(first_trial_array):
    y = first_trial_array[:,1]
    x = np.sqrt(first_trial_array[:,0]**2 + first_trial_array[:,2]**2)
    first_tilt_y = np.arctan2(y, x)
    return first_tilt_y

first_tilt_y = first_find_tilt_y(first_trial_array)

# If you look at the angle measurements for Y, they are negligible (always zero)
# So, moving forward, we can ignore Y, and focus on calculating tilts X and Z

def first_find_tilt_z(first_trial_array):
    y = np.sqrt(first_trial_array[:,0]**2 + first_trial_array[:,1]**2)
    x = first_trial_array[:,2]
    first_tilt_z = np.arctan2(y, x)
    return first_tilt_z

first_tilt_z = first_find_tilt_z(first_trial_array)

# TRIAL 2 - X, Y, Z Tilts
def second_find_tilt_x(second_trial_array):
    y = second_trial_array[:,0]
    x = np.sqrt(second_trial_array[:,1]**2 + second_trial_array[:,2]**2)
    second_tilt_x = np.arctan2(y, x)
    return second_tilt_x

second_tilt_x = second_find_tilt_x(second_trial_array)

def second_find_tilt_z(second_trial_array):
    y = np.sqrt(second_trial_array[:,0]**2 + second_trial_array[:,1]**2)
    x = second_trial_array[:,2]
    second_tilt_z = np.arctan2(y, x)
    return second_tilt_z

second_tilt_z = second_find_tilt_z(second_trial_array)

# TRIAL 3 - X, Y, Z Tilts
def third_find_tilt_x(third_trial_array):
    y = third_trial_array[:,0]
    x = np.sqrt(third_trial_array[:,1]**2 + third_trial_array[:,2]**2)
    third_tilt_x = np.arctan2(y, x)
    return third_tilt_x

third_tilt_x = third_find_tilt_x(third_trial_array)

def third_find_tilt_z(third_trial_array):
    y = np.sqrt(third_trial_array[:,0]**2 + third_trial_array[:,1]**2)
    x = third_trial_array[:,2]
    third_tilt_z = np.arctan2(y, x)
    return third_tilt_z

third_tilt_z = third_find_tilt_z(third_trial_array)

# TRIAL 4 - X, Y, Z Tilts
def fourth_find_tilt_x(fourth_trial_array):
    y = fourth_trial_array[:,0]
    x = np.sqrt(fourth_trial_array[:,1]**2 + fourth_trial_array[:,2]**2)
    fourth_tilt_x = np.arctan2(y, x)
    return fourth_tilt_x

fourth_tilt_x = fourth_find_tilt_x(fourth_trial_array)

def fourth_find_tilt_z(fourth_trial_array):
    y = np.sqrt(fourth_trial_array[:,0]**2 + fourth_trial_array[:,1]**2)
    x = fourth_trial_array[:,2]
    fourth_tilt_z = np.arctan2(y, x)
    return fourth_tilt_z

fourth_tilt_z = fourth_find_tilt_z(fourth_trial_array)

# TRIAL 5 - X, Y, Z Tilts
#def fifth_find_tilt_x(fifth_trial_array):
#    y = fifth_trial_array[:,0]
#    x = np.sqrt(fifth_trial_array[:,1]**2 + fifth_trial_array[:,2]**2)
#    fifth_tilt_x = np.arctan2(y, x)
#    return fifth_tilt_x
#
#fifth_tilt_x = fifth_find_tilt_x(fifth_trial_array)
#
#def fifth_find_tilt_z(fifth_trial_array):
#    y = np.sqrt(fifth_trial_array[:,0]**2 + fifth_trial_array[:,1]**2)
#    x = fifth_trial_array[:,2]
#    fifth_tilt_z = np.arctan2(y, x)
#    return fifth_tilt_z
#
#fifth_tilt_z = fifth_find_tilt_z(fifth_trial_array)

# We learned from Jenn that the Y tilts are negligible (almost always zero degrees)
# The main focus is on the X and Z tilts, so we should plot those as graphs

# *******************************

# PLOTTING TIME VS PENDULUM ANGLE

# TRIAL 1
# I'm trying to plot the time on the x-axis (taken directly from above which works)
# and I'm trying to plot the pendulum angle as the y-axis (using similar structure)
# I'm getting an "IndexError: too many indices for array" - not sure why...
# Theoretically this graph should print the Angle vs Time

x1 = first_trial_array[:,3]/1000 
y1_angle = first_tilt_x[:,0]
plt.plot(x1,y1_angle,".-",)
plt.title('Trial 1 w/ X Pendulum Angle vs Time')
plt.xlabel('Time')
plt.ylabel('X Pendulum Angle')
plt.show()

z1_angle = first_tilt_z[:,0]
plt.plot(x1,z1_angle,".-",)
plt.title('Trial 1 w/ Z Pendulum Angle vs Time')
plt.xlabel('Time')
plt.ylabel('Z Pendulum Angle')
plt.show()