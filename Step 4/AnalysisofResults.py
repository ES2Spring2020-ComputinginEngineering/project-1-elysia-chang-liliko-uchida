#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:23:06 2020

@author: elysiachang
"""

# IMPORT STATEMENTS
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.constants as cons

path = "/Users/elysiachang/Documents/GitHub/project-1-elysia-chang-liliko-uchida/Step 3"

os.chdir(path)
print(os.getcwd())

first_trial = 'twelve.csv'
second_trial = 'fourteen.csv'
third_trial = 'sixteen.csv'
fourth_trial = 'eighteen.csv'
fifth_trial = 'twenty.csv'

# *******************************

# FUNCTIONS
# Creating a script that can parse in and read data files
# Below are the respective functions that turns each line into a row in an array
# We did this part by ourselves
first_trial_array = np.genfromtxt(first_trial, delimiter=',')
second_trial_array = np.genfromtxt(second_trial, delimiter=',')
third_trial_array = np.genfromtxt(third_trial, delimiter=',')
fourth_trial_array = np.genfromtxt(fourth_trial, delimiter=',')
fifth_trial_array = np.genfromtxt(fifth_trial, delimiter=',')

# Crop arrays to clean data rows
# We received assistance from Jenn's starter code on this part
first_trial_array = first_trial_array[500:1300,:]
second_trial_array = second_trial_array[500:1300,:]
third_trial_array = third_trial_array[500:1300,:]
fourth_trial_array = fourth_trial_array[500:1300,:]
#fifth_trial_array = fifth_trial_array[500:1300,:]

# Calculate accelerations in G units from milliG (and time from milliseconds to seconds)
# We did this part by ourselves
first_trial_array = first_trial_array/1000
second_trial_array = second_trial_array/1000
third_trial_array = third_trial_array/1000
fourth_trial_array = fourth_trial_array/1000
#fifth_trial_array = fifth_trial_array/1000

# Calculate Theta and Apply Median Filter (Window size =3)
# We did this part by ourselves and then checked with Jenn's starter code on this part
theta12 = sig.medfilt(np.arctan2(first_trial_array[:,0], np.sqrt(first_trial_array[:,1] ** 2) + (first_trial_array[:,2] ** 2)), 3)
theta14 = sig.medfilt(np.arctan2(second_trial_array[:,0], np.sqrt(second_trial_array[:,1] ** 2) + (second_trial_array[:,2] ** 2)), 3)
theta16 = sig.medfilt(np.arctan2(third_trial_array[:,0], np.sqrt(third_trial_array[:,1] ** 2) + (third_trial_array[:,2] ** 2)), 3)
theta18 = sig.medfilt(np.arctan2(fourth_trial_array[:,0], np.sqrt(fourth_trial_array[:,1] ** 2) + (fourth_trial_array[:,2] ** 2)), 3)
#theta20 = sig.medfilt(np.arctan2(fifth_trial_array[:,0], np.sqrt(fifth_trial_array[:,1] ** 2) + (fifth_trial_array[:,2] ** 2)), 3)

# Calculate accelerations in m/s^2 units (cons.g is 9.80665 m/s^2)
# We received assistance from Jenn's starter code on this part
first_trial_array[:,0:2] = first_trial_array[:,0:2]*cons.g
second_trial_array[:,0:2] = second_trial_array[:,0:2]*cons.g
third_trial_array[:,0:2] = third_trial_array[:,0:2]*cons.g
fourth_trial_array[:,0:2] = fourth_trial_array[:,0:2]*cons.g
#fifth_trial_array[:,0:2] = fifth_trial_array[:,0:2]*cons.g

# *******************************

# PLOTS
# Acceleration vs Time Graphs
# Graphs of Accelerations and Theta

# Trial 1 - 12 Inches
# We did the acceleration part by ourselves and then checked with Jenn's starter code on the theta part
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8], sharex=True)
ax1.plot(first_trial_array[:,3], first_trial_array[:,0], "#9467bd")
ax1.set_title('X Accel vs Time, Length 12 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(first_trial_array[:,3], first_trial_array[:,1], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(first_trial_array[:,3], first_trial_array[:,2], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(first_trial_array[:,3], theta12[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 2 - 14 Inches
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(second_trial_array[:,3], second_trial_array[:,0], "#9467bd")
ax1.set_title('X Accel vs Time, Length 14 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(second_trial_array[:,3], second_trial_array[:,1], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(second_trial_array[:,3], second_trial_array[:,2], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(second_trial_array[:,3], theta14[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 3 - 16 Inches
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(third_trial_array[:,3], third_trial_array[:,0], "#9467bd")
ax1.set_title('X Accel vs Time, Length 16 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(third_trial_array[:,3], third_trial_array[:,1], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(third_trial_array[:,3], third_trial_array[:,2], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(third_trial_array[:,3], theta16[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 4 - 18 Inches
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(fourth_trial_array[:,3], fourth_trial_array[:,0], "#9467bd")
ax1.set_title('X Accel vs Time, Length 18 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(fourth_trial_array[:,3], fourth_trial_array[:,1], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(fourth_trial_array[:,3], fourth_trial_array[:,2], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(fourth_trial_array[:,3], theta18[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 5 - 20 Inches
#fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
#ax1.plot(fifth_trial_array[:,3], fifth_trial_array[:,0], "#9467bd")
#ax1.set_title('X Accel vs Time, Length 20 Inches')
#ax1.set_ylabel ('Acceleration (m/s^2)')    
#ax2.plot(fifth_trial_array[:,3], fifth_trial_array[:,1], "#17becf")
#ax2.set_title('Y Accel vs Time')
#ax2.set_ylabel ('Acceleration (m/s^2)')
#ax3.plot(fifth_trial_array[:,3], fifth_trial_array[:,2], "#2ca02c")
#ax3.set_title('Z Accel vs Time')
#ax3.set_ylabel ('Acceleration (m/s^2)')
#ax4.plot(fifth_trial_array[:,3], theta20[:], "#ff7f0e")
#ax4.set_title('Theta vs Time')
#ax4.set_ylabel ('Theta (rad)')
#plt.xlabel('Time (s)')
#plt.tight_layout()
#plt.show()