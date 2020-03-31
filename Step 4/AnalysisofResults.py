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
import statistics

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

# Calculate accelerations in G units from milliG (and time from milliseconds to seconds)
# We did this part by ourselves
first_trial_array = first_trial_array/1000
second_trial_array = second_trial_array/1000
third_trial_array = third_trial_array/1000
fourth_trial_array = fourth_trial_array/1000
fifth_trial_array = fifth_trial_array/1000

# Calculate Theta and Apply Median Filter (Window size =3)
# We did this part by ourselves and then checked with Jenn's starter code on this part
theta12 = sig.medfilt(np.arctan2(first_trial_array[:,0], np.sqrt(first_trial_array[:,1] ** 2) + (first_trial_array[:,2] ** 2)), 3)
theta14 = sig.medfilt(np.arctan2(second_trial_array[:,0], np.sqrt(second_trial_array[:,1] ** 2) + (second_trial_array[:,2] ** 2)), 3)
theta16 = sig.medfilt(np.arctan2(third_trial_array[:,0], np.sqrt(third_trial_array[:,1] ** 2) + (third_trial_array[:,2] ** 2)), 3)
theta18 = sig.medfilt(np.arctan2(fourth_trial_array[:,0], np.sqrt(fourth_trial_array[:,1] ** 2) + (fourth_trial_array[:,2] ** 2)), 3)
theta20 = sig.medfilt(np.arctan2(fifth_trial_array[:,0], np.sqrt(fifth_trial_array[:,1] ** 2) + (fifth_trial_array[:,2] ** 2)), 3)

# Calculate accelerations in m/s^2 units (cons.g is 9.80665 m/s^2)
# We received assistance from Jenn's starter code on this part
first_trial_array[:,0:2] = first_trial_array[:,0:2]*cons.g
second_trial_array[:,0:2] = second_trial_array[:,0:2]*cons.g
third_trial_array[:,0:2] = third_trial_array[:,0:2]*cons.g
fourth_trial_array[:,0:2] = fourth_trial_array[:,0:2]*cons.g
fifth_trial_array[:,0:2] = fifth_trial_array[:,0:2]*cons.g

# *******************************

# PLOTS
# Acceleration vs Time Graphs
# Graphs of Accelerations and Theta

# Trial 1 - 12 Inches
# We did the acceleration part by ourselves and then checked with Jenn's starter code on the theta part
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8], sharex=True)
ax1.plot(first_trial_array[:,3][0:-20], first_trial_array[:,0][0:-20], "#9467bd")
ax1.set_title('X Accel vs Time, Length 12 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(first_trial_array[:,3][0:-20], first_trial_array[:,1][0:-20], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(first_trial_array[:,3][0:-20], first_trial_array[:,2][0:-20], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(first_trial_array[:,3][0:-20], theta12[:][0:-20], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 2 - 14 Inches
# We did the acceleration part by ourselves and then checked with Jenn's starter code on the theta part
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(second_trial_array[:,3][0:-12], second_trial_array[:,0][0:-12], "#9467bd")
ax1.set_title('X Accel vs Time, Length 14 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(second_trial_array[:,3][0:-12], second_trial_array[:,1][0:-12], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(second_trial_array[:,3][0:-12], second_trial_array[:,2][0:-12], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(second_trial_array[:,3][0:-12], theta14[:][0:-12], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 3 - 16 Inches
# We did the acceleration part by ourselves and then checked with Jenn's starter code on the theta part
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(third_trial_array[:,3][0:-23], third_trial_array[:,0][0:-23], "#9467bd") # chop off
ax1.set_title('X Accel vs Time, Length 16 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(third_trial_array[:,3][0:-23], third_trial_array[:,1][0:-23], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(third_trial_array[:,3][0:-23], third_trial_array[:,2][0:-23], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(third_trial_array[:,3][0:-23], theta16[:][0:-23], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 4 - 18 Inches
# We did the acceleration part by ourselves and then checked with Jenn's starter code on the theta part
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(fourth_trial_array[:,3][0:-12], fourth_trial_array[:,0][0:-12], "#9467bd")
ax1.set_title('X Accel vs Time, Length 18 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(fourth_trial_array[:,3][0:-12], fourth_trial_array[:,1][0:-12], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(fourth_trial_array[:,3][0:-12], fourth_trial_array[:,2][0:-12], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(fourth_trial_array[:,3][0:-12], theta18[:][0:-12], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# Trial 5 - 20 Inches
# We did the acceleration part by ourselves and then checked with Jenn's starter code on the theta part
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(fifth_trial_array[:,3][0:-5], fifth_trial_array[:,0][0:-5], "#9467bd")
ax1.set_title('X Accel vs Time, Length 20 Inches')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(fifth_trial_array[:,3][0:-5], fifth_trial_array[:,1][0:-5], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(fifth_trial_array[:,3][0:-5], fifth_trial_array[:,2][0:-5], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(fifth_trial_array[:,3][0:-5], theta20[:][0:-5], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

# *******************************

# Period Calculations

# Trial 1 - 12 Inches
# Graphing the peaks of the sine waves for trial 1 using the original data
# We used "distance=30" to help detect and account for only the peaks that we wanted to include
time1 = first_trial_array[:,3][0:-20]
y1 = theta12[:][0:-20]
y_pks1, _ = sig.find_peaks(y1, distance=30)
plt.plot(time1, y1, 'r-', time1[y_pks1], y1[y_pks1], 'b.')
plt.title('Trial 1 (12 Inches) Original Graph Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.show()

# find_period1 takes zero parameters
# it inputs the data from graphing the peaks above as well as a for loop to find the time
# differences between each of the peaks and then appends it to the interval to take the mean
# it returns the average period and saves it as a variable named period1
def find_period1():
    time1 = first_trial_array[:,3][0:-20]
    y1 = theta12[:][0:-20]
    y_pks1, _ = sig.find_peaks(y1, distance=30)
    pk_time = time1[y_pks1]
    difference = []
    for i in range(len(pk_time)-1):
        interval = pk_time[i+1]-pk_time[i]
        difference.append(interval)
    average_period = statistics.mean(difference)
    return average_period

period1 = find_period1()

# Trial 2 - 14 Inches
# Graphing the peaks of the sine waves for trial 2 using the median filtered data
# We used "distance=30" to help detect and account for only the peaks that we wanted to include
time2 = second_trial_array[:,3][0:-12]
y2 = theta14[:][0:-12]
y_filt2 = sig.medfilt(y2)
y_filt_pks2, _ = sig.find_peaks(y_filt2, distance=30)
plt.plot(time2, y_filt2, 'r-', time2[y_filt_pks2], y_filt2[y_filt_pks2], 'b.')
plt.title('Trial 2 (14 Inches) Original Median Filtered Graph Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.show()

# find_period2 takes zero parameters
# it inputs the data from graphing the peaks above as well as a for loop to find the time
# differences between each of the peaks and then appends it to the interval to take the mean
# it returns the average period and saves it as a variable named period2
def find_period2():
    time2 = second_trial_array[:,3][0:-12]
    y2 = theta14[:][0:-12]
    y_filt2 = sig.medfilt(y2)
    y_filt_pks2, _ = sig.find_peaks(y_filt2, distance=30)
    pk_time = time2[y_filt_pks2]
    difference = []
    for i in range(len(pk_time)-1):
        interval = pk_time[i+1]-pk_time[i]
        difference.append(interval)
    average_period = statistics.mean(difference)
    return average_period

period2 = find_period2()

# Trial 3 - 16 Inches
# Graphing the peaks of the sine waves for trial 3 using the original data
# We used "distance=40" to help detect and account for only the peaks that we wanted to include
time3 = third_trial_array[:,3][0:-22]
y3 = theta16[:][0:-22]
y_pks3, _ = sig.find_peaks(y3, distance=40)
plt.plot(time3, y3, 'r-', time3[y_pks3], y3[y_pks3], 'b.')
plt.title('Trial 3 (16 Inches) Original Graph Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.show()

# find_period3 takes zero parameters
# it inputs the data from graphing the peaks above as well as a for loop to find the time
# differences between each of the peaks and then appends it to the interval to take the mean
# it returns the average period and saves it as a variable named period3
def find_period3():
    time3 = third_trial_array[:,3][0:-22]
    y3 = theta16[:][0:-22]
    y_pks3, _ = sig.find_peaks(y3, distance=40)
    pk_time = time3[y_pks3]
    difference = []
    for i in range(len(pk_time)-1):
        interval = pk_time[i+1]-pk_time[i]
        difference.append(interval)
    average_period = statistics.mean(difference)
    return average_period

period3 = find_period3()

# Trial 4 - 18 Inches
# Graphing the peaks of the sine waves for trial 4 using the median filtered data
# We used "distance=30" to help detect and account for only the peaks that we wanted to include
time4 = fourth_trial_array[:,3][0:-12]
y4 = theta18[:][0:-12]
y_filt4 = sig.medfilt(y4)
y_filt_pks4, _ = sig.find_peaks(y_filt4, distance=30)
plt.plot(time4, y_filt4, 'r-', time4[y_filt_pks4], y_filt4[y_filt_pks4], 'b.')
plt.title('Trial 4 (18 Inches) Original Median Filtered Graph Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.show()

# find_period4 takes zero parameters
# it inputs the data from graphing the peaks above as well as a for loop to find the time
# differences between each of the peaks and then appends it to the interval to take the mean
# it returns the average period and saves it as a variable named period4
def find_period4():
    time4 = fourth_trial_array[:,3][0:-12]
    y4 = theta18[:][0:-12]
    y_filt4 = sig.medfilt(y4)
    y_filt_pks4, _ = sig.find_peaks(y_filt4, distance=30)
    pk_time = time4[y_filt_pks4]
    difference = []
    for i in range(len(pk_time)-1):
        interval = pk_time[i+1]-pk_time[i]
        difference.append(interval)
    average_period = statistics.mean(difference)
    return average_period

period4 = find_period4()

# Trial 5 - 20 Inches
# Graphing the peaks of the sine waves for trial 4 using the original data
time5 = fifth_trial_array[:,3][0:-5]
y5 = theta20[:][0:-5]
y_pks5, _ = sig.find_peaks(y5)
plt.plot(time5, y5, 'r-', time5[y_pks5], y5[y_pks5], 'b.')
plt.title('Trial 5 (20 Inches) Original Graph Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.show()

# find_period5 takes zero parameters
# it inputs the data from graphing the peaks above as well as a for loop to find the time
# differences between each of the peaks and then appends it to the interval to take the mean
# it returns the average period and saves it as a variable named period5
def find_period5():
    time5 = fifth_trial_array[:,3][0:-5]
    y5 = theta20[:][0:-5]
    y_pks5, _ = sig.find_peaks(y5)
    pk_time = time5[y_pks5]
    difference = []
    for i in range(len(pk_time)-1):
        interval = pk_time[i+1]-pk_time[i]
        difference.append(interval)
    average_period = statistics.mean(difference)
    return average_period

period5 = find_period5()