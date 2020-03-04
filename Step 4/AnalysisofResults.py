#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:23:06 2020

@author: elysiachang
"""

import numpy as np
import matplotlib.pyplot as plt


#MAIN SCRIPT
lengthsList = [0.3048,0.3556,0.4064,0.4572,0.508] #in meters to stay 
                                                  #consistent with metric units.
                                                  # Lengths in inches are 12, 14, 16, 18, 20
lengthsArray = np.array(lengthsList)
T = 2.0045*(lengthsArray**0.5)+0.0077             #Based on the eq'n from reading. 
                                                  #Period is in seconds.

plt.plot(lengthsArray, T)
plt.ylabel('Period (s)')
plt.xlabel('Lengths (m)')