# -*- coding: utf-8 -*-

#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





#PART 1: THEORETICAL PERIOD
lengthsList = [0.3048,0.3556,0.4064,0.4572,0.508] #in meters to stay 
                                                  #consistent with metric units.
                                                  # Lengths in inches are 12, 14, 16, 18, 20
lengthsArray = np.array(lengthsList)
T = 2.0045*(lengthsArray**0.5)+0.0077             #Based on the eq'n from reading. 
                                                  #Period is in seconds.

plt.plot(lengthsArray, T)
plt.ylabel('Period (s)')
plt.xlabel('Lengths (m)')


#LIMITS OF THIS MODEL/ASSUMPTIONS BEING MADE: WHY WOULD A MODEL IN THE "REAL" WORLD NEVER
#BEHAVE EXACTLY ACCORDING TO THIS EQUATION? 

#--- Assumptions -----
#1. The pendulum is massless.
#2. There is no air resistence. 
#3. The pivot point of the pendulum is frictionless.

#In real life, it is impossible to create an absolutely frictionless pivot point, as well as 
#create a massless pendulum. These assumptions create plenty of uncertainty in this pendulum
#model built with LEGO because the pivot used is only a plastic knob which, while rotates 
#smoothly, is not frictionless. The pendulum also has mass because it is built from LEGO.