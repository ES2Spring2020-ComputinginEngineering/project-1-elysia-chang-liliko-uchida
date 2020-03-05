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


#PART 4: 
df = pd.read_excel(/Users/lilikouchida/Desktop/school/ES2/project-1-elysia-chang-liliko-uchida/Step 3/twelve.csv)
df.as_matrix()

df = pd.read_excel(/Users/lilikouchida/Desktop/school/ES2/project-1-elysia-chang-liliko-uchida/Step 3/fourteen.csv)
df.as_matrix()

df = pd.read_excel(/Users/lilikouchida/Desktop/school/ES2/project-1-elysia-chang-liliko-uchida/Step 3/sixteen.csv)
df.as_matrix()

df = pd.read_excel(/Users/lilikouchida/Desktop/school/ES2/project-1-elysia-chang-liliko-uchida/Step 3/eighteen.csv)
df.as_matrix()

df = pd.read_excel(/Users/lilikouchida/Desktop/school/ES2/project-1-elysia-chang-liliko-uchida/Step 3/twenty.csv)
df.as_matrix()