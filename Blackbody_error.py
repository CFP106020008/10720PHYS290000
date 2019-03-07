# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:03:50 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#SI unit
h = 6.62*10**-34 #Planck constant
c = 3*10**8      #speed of light
k = 1.38*10**-23 #Boltzmann Constant JK^-1

v = np.linspace(10**0, 10**15, 100, endpoint=True)
#print(v)

T=float(5000)
B=2*h*v**3/c**2/(math.e**(h*v/k/T)-1)
#print(B)
dB = np.random.normal(0.000000001,0.000000001,100)
B += dB
#plt.errorbar(v, B, yerr=0.5*B, xerr=0.1*v, ecolor="green")

#plt.plot(v, B,"g.")
#plt.plot(v, B,"r--")

plt.plot(v,B,".")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity Watts/Hz/m^2")

plt.show()                