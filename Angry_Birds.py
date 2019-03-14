# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:24:48 2019

@author: Julius 本機
"""

import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0,100,1000)
px = np.random.random(1)*50+50
py = np.random.random(1)*70
plt.plot(px,py,'.',markersize=24)
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()

theta = float(3.14*float(input('Firing Angle: '))/180)
v = float(input('Initial Velocity: '))

trajectory_x = v*math.cos(theta)*t
trajectory_y = v*math.sin(theta)*t-0.5*9.81*t**2
plt.plot(px,py,'.',markersize=24)
plt.plot(trajectory_x,trajectory_y,linewidth=5)
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()

r = np.zeros(1000)

for i in range(0,1000):
    r[i] = (trajectory_x[i]-px)**2 + (trajectory_y[i]-py)**2

if  np.min(r) <= 16:
    print('命中目標！')
else:
    print('脫靶！脫靶！')
