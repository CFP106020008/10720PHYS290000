# -*- coding: utf-8 -*-
'''
Spyder Editor

This is a temporary script file.
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100,endpoint=False)
A,mu,sigma = 10,5,0.5
y_1 = np.zeros(100)
n = 100

for i in range(1,n):
    y = A*np.exp(-(x-mu)**2/2/sigma**2) 
    dy = np.random.normal(1,1,100)
    y += dy
    plt.plot(x,y)
    y_1 = y_1 + y

plt.show()
plt.plot(x,y_1/n)
plt.show()