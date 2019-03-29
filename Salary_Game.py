# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:34:55 2019

@author: Julius 本機
"""
import numpy as np
import matplotlib.pyplot as plt

n = 1000
m = 10
dm = 1
k = 1000

M_S = np.ones(n)
M_S = m * M_S

x = np.ones(k)

#可負債模式
while k > 0:
    a = np.random.randint(1,n)
    b = np.random.randint(1,n)
    c = np.random.randint(1,3)
    if a==b:
        M_S[a] =  M_S[a]
        M_S[b] =  M_S[b]
    else:
        if c == 1:
            k += -1
        else:
            M_S[a] =  M_S[a] - dm
            M_S[b] =  M_S[b] + dm
            k +=-1
        
plt.hist(M_S)
plt.show()
'''
while k > 0:
    a = np.random.randint(1,n)
    b = np.random.randint(1,n)
    c = np.random.randint(1,3) #代表猜拳，C=1代表平手
    if a==b:
        M_S[a] =  M_S[a]
        M_S[b] =  M_S[b]
    else:
        if M_S[a] <= 0 or M_S[b] <= 0:
            M_S[a] =  M_S[a]
            M_S[b] =  M_S[b]
        else:
            if c == 1:
                k += -1
            else:
                M_S[a] =  M_S[a] - dm
                M_S[b] =  M_S[b] + dm
                k +=-1
plt.hist(M_S)
plt.show()  
'''            