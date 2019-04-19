# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 04:21:01 2019

@author: Julius 本機
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio as io

#Set up some parameter
scale = 100
k = 10
simulation_time = 300
time_resolution = 0.1

#Set up some Variable
R = np.zeros((scale+1,scale+1))
V = np.zeros((scale+1,scale+1))
F = np.zeros((scale+1,scale+1))

#Initial condition
'''
#Guassian
A,mu,sigma = 10,5,0.5
x, y = np.meshgrid(np.linspace(0,scale+1,scale+1), np.linspace(0,scale+1,scale+1))
d = np.sqrt((x-scale/3)**2+(y-scale/3)**2)
g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
R = g
'''
R[5,35] = 10
R[5,65] = 10

def frame(R,V,t):
    R1 = np.delete(R,0,0)
    R1 = np.append(R1,np.zeros((1,scale+1)),0)
    R2 = np.delete(R,scale,0)
    R2 = np.append(np.zeros((1,scale+1)),R2,0)
    R3 = np.delete(R,0,1)
    R3 = np.append(R3,np.zeros((scale+1,1)),1)
    R4 = np.delete(R,scale,1)
    R4 = np.append(np.zeros((scale+1,1)),R4,1)
    F  = -k*(R*4-R1-R2-R3-R4)
    
    #Boundary
    F[0,:] = 0
    F[-1,:] = 0
    F[:,0] = 0
    F[:,-1] = 0
    
    V += F*time_resolution
    R += V*time_resolution
    
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(R,vmax = 0.5,vmin = -0.5,cmap = 'gray')
    ax.set(xlabel='Offset', ylabel='Offset',title='fame:{}'.format(t))
    
    fig.canvas.draw()  # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image

kwargs_write = {'fps':24.0, 'quantizer':'nq'}
io.mimsave('./2D_Transverse_wave.gif', [frame(R,V,t) for t in range(simulation_time)], fps=20)