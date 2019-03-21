# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:13:35 2019

@author: Julius 本機
"""

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

im1 = img.imread(r'C:\Users\林彥興\OneDrive\大學\課程\計算物理概論\HW3\DSC_0458.jpg')
im2 = img.imread(r'C:\Users\林彥興\OneDrive\大學\課程\計算物理概論\HW3\DSC_0459.jpg')
im3 = img.imread(r'C:\Users\林彥興\OneDrive\大學\課程\計算物理概論\HW3\DSC_0460.jpg')
im4 = img.imread(r'C:\Users\林彥興\OneDrive\大學\課程\計算物理概論\HW3\DSC_0461.jpg')
im5 = img.imread(r'C:\Users\林彥興\OneDrive\大學\課程\計算物理概論\HW3\DSC_0462.jpg')

B_1 = im1[:,:,2]
B_2 = im2[:,:,2]
B_3 = im3[:,:,2]
B = np.stack((B_1,B_2,B_3))

All = np.stack((im1,im2,im3,im4,im5))

mean = np.mean(All,axis = 0)
median = np.median(All,axis = 0)

plt.imshow(mean.astype(int))
plt.axis("off")
plt.savefig("Mean",dpi=300)
plt.show()

plt.imshow(median.astype(int))
plt.axis("off")
plt.savefig("Median",dpi=300)
plt.show()
