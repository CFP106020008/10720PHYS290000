# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:30:32 2019

@author: Julius 本機
"""

import numpy as np
import matplotlib.pyplot as plt 
import astropy.io.fits as fits

#%%

'''Open an image'''
image = fits.getdata('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/20181130_M1-001R300.fits')

#%%

'''View an image'''
plt.imshow(image)
plt.colorbar()
plt.show()

#%%

'''View Header'''
header = fits.getheader('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/20181130_M1-001R300.fits')
print(repr(header))

#%%

'''image Process'''

#Loading datas
image = fits.getdata('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/20181130_M1-001R300.fits')
bias = fits.getdata('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/20181130-001Bias.fits')
dark = fits.getdata('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/20181130_dark-001d300.fits')
flat = fits.getdata('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/20181201-001R5s.fits')

#%%

#Showing everything
plt.imshow(image)
plt.show()
plt.imshow(bias)
plt.show()
plt.imshow(dark)
plt.show()
plt.imshow(flat)
plt.show()

#%%

#Process and show the result
image_processed = ((image-bias)-(dark-bias))/((flat-bias)-(dark-bias)*5/300)*np.mean((flat-bias)-(dark-bias)*5/300)
plt.imshow(image_processed)
plt.colorbar()
plt.show()

#%%

'''Analyzing the image'''

image = image_processed

print('Size of the image: '+ str(image.shape)) #圖片大小
print('Mean Value: '+ str(np.mean(image))) #圖片平均亮度
print('Median Value: '+ str(np.median(image))) #圖片亮度中位數
print('Maximum Value: '+ str(np.max(image))) #圖片最大亮度
print('Min Value: '+ str(np.min(image))) #圖片最小亮度
print('Standard Deviation: ' + str(np.std(image))) #圖片標準差

#%%

#Plotting histogram
plt.hist(np.ndarray.flatten(image),bins = 100,range = (850,1500))
plt.show()

#%%

'''Saving image'''
fits.writeto('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/M1_Processed.fits', image, overwrite = True)

#%%

plt.imshow(image)
plt.colorbar()
plt.savefig('C:/Users/林彥興/OneDrive/大學/課程/計算物理概論/Easy/M1_Processed.tiff')
