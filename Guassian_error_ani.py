'''
Code origin: https://ndres.me/post/matplotlib-animated-gifs-easily/
Editor: julius52700
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import imageio

#Set some parameter for the Gaussian function
A,mu,sigma = 10,5,0.5

#Define function to generate the data
def plot_for_offset(n, y_max):
      
    for i in range(0,n):
        y = A*np.exp(-(x-mu)**2/2/sigma**2) 
        dy = np.random.normal(1,1,100)
        y += dy
        y_1 = y_1 + y
    
    s = y_1/n

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(x, s)
    ax.set(xlabel='Offset', ylabel='intensity',
           title='Numbers of image stacked: {}'.format(n))

    # IMPORTANT ANIMATION CODE HERE
    # Used to keep the limits constant
    ax.set_ylim(0, y_max)

    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image

#Draw the animation
kwargs_write = {'fps':24.0, 'quantizer':'nq'}
imageio.mimsave('./stacking.gif', [plot_for_offset(i, 20) for i in range(120)], fps=20)
