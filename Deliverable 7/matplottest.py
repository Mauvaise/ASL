import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import Leap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
import numpy as np
import pygame
from pygame.locals import *
#matplotlib.use("Agg")
matplotlib.pyplot.ion()

#fig = plt.figure( figsize=(8,6) )
fig = pylab.figure(figsize=[7, 5], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
ax = fig.add_subplot ( 111, projection='3d' )
#plt.draw()
controller = Leap.Controller()
#ax.plot([1, 2, 4])
 
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
 
pygame.init()
 
window = pygame.display.set_mode((900, 700), DOUBLEBUF)
screen = pygame.display.get_surface()
 
size = canvas.get_width_height()
 
surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()
 
while True:
    pass