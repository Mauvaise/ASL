import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
from pylab import *
from drawnow import drawnow, figure
 
fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()

def draw_hand():
    

ax.plot([1, 2, 4])
 
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
 

 
pygame.init()
 
window = pygame.display.set_mode((600, 400), DOUBLEBUF)
screen = pygame.display.get_surface()
 
size = canvas.get_width_height()
 
surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()
 
while True:
    pass