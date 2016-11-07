from PyQt4.QtGui import *  # (the example applies equally well to PySide)
import pyqtgraph as pg
import os
import sys
import Leap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import pickle
import numpy as np
import sklearn 
from sklearn import datasets

## Always start by initializing Qt (only once per application)
app = QApplication(sys.argv)

matplotlib.interactive(True)
#fig = plt.figure( figsize=(8,6) )
#ax = fig.add_subplot ( 111, projection='3d' )
controller = Leap.Controller()

## Define a top-level widget to hold everything
w_pane = QWidget()

## Create some widgets to be placed inside
#btn = QPushButton('press me')
#text = QLineEdit('enter text')
listwidget = QListWidget()
plot = pg.PlotWidget() 
label = QLabel(w_pane)
hand_over = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/leaphoverbest.png")
hand_over = hand_over.scaledToHeight(300)
thumbs_up = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/thumbsup.png")
thumbs_up = thumbs_up.scaledToHeight(300)



#Functions for program states
def programState(state):
    if state ==0:
        label.setPixmap(hand_over)
    elif state ==1:
        label.setPixmap(thumbs_up)


while True:
    frame = controller.frame() # Leap frame
    print "fuck you dolphin"
        
    if frame.hands.is_empty:
        programState(0)
        
    elif not frame.hands.is_empty:
        programState(1)

#w_pane.resize(hand_over.width(),hand_over.height())


## Create a grid layout to manage the widgets size and position
layout = QGridLayout()
w_pane.setLayout(layout)

## Add widgets to the layout in their proper positions
#layout.addWidget(btn, 0, 0)   # button goes in upper-left
#layout.addWidget(text, 1, 0)   # text edit goes in middle-left
layout.addWidget(listwidget, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows
layout.addWidget(label,0,0)
## Display the widget as a new window
w_pane.show()
## Start the Qt event loop
app.exec_()