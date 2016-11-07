import numpy as np
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

class Reader:
    def __init__(self):
        self.lines = []
        self.fig = plt.figure( figsize=(8,6) )
        self.ax = self.fig.add_subplot ( 111, projection='3d' )
        self.ax.set_xlim(-400,400)
        self.ax.set_ylim(0,700)
        self.ax.set_zlim(0,1000)
        self.ax.view_init(azim=90) 
        fileName = 'C:/Users/Kalista13/Documents/HCI/Deliverable 1/userData/numOfGestures.dat'
        f = open(fileName,'r')
        self.numberOfGesturesSaved = pickle.load(f)
        f.close()
        plt.draw()
    
    def RunForever(self):
        while True:
            self.PrintData()
            
    def ClearLines(self):
        while (len(self.lines) > 0):
            ln = self.lines.pop()
            ln.pop(0).remove()
            del ln
            ln = []  
              
    def PrintGesture(self,i):
        self.ClearLines()
        fileName ='C:/Users/Kalista13/Documents/HCI/Deliverable 1/userData/gesture{}.dat'.format(i)
        f = open(fileName,'r')
        gestureData = pickle.load(f)
        f.close()
        for i in range(0,5):
            for j in range(0,4):
                xBase = gestureData[i,j,0]
                yBase = gestureData[i,j,1] 
                zBase = gestureData[i,j,2]
                xTip = gestureData[i,j,3] 
                yTip = gestureData[i,j,4] 
                zTip = gestureData[i,j,5] 
                self.lines.append(self.ax.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],'b'))
        plt.pause(0.5)
        plt.draw()
                

    def PrintData(self):
        for i in range(0,int(self.numberOfGesturesSaved)):
            self.PrintGesture(i)
        
reader = Reader()
reader.RunForever()