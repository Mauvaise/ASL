import Leap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
import pickle

class Deliverable: 
    def __init__(self):
        self.controller = Leap.Controller()
        self.lines = []
        matplotlib.interactive(True)
        self.gestureData = np.zeros((5,4,6),dtype='f')
        self.xMin = -1000
        self.xMax = 1000
        self.yMin = 0
        self.yMax = 1000
        self.zMin = 0
        self.zMax = 1000
        self.fig = plt.figure( figsize=(8,6) )
        self.ax = self.fig.add_subplot ( 111, projection='3d' )
        self.previousNumberOfHands = 0
        self.currentNumberOfHands = 0
        self.numberOfGesturesSaved = 0
        plt.draw()
         
 # Functions that handle the leap logic
    def SaveGesture(self):
        fileName ='C:/Users/Kalista13/Documents/HCI/Deliverable 1/userData/gesture{}.dat'.format(self.numberOfGesturesSaved)
        f = open(fileName,'w')
        pickle.dump(self.gestureData,f)
        f.close()
        self.numberOfGesturesSaved = self.numberOfGesturesSaved + 1
        fileName = 'C:/Users/Kalista13/Documents/HCI/Deliverable 1/userData/numOfGestures.dat'
        f = open(fileName,'w')
        pickle.dump(str(self.numberOfGesturesSaved),f)
        f.close()
        
             
    def HandleHands(self):
        frame = self.controller.frame()       
        if not frame.hands.is_empty:
            self.ClearLines()
            self.previousNumberOfHands = self.currentNumberOfHands
            self.currentNumberOfHands = len(frame.hands) 
            if (self.RecordingIsEnding()):
                print self.gestureData[:,:,:]
                self.SaveGesture()
                        
            self.hand = frame.hands[0]        
            fingers = self.hand.fingers
            for i in range(0,5):
                self.HandleFinger(fingers[i],i)     
    
    def HandleFinger(self, finger, i):
        self.SetAxesLimits()
        for j in range(0,4):
            self.HandleBone(finger.bone(j), i, j)
            
    def HandleBone(self, bone, i, j):          
        tip = bone.next_joint
        base = bone.prev_joint
        self.SetCoords(tip, base, i, j)

# Functions that handle running program
    def RunOnce(self):
        self.HandleHands()                 
        plt.draw()
                    
    def RunForever(self):
        while True:
            self.RunOnce()
            plt.pause(0.0001)
            pass
            
    def RecordingIsEnding(self):
        return (self.previousNumberOfHands==2) & (self.currentNumberOfHands==1)
  
 # Utility functions below       
    def ClearLines(self):
        while (len(self.lines) > 0):
            ln = self.lines.pop()
            ln.pop(0).remove()
            del ln
            ln = []
            
    def SetAxesLimits(self):
        self.ax.set_xlim(self.xMin,self.xMax)
        self.ax.set_ylim(self.yMin,self.yMax)
        self.ax.set_zlim(self.zMin,self.zMax)
        self.ax.view_init(azim=90)      
                 
    def SetCoords(self, tip, base, i, j):
        # Sets x, y, z base and tip coords
        xBase = base[0]
        yBase = base[1]
        zBase = base[2]
        xTip = tip[0]
        yTip = tip[1]
        zTip = tip[2]
        self.gestureData[i,j,0] = xBase
        self.gestureData[i,j,1] = yBase
        self.gestureData[i,j,2] = zBase
        self.gestureData[i,j,3] = xTip
        self.gestureData[i,j,4] = yTip
        self.gestureData[i,j,5] = zTip

        # Reactive limit setting logic for hand placement
        if (xBase < self.xMin):
            self.xMin = xBase
        if (xBase > self.xMax):
            self.xMax = xBase
        if (xTip < self.xMin):
            self.xMin = xTip
        if (xTip > self.xMax):
            self.xMax = xTip          
        if (yBase < self.yMin):
            self.yMin = yBase
        if (yBase > self.yMax):
            self.yMax = yBase                        
        if (yTip < self.yMin):
            self.yMin = yTip
        if (yTip > self.yMax):
            self.yMax = yTip          
        if (zBase < self.zMin):
            self.zMin = zBase
        if (zBase > self.zMax):
            self.zMax = zBase
        if (zTip < self.zMin):
            self.zMin = zTip
        if (zTip > self.zMax):
            self.zMax = zTip    
        # Plots the hand 
        color = 'r'
        if (self.currentNumberOfHands == 1):
            color = 'g'
        
        self.lines.append(self.ax.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],color))
                
deliverable = Deliverable()
deliverable.RunForever()