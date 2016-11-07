import Leap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import pickle
import numpy as np
import pygame
from pygame.locals import *
import sklearn 
from sklearn import datasets

matplotlib.interactive(True)
fig = plt.figure( figsize=(8,6) )
ax = fig.add_subplot ( 111, projection='3d' )
controller = Leap.Controller()
plt.draw()
clf = pickle.load(open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','r'))
lines = []
xMin = -1000
xMax = 1000
yMin = 0
yMax = 1000
zMin = 0
zMax = 1000
#programState = 0



while True:
    frame = controller.frame() # Leap frame
    if not frame.hands.is_empty: #Leap check for hands
        k = 0
        #programState = 1
        testData = np.zeros((1,30),dtype='f') # Data
        while (len(lines) > 0): #
            ln = lines.pop()
            ln.pop(0).remove()
            del ln
            ln = []
            
        hand = frame.hands[0] # Leap
        fingers = hand.fingers #Leap
        
        for i in range(0,5):
            finger = fingers[i]-500
            ax.view_init(azim=90)
            
            for j in range(0,4):
                bone = finger.bone(j)
                tip = bone.next_joint
                base = bone.prev_joint
                xBase = base[0]
                yBase = base[1]
                zBase = base[2]
                xTip = tip[0]
                yTip = tip[1]
                zTip = tip[2]
                #
                if (xBase < xMin):
                    xMin = xBase
                if (xBase > xMax):
                    xMax = xBase
                if (xTip < xMin):
                    xMin = xTip
                if (xTip > xMax):
                    xMax = xTip
                    
                if (yBase < yMin):
                    yMin = yBase
                if (yBase > yMax):
                    yMax = yBase                        
                if (yTip < yMin):
                    yMin = yTip
                if (yTip > yMax):
                    yMax = yTip
                    
                if (zBase < zMin):
                    zMin = zBase
                if (zBase > zMax):
                    zMax = zBase
                if (zTip < zMin):
                    zMin = zTip
                if (zTip > zMax):
                    zMax = zTip
                    
                if ((j==0) or (j==3)):
                    testData[0,k] = xTip
                    testData[0,k+1] = yTip
                    testData[0,k+2] = zTip
                    k = k + 3
                    
                #print testData
                #testData = CenterData(testData)
                predictedClass = clf.predict(testData)
                print predictedClass
                lines.append(ax.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],'r'))

        plt.draw()
    plt.pause(0.000001)
    pass