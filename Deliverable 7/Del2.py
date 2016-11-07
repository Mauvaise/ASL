import Leap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import pickle
import numpy as np
matplotlib.interactive(True)
fig = plt.figure( figsize=(8,6) )
ax = fig.add_subplot ( 111, projection='3d' )
plt.draw()
controller = Leap.Controller()
clf = pickle.load(open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','r'))
lines = []
xMin = -1000
xMax = 1000
yMin = 0
yMax = 1000
zMin = 0
zMax = 1000
#
#def CenterData(testData):
#    allXCoordinates = testData[0,::3]
#    meanValue = allXCoordinates.mean()
#    testData[0,::3] = allXCoordinates - meanValue
#
#    
#    allYCoordinates = testData[0,1::3]
#    meanValue = allYCoordinates.mean()
#    testData[0,1::3] = allYCoordinates - meanValue
#
#    
#    allZCoordinates = testData[0,2::3]
#    meanValue = allZCoordinates.mean()
#    testData[0,2::3] = allZCoordinates - meanValue
#
#    
#    return(testData)


while True:
    frame = controller.frame()
    if not frame.hands.is_empty:
        k = 0
        testData = np.zeros((1,30),dtype='f')
        while (len(lines) > 0):
            ln = lines.pop()
            ln.pop(0).remove()
            del ln
            ln = []
            
        hand = frame.hands[0]
        fingers = hand.fingers
        
        for i in range(0,5):
            finger = fingers[i]
            ax.set_xlim(xMin,xMax)
            ax.set_ylim(yMin,yMax)
            ax.set_zlim(zMin,zMax)
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