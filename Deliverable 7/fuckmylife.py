from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt
from PyQt4 import QtGui

import Leap
import sys
import pickle

from mpl_toolkits.mplot3d import Axes3D
import matplotlib 
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
#from matplotlib.backends.backend_qt4agg import (
#    FigureCanvasQTAgg as FigureCanvas,
#    NavigationToolbar2QT as NavigationToolbar)
#from matplotlib.backends import qt4_compat
#from matplotlib.backends import qt4_compat
#use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE
#
#if use_pyside:
#    from PySide.QtCore import *
#    from PySide.QtGui import *
#else:
#    from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import sklearn 
from sklearn import datasets
#import PlotCanvas
from scipy.stats import mode
#import collections
#from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
#from matplotlib.figure import Figure
from PyQt4.uic import loadUiType
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
Ui_MainWindow, QMainWindow = loadUiType("C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/QtASL/window.ui")

class QtPyApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self, sampleinterval=.01, timewindow=10.):
        self._interval = int(sampleinterval*1000)
        super(QtPyApp, self).__init__()
        self.setupUi(self)
        
        self.fig = Figure((10,8))
        
        self.axes = self.fig.add_subplot(111,projection='3d')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.mplwindow)
        print type(self.mplvl)
        self.plotLayout = QGridLayout()
        self.plotLayout.addWidget(self.canvas)
        self.mplwindow.setLayout(self.plotLayout)
        #self.layout = QtGui.QVBoxLayout()
        #self.layout.QtGui.addWidget(self.canvas)
        #self.mplvl.addWidget(self.canvas)
        #self.canvas.setParent(self.mplwindow)
        self.canvas.draw()  
        
        #self.fig = Figure((10,8))
        #self.canvas = FigureCanvas(self.fig)
        #self.canvas.setParent(self.w_pane)
        #self.canvas.setFocusPolicy(Qt.StrongFocus)
        #self.canvas.setFocus()      
        #
## Always start by initializing Qt (only once per application)        
        #self.app = QApplication(sys.argv)
        #self.setQuitOnLastWindowClosed(False)
        
## Define a top-level widget to hold everything
        #self.w_pane = centralWidget()
#        #self.w_pane.setGeometry(300,300,1200,700)
#
### Create some widgets to be placed inside
#        self.w_pane.setWindowTitle('ASL Learner')
#        self.left_box = QWidget(self.w_pane)
#        self.label_pic = QLabel(self.left_box)
#        #self.listwidget = QListWidget()
#        #self.listwidget.maximumSize(50,100)
#        self.left_frame = QFrame(self.w_pane)
#        #self.left_frame.setMinimumWidth(50)
#        #self.left_frame.setMaximumWidth(100)
#        self.label = QLabel(self.w_pane)

        
## Create a grid layout to manage the widgets size and position
        #self.layout = QGridLayout()
        #self.layout_box = QVBoxLayout()
        #self.layout.setColumnMaxWidth(0, 50)
        #
## Set pics
        #self.hand_over = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/leaphoverbest.png")
        #self.hand_over = self.hand_over.scaledToHeight(400)
        #self.thumbs_up = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/thumbsup.png")
        #self.thumbs_up = self.thumbs_up.scaledToHeight(200)      
        #self.label.setPixmap(self.hand_over)
        #self.hand_color = 'r'
        
## Add widgets to the layout in their proper positions
        #self.layout_box.addWidget(self.label_pic)
        #self.layout.addWidget(self.left_box, 1, 0, 1,1)  # list widget goes in bottom-left
        #self.layout.addWidget(self.canvas, 0, 1, 5, 20)  # plot goes on right side, spanning 3 rows
        #self.layout.addWidget(self.label, 0, 1, 5, 20)  # plot goes on right side, spanning 3 rows
        #self.layout.addWidget(self.label,0,0) 
        
## Display the widget as a new window
        #self.w_pane.setLayout(self.layout)
        #self.left_box.setLayout(self.layout_box)
        #self.left_box.show()   
        #self.w_pane.show()
        
        #Initialize Leap 
        self.controller = Leap.Controller()
        self.clf = pickle.load(open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','r'))
        self.predictedNumArray = []
        
        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self._interval)
        self.lines = []
        self.on_draw()
        #
        #self.predictionDeque = collections.deque(30*[0], 30)
#Load clf pickle file
        #clf = pickle.load(open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','r'))


    def changeProgramState(self,state):
        if state ==0:
            self.label.setPixmap(self.hand_over)
            
        elif state ==1:
            self.label.setPixmap(self.thumbs_up)
            
        elif state == 2:
            self.hand_color = 'g'
                    
    
    def on_draw(self):
        self.fig.clear()

        
        self.axes.set_xlim(-500,500)
        self.axes.set_ylim(0,500)
        self.axes.set_zlim(0,500)
        #self.fig.axes.get_xaxis().set_ticks([])
        #self.fig.axes.get_yaxis().set_ticks([])
        #self.fig.axes.get_zaxis().set_ticks([])
        #self.axes.plot(self.x, self.y, 'ro')
        #self.axes.imshow(self.data, interpolation='nearest')
        #self.axes.plot([1,2,3])
        self.axes.view_init(azim=90)
        self.canvas.draw()
        
    def CenterData(testData):
        print "centering"
        allXCoordinates = testData[0,::3]
        meanValue = allXCoordinates.mean()
        testData[0,::3] = allXCoordinates - meanValue
    
        
        allYCoordinates = testData[0,1::3]
        meanValue = allYCoordinates.mean()
        testData[0,1::3] = allYCoordinates - meanValue
    
        
        allZCoordinates = testData[0,2::3]
        meanValue = allZCoordinates.mean()
        testData[0,2::3] = allZCoordinates - meanValue
    
        return(testData)
        
        self.changeProgramState(0)
        
    def updateplot(self):
        frame = self.controller.frame()
        
        #frame_center = frame.interaction_box.center
        #
        #if frame.hands.is_empty:
        #    self.changeProgramState(0)
            
        if not frame.hands.is_empty:
            self.changeProgramState(1)
            
            k = 0
            testData = np.zeros((1,30),dtype='f')
            
            while (len(self.lines) > 0): #
                ln = self.lines.pop()
                ln.pop(0).remove()
                del ln
                ln = []
            #self.w_pane.clear()
                
            hand = frame.hands[0]
            fingers = hand.fingers 
            
            hand_center = hand.palm_position
            hand_x = hand_center[0]
            hand_z = hand_center[2]
            print hand_x, hand_z
            
            if abs(hand_x) < 30 and abs(hand_z) <30:
                self.changeProgramState(2)
                
            else:
                self.hand_color = 'r'
                
            for i in range(0,5):
                finger = fingers[i]
                            
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
                        
                    if ((j==0) or (j==3)):
                        testData[0,k] = xTip
                        testData[0,k+1] = yTip
                        testData[0,k+2] = zTip
                        k = k + 3
                        
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
                    
                    predictedNum = self.clf.predict(testData)
                    #self.predictionDeque.append(predictedNum)
                    #print predictedNum
                #    self.predictedNumArray.append(int(predictedNum))
                #    #print mode(self.predictedNumArray)
                #    numpred = len(self.predictedNumArray)
                #    if numpred >= 20:
                #        self.predictedNumArray = self.predictedNumArray[-20:]
                #        
                #    #print self.predictedNumArray
                ##for i in range(20):
                ##    self.predictedNumArray.append(predictedNum)
                ##    print "got to here"
                ##    if len(self.predictedNumArray) > 20:
                ##        self.predictedNumArray[:] = []
                ##
                #    print mode(self.predictedNumArray)
                    
                    
                    #print mode(predictionDeque)
                        

                    
                    self.lines.append(self.axes.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],self.hand_color))
            
            self.canvas.draw()
            
            
                                        
                        
                            
                        
                      
                    #self.predictionDeque.append(predictedNum)
                    #print predictedNum
                #    self.predictedNumArray.append(int(predictedNum))
                #    #print mode(self.predictedNumArray)
                #    numpred = len(self.predictedNumArray)
                #    if numpred >= 20:
                #        self.predictedNumArray = self.predictedNumArray[-20:]
                #        
                #    #print self.predictedNumArray
                ##for i in range(20):
                ##    self.predictedNumArray.append(predictedNum)
                ##    print "got to here"
                ##    if len(self.predictedNumArray) > 20:
                ##        self.predictedNumArray[:] = []
                ##
                #    print mode(self.predictedNumArray)
                    
                    
                    #print mode(predictionDeque)
        
    def run(self):
        self.app.exec_()
        
if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    from PyQt4.QtGui import QApplication
    app = QtGui.QApplication(sys.argv)
    main = QtPyApp(sampleinterval=.1, timewindow=10)
    main.show()
    #main.run()
    sys.exit(app.exec_())