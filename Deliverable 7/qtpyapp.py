from PyQt4.QtGui import *  # (the example applies equally well to PySide)
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication
from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph.Qt import QtCore, QtGui
import Leap
import pyqtgraph as pg
import sys
import pickle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib 
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat
use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE

if use_pyside:
    from PySide.QtCore import *
    from PySide.QtGui import *
else:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
import numpy as np
import sklearn 
from sklearn import datasets
import PlotCanvas
from scipy.stats import mode
#import collections
import time
from random import randint


class QtPyApp():
    
    def __init__(self, sampleinterval=.001, timewindow=10.):
        self.interval = int(sampleinterval*1000)

        
## initializes Qt (only once per application)        
        #self.app = QApplication(sys.argv)

        
## Define a top-level widget to hold everything
        self.w_pane = QWidget()
        self.w_pane.setGeometry(300,300,1200,700)

## Login widget to check to database       
        #self.login = Login()
        #self.login.setGeometry(500,500,300,300)
        #self.login.show()
             

## Create some widgets to be placed inside
        self.w_pane.setWindowTitle('ASL Learner')
        #self.left_box = QWidget(self.w_pane)
        self.center_label = QLabel()
        self.center_arrow = QLabel()
        self.right_label = QLabel()
        self.left_label = QLabel()
        self.signs_label = QLabel()
        #self.listwidget = QListWidget()
        self.fig = Figure((8,6), facecolor='#AAB7B8')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.w_pane)
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()

        
## Bedazzling
        self.w_pane.setAutoFillBackground(True)
        self.palette = self.w_pane.palette()
        self.palette.setColor(self.w_pane.backgroundRole(), Qt.black)
        self.w_pane.setPalette(self.palette)
       
        
## Create a grid layout to manage the widgets size and position
        self.layout = QGridLayout()

## Set pics
        self.hand_over = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/leaphoverbest.png")
        self.hand_over = self.hand_over.scaledToHeight(600)
        
        self.thumbs_up = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/thumbsup.png")
        self.thumbs_up = self.thumbs_up.scaledToHeight(180)
        
        self.red_arrow = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/redarrow.png")
        self.red_arrow = self.red_arrow.scaledToHeight(50)
        
        self.check_mark = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/checkmark.png")
        self.check_mark = self.check_mark.scaledToHeight(150)
    
        self.red_mark = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/redmark.png")
        self.red_mark = self.red_mark.scaledToHeight(150)
        
        self.asl_0 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl0withnum.png")
        self.asl_0 = self.asl_0.scaledToHeight(120)
        
        self.asl_1 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl1withnum.png")
        self.asl_1 = self.asl_1.scaledToHeight(120)
        
        self.asl_2 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl2withnum.png")
        self.asl_2 = self.asl_2.scaledToHeight(120)
        
        self.asl_3 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl3withnum.png")
        self.asl_3 = self.asl_3.scaledToHeight(120)
        
        self.asl_4 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl4withnum.png")
        self.asl_4 = self.asl_4.scaledToHeight(120)
        
        self.asl_5 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl5withnum.png")
        self.asl_5 = self.asl_5.scaledToHeight(120)
        
        self.asl_6 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl6withnum.png")
        self.asl_6 = self.asl_6.scaledToHeight(120)
        
        self.asl_7 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl7withnum.png")
        self.asl_7 = self.asl_7.scaledToHeight(120)
        
        self.asl_8 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl8withnum.png")
        self.asl_8 = self.asl_8.scaledToHeight(120)
        
        self.asl_9 = QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/asl9withnum.png")
        self.asl_9 = self.asl_9.scaledToHeight(120)
        
        self.asl_list = [self.asl_0,self.asl_1,self.asl_2,self.asl_3,self.asl_4,self.asl_5,self.asl_6,self.asl_7,self.asl_8,self.asl_9] 
        
        self.program_state = 0
        self.changeProgramState(0)           
        self.centered_count = 0
        self.current_ASL_num = -1
        self.correct_count = 0
        self.predictedNumArray = []
        
## Add widgets to the layout in their proper positions
        self.layout.addWidget(self.canvas, 0, 1, 8, 20)  # plot goes on right side, spanning 3 rows
        self.layout.addWidget(self.right_label, 1,17)  # plot goes on right side, spanning 3 rows
        self.layout.addWidget(self.signs_label, 5,11)  # plot goes on right side, spanning 3 rows
        self.layout.addWidget(self.center_arrow, 1,12)  # plot goes on right side, spanning 3 rows
        self.layout.addWidget(self.center_label, 3,11)  # plot goes on right side, spanning 3 rows
        #self.layout.addWidget(self.left_label, 1,2)  # plot goes on right side, spanning 3 rows
        
## Display the widget as a new window
        self.w_pane.setLayout(self.layout)  
        self.w_pane.show()
        
        #Initialize Leap 
        self.controller = Leap.Controller()

        
        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self.interval)
        self.lines = []
        self.on_draw()
        
        #Load clf pickle file
        self.clf = pickle.load(open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','rb'))


#Changes program states
    def changeProgramState(self,state):
        self.program_state = state
        
        #Hand not present
        if state == 0:
            self.center_arrow.hide()
            self.signs_label.hide()
            self.center_label.show()
            self.center_label.setPixmap(self.hand_over)
            self.hand_color = 'maroon'
        
        #Hand is present but not centered
        elif state == 1:
            self.right_label.hide()
            self.signs_label.hide()
            self.center_label.hide()
            self.center_arrow.show()
            self.center_arrow.setPixmap(self.red_arrow)
           
        #Hand is present and centered 
        elif state == 2:
            self.hand_color = 'g'
            
        #Hand has correctly signed the current number displayed
        elif state == 3:
            self.signs_label.hide()
            #self.signs_label.show()
            self.right_label.show()
            self.right_label(self.thumbs_up)
            self.center_arrow.hide()
                                
#Draws plot   
    def on_draw(self):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111,projection='3d', axis_bgcolor='burlywood') 
        self.axes.axis('off')
        self.axes.set_xlim(-350,350)
        self.axes.set_ylim(0,350)
        self.axes.set_zlim(0,350)
        self.axes.view_init(azim=90)
        self.canvas.draw()
        
    #def centerData(testData):
    #    print "centering"
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
    #    return(testData)

      
#Clears lines       
    def clearHand(self):
        while (len(self.lines) > 0): 
            ln = self.lines.pop()
            ln.pop(0).remove()
            del ln
            ln = []
            
    def setRandoASL(self):
        self.signs_label.show()
        rando_index = randint(0, len(self.asl_list))
        self.right_label.hide()
        self.signs_label.setPixmap(self.asl_list[rando_index])
        self.current_ASL_num = rando_index    
            
    def updateplot(self):
        frame = self.controller.frame()
        self.clearHand()
        
        if frame.hands.is_empty:
            self.changeProgramState(0)
            
        if not frame.hands.is_empty:
            #self.clearHand()
            
            if not self.program_state > 1:
                self.changeProgramState(1)

            k = 0
            testData = np.zeros((1,30),dtype='f')          
            hand = frame.hands[0]
            fingers = hand.fingers       
            hand_center = hand.palm_position
            hand_x = hand_center[0]
            hand_z = hand_center[2]  
                
            #Checks if user's hand is centered
            if abs(hand_x) < 50 and abs(hand_z) < 50:
                self.changeProgramState(2)
                self.centered_count+=1

                if self.centered_count == 10:
                    self.center_arrow.hide()
                    self.right_label.show()
                    self.right_label.setPixmap(self.thumbs_up)
                    vb_timer = QtCore.QTimer()
                    vb_timer.singleShot(2000, self.setRandoASL)                                
                                  
            else:
                self.right_label.hide()
                self.center_arrow.show()
                self.centered_count = 0
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
                                       
                    #testData = self.centerData(testData)     
                    predictedNum = self.clf.predict(testData)
                    print predictedNum
                    
                    #Changes program state to 3 iff the user's sign is correct
                    if int(predictedNum) == self.current_ASL_num:
                        print self.current_ASL_num
                        self.correct_count+=1
                        if self.correct_count == 7:
                            self.changeProgramState(3)
                            self.correct_count = 0
                            vb_timer.singleShot(3000, self.setRandoASL())
                            
                    else:
                        self.correct_count = 0

                    
                    self.lines.append(self.axes.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],self.hand_color, lw = 2, solid_capstyle='round')),
            
        self.canvas.draw()
            
        
    def run(self):
        self.app.exec_()

class Login():
    def __init__(self, parent=None):
        self.app = QApplication(sys.argv)
        self.dialog = QtGui.QDialog()
        #super(Login, self).__init__(parent)
        self.textName = QtGui.QLineEdit()
        self.textPass = QtGui.QLineEdit()
        self.buttonLogin = QtGui.QPushButton('Login')
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.textName)
        #layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.dialog.setLayout(layout)
        self.database = {}
        self.dialog.show()
        
        
    def run(self):
        self.app.exec_()

    def handleLogin(self):
        userName = self.textName.text()
        
        #database = pickle.load( open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/database.p','rb'))
        
        
        #try:
        with open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/database.p', 'rb') as db:
            self.database = db.readlines()
            db.close()        
        #except IOError:
        #    print "File error!"
        #    with open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/database.p','wb') as self.database:
        #        pickle.dump([userName],self.database)
                
        
        
        if self.textName.text() in self.database:
            print 'Welcome back ' + userName + '.'
            
        else: 
            self.database.append(userName)
            print 'Welcome ' + userName + '.' 
        
        pickle.dump(self.database, open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/database.p', 'wb'))
            
        self.dialog.accept()        
        
        app = QtPyApp(sampleinterval= 0.001, timewindow=10.)
        app.run()
        
    
    
    
                     
if __name__ == '__main__':
    loginApp = Login()
    loginApp.run()
    

    
    