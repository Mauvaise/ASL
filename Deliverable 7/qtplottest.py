import Leap
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import pickle

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np

class Qt3DPlotter():
    
    def __init__(self, sampleinterval=0.1, timewindow=10.):
        self._interval = int(sampleinterval*1000)
        
        self.app = QtGui.QApplication([])
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 100
        self.w.show()
        self.w.setWindowTitle('pyqtgraph Test')
        self.g = gl.GLGridItem()
        self.w.addItem(self.g)
        
        self.controller = Leap.Controller()
        self.clf = pickle.load(open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','r'))
        
        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self._interval)
        
    def updateplot(self):
        lines = []
        frame = self.controller.frame()
        pos = np.empty((2, 3))
        if not frame.hands.is_empty:
            k = 0
            testData = np.zeros((1,30),dtype='f')
            self.w.clear()
                
            hand = frame.hands[0]
            fingers = hand.fingers 
                
            for i in range(0,5):
                finger = fingers[i]
                            
                for j in range(0,4):
                    bone = finger.bone(j)
                    tip = bone.next_joint
                    base = bone.prev_joint
                    xTip = tip[0]
                    yTip = tip[1]
                    zTip = tip[2]
                        
                    if ((j==0) or (j==3)):
                        testData[0,k] = xTip
                        testData[0,k+1] = yTip
                        testData[0,k+2] = zTip
                        k = k + 3
                        
                    predictedClass = self.clf.predict(testData)
                    #print predictedClass
                    
                    pos[0] = (-tip[0],tip[1],tip[2])
                    pos[1] = (-base[0],base[1],base[2])
                    tipPlot = gl.GLScatterPlotItem(pos=pos, size=1.0, color=[0.5,0.5,0.5,1.0], pxMode=False)
                    tipPlot.translate(5,5,5,local=True)
                    print tipPlot.pos
                    self.w.addItem(tipPlot)
        
    def run(self):
        self.app.exec_()
        
if __name__ == '__main__':
    plotter = Qt3DPlotter(sampleinterval=0.00001, timewindow=10.)
    plotter.run()