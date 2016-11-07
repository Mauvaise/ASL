import sys
from PyQt4.QtCore import*
from PyQt4.QtGui import *

app = QApplication(sys.argv)
win = QWidget()
label = QLabel()
label.setPixmap(QPixmap("C:/Users/Tetris/Desktop/HCI 2016/images/handhoverleap.jpg"))

vbox = QVBoxLayout()
vbox.addWidget(label)
win.setLayout(vbox)
win.setWindowTitle("QPixmap Demo")
win.show()
app.exec_()
	
