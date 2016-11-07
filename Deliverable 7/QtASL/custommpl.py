from PyQt4.uic import loadUiType
 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
Ui_MainWindow, QMainWindow = loadUiType("C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/QtASL/window.ui")


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
 
if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
 
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())