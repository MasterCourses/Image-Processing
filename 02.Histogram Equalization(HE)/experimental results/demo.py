# Display RGB Histogram
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys

from demo_result import Ui_MainWindow

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)  # call init of QMainWindow, or QWidget or whatever)
        self.setupUi(self)  # call the function that actually does all the stuff you set up in QtDesigner

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
