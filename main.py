from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
import sys
#import math mod
from functools import partial

#import pyside
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import *

#import gui file
from ui_interface import *


shadow_elements = {
    "left_menu_widget",
    "frame_6",
    "frame_4",
    "header_frame",
    "frame_8"
}
class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #set window minimum size 
        self.setMinimumSize(850, 600)
        #show window
        self.show()

#execute app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())