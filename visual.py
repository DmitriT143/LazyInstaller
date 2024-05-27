import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(object):
    def __init__(self):
        super(Window, self).__init__()
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("CentralWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.InputWidget = QtWidgets.QWidget(self.centralwidget)
        self.InputWidget.setObjectName("InputWidget")

        self.InputLayout = QtWidgets.QGridLayout(self.InputWidget)
        self.InputLayout.setObjectName("InputLayout")



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Window
ui.__init__()
MainWindow.show()
sys.exit(app.exec_())
