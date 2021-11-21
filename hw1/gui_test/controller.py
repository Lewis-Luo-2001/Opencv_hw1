from PyQt5 import QtWidgets, QtGui, QtCore

from tutorialUi import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.pushButton.setText("click me!")
        self.clickedCounter = 0
        self.ui.pushButton.clicked.connect(self.buttonClicked)


    def buttonClicked(self):
        self.clickedCounter += 1
        print(self.clickedCounter)