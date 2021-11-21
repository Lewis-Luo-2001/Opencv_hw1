from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
import cv2

class Widget1_1_1(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(620, 387)
        self.setWindowTitle("1.1 Load Image")

        # Label
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 620, 387)
        self.label.setAlignment(Qt.AlignCenter)
        self.img_path = '..\src\Q1_image\Sun.jpg'
        self.display_img()

    def display_img(self):
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(self.qimg))
        print("Height :  ", width)
        print("Width :  ", height)
