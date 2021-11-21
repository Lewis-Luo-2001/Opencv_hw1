from PyQt5 import QtWidgets, QtGui, QtCore
from HW1_menu_ui import Ui_MainWindow
import numpy as np
import cv2
import copy

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        # self.subWindow = Widget1_1_1()

    def setup_control(self):
        #------------ Q1 ------------#
        self.ui.pushButton_q1_1.clicked.connect(self.buttonClicked_1_1)
        self.ui.pushButton_q1_2.clicked.connect(self.buttonClicked_1_2)
        self.ui.pushButton_q1_3.clicked.connect(self.buttonClicked_1_3)
        self.ui.pushButton_q1_4.clicked.connect(self.buttonClicked_1_4)

        #------------ Q2 ------------#
        self.ui.pushButton_q2_1.clicked.connect(self.buttonClicked_2_1)
        self.ui.pushButton_q2_2.clicked.connect(self.buttonClicked_2_2)
        self.ui.pushButton_q2_3.clicked.connect(self.buttonClicked_2_3)

        #------------ Q3 ------------#
        self.ui.pushButton_q3_1.clicked.connect(self.buttonClicked_3_1)
        self.ui.pushButton_q3_2.clicked.connect(self.buttonClicked_3_2)
        self.ui.pushButton_q3_3.clicked.connect(self.buttonClicked_3_3)
        self.ui.pushButton_q3_4.clicked.connect(self.buttonClicked_3_4)

        #------------ Q4 ------------#
        self.ui.pushButton_q4_1.clicked.connect(self.buttonClicked_4_1)
        self.ui.pushButton_q4_2.clicked.connect(self.buttonClicked_4_2)
        self.ui.pushButton_q4_3.clicked.connect(self.buttonClicked_4_3)
        self.ui.pushButton_q4_4.clicked.connect(self.buttonClicked_4_4)


    #------------ Q1 ------------#
    def buttonClicked_1_1(self):
        img = cv2.imread('..\src\Q1_image\Sun.jpg')
        height, width, channel = img.shape
        cv2.imshow("1.1 Load Image", img)
        print("Height :  ", height)
        print("Width :  ", width)

    def buttonClicked_1_2(self):
        img = cv2.imread('..\src\Q1_image\Sun.jpg')
        height, width, channel = img.shape
        zeros = np.zeros(img.shape[:2], dtype="uint8")
        B, G, R = cv2.split(img)
        cv2.imshow("1.2 Color Seperation B channel", cv2.merge([B, zeros, zeros]))
        cv2.imshow("1.2 Color Seperation G channel", cv2.merge([zeros, G, zeros]))
        cv2.imshow("1.2 Color Seperation R channel", cv2.merge([zeros, zeros, R]))
    
    def buttonClicked_1_3(self):
        img = cv2.imread('..\src\Q1_image\Sun.jpg')
        height, width, channel = img.shape
        B, G, R = cv2.split(img)
        
        img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("1.3 Color Transformation OpenCV function", img_1)

        img_2 = (B/3+G/3+R/3).astype(np.uint8)
        cv2.imshow("1.3 Color Transformation Average Weighted", img_2)
    
    def buttonClicked_1_4(self):
        def update(x):
            alpha = x/255
            beta = 1.0 - alpha
            rst = cv2.addWeighted(img_1, beta, img_2, alpha, 0.0)
            cv2.imshow("1.4 Blending", rst)

        img_1 = cv2.imread("..\src\Q1_image\Dog_Strong.jpg")
        img_2 = cv2.imread("..\src\Q1_image\Dog_Weak.jpg")
        alpha = 0
        beta = 1.0 - alpha

        rst = cv2.addWeighted(img_1, beta, img_2, alpha, 0.0)
        cv2.imshow("1.4 Blending", rst)

        cv2.createTrackbar("Blend", "1.4 Blending", 0, 255, update)


    #------------ Q2 ------------#
    def buttonClicked_2_1(self):
        img = cv2.imread('..\src\Q2_image\Lenna_whiteNoise.jpg')
        blur = cv2.GaussianBlur(img,(5,5),0)
        cv2.imshow("2.1 Gaussian Blur before", img)
        cv2.imshow("2.1 Gaussian Blur after", blur)
    
    def buttonClicked_2_2(self):
        img = cv2.imread('..\src\Q2_image\Lenna_whiteNoise.jpg')
        BF = cv2.bilateralFilter(img, 9, 90, 90)
        cv2.imshow("2.2 Bilateral Filter before", img)
        cv2.imshow("2.2 Bilateral Filter after", BF)
    
    def buttonClicked_2_3(self):
        img = cv2.imread('..\src\Q2_image\Lenna_pepperSalt.jpg')
        MF_3 = cv2.medianBlur(img, 3)
        MF_5 = cv2.medianBlur(img, 5)
        cv2.imshow("2.3 Median Filter before", img)
        cv2.imshow("2.3 Median Filter 3x3", MF_3)
        cv2.imshow("2.3 Median Filter 5x5", MF_5)


    #------------ Q3 ------------#
    def buttonClicked_3_1(self):
        img = cv2.imread('..\src\Q3_image\House.jpg')
        B, G, R = cv2.split(img)
        height, width, channel = img.shape

        img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        GaussianFilter = [[0.045, 0.122, 0.015], [0.122, 0.332, 0.122], [0.045, 0.122, 0.045]]
        m = 3
        img_gaussian = copy.copy(img_grayscale)
        for i in range(1, height-1):
            for j in range(1, width-1):
                img_gaussian[i][j] = np.sum(img_grayscale[i-1:i-1+m, j-1:j-1+m] * GaussianFilter) 

        cv2.imshow("3.1 Gaussian Blur before ", img)
        cv2.imshow("3.1 Gaussian Blur grayscale ", img_grayscale)
        cv2.imshow("3.1 Gaussian Blur after ", img_gaussian)
    
    def buttonClicked_3_2(self):
        img = cv2.imread('..\src\Q3_image\House.jpg')
        B, G, R = cv2.split(img)
        height, width, channel = img.shape

        img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        GaussianFilter = [[0.045, 0.122, 0.015], [0.122, 0.332, 0.122], [0.045, 0.122, 0.045]]
        m = 3
        img_gaussian = copy.copy(img_grayscale)
        for i in range(1, height-1):
            for j in range(1, width-1):
                img_gaussian[i][j] = np.sum(img_grayscale[i-1:i-1+m, j-1:j-1+m] * GaussianFilter) 

        SobelXFilter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        m = 3
        img_sobelX = copy.copy(img_gaussian)
        for i in range(1, height-1):
            for j in range(1, width-1):
                tempValue = abs(np.sum(img_gaussian[i-1:i-1+m, j-1:j-1+m] * SobelXFilter))
                if tempValue > 255 :
                    img_sobelX[i][j] = 255
                else :
                    img_sobelX[i][j] = tempValue

        cv2.imshow("3.2 Sobel X before ", img_gaussian)
        cv2.imshow("3.2 Sobel X after ", img_sobelX)
    
    def buttonClicked_3_3(self):
        img = cv2.imread('..\src\Q3_image\House.jpg')
        B, G, R = cv2.split(img)
        height, width, channel = img.shape

        img_grayscale = (B/3+G/3+R/3).astype(np.uint8)

        GaussianFilter = [[0.045, 0.122, 0.015], [0.122, 0.332, 0.122], [0.045, 0.122, 0.045]]
        m = 3
        img_gaussian = copy.copy(img_grayscale)
        for i in range(1, height-1):
            for j in range(1, width-1):
                img_gaussian[i][j] = np.sum(img_grayscale[i-1:i-1+m, j-1:j-1+m] * GaussianFilter) 

        SobelYFilter = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
        m = 3
        img_sobelY = copy.copy(img_gaussian)
        for i in range(1, height-1):
            for j in range(1, width-1):
                tempValue = abs(np.sum(img_gaussian[i-1:i-1+m, j-1:j-1+m] * SobelYFilter))
                if tempValue > 255 :
                    img_sobelY[i][j] = 255
                else :
                    img_sobelY[i][j] = tempValue

        cv2.imshow("3.3 Sobel Y before ", img_gaussian)
        cv2.imshow("3.3 Sobel Y after ", img_sobelY)
        
    def buttonClicked_3_4(self):
        img = cv2.imread('..\src\Q3_image\House.jpg')
        B, G, R = cv2.split(img)
        height, width, channel = img.shape

        img_grayscale = (B/3+G/3+R/3).astype(np.uint8)

        GaussianFilter = [[0.045, 0.122, 0.015], [0.122, 0.332, 0.122], [0.045, 0.122, 0.045]]
        m = 3
        img_gaussian = copy.copy(img_grayscale)
        for i in range(1, height-1):
            for j in range(1, width-1):
                img_gaussian[i][j] = np.sum(img_grayscale[i-1:i-1+m, j-1:j-1+m] * GaussianFilter) 

        SobelXFilter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        SobelYFilter = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
        m = 3
        img_magnitude = copy.copy(img_gaussian)
        for i in range(1, height-1):
            for j in range(1, width-1):
                sobelX = abs(np.sum(img_gaussian[i-1:i-1+m, j-1:j-1+m] * SobelXFilter))
                if sobelX > 255 :
                    sobelX = 255

                sobelY = abs(np.sum(img_gaussian[i-1:i-1+m, j-1:j-1+m] * SobelYFilter))
                if sobelY > 255 :
                    sobelY = 255

                img_magnitude[i][j] = (sobelX ** 2 + sobelY ** 2) ** 0.5 * 255 / 361

        cv2.imshow("3.4 Magnitude", img_magnitude)



    #------------ Q3 ------------#
    def buttonClicked_4_1(self):
        pass
    def buttonClicked_4_2(self):
        pass
    def buttonClicked_4_3(self):
        pass
    def buttonClicked_4_4(self):
        pass