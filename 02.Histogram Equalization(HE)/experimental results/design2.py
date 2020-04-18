# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 244, 244))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/output_img.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 244, 244))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../my_cat(RGB_low_contrast).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 310, 411, 241))
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/output_RGB_hist.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(270, 10, 411, 241))
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/input_RGB_hist.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 560, 221, 31))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Histogram Equalization(RGB)_Result"))
        self.label_2.setText(_translate("MainWindow", "Input color image"))
        self.label_3.setText(_translate("MainWindow", "Output color image"))

