# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1253, 600)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 411, 241))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/input_red_hist.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 30, 411, 241))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/input_green_hist.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 30, 411, 241))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/input_blue_hist.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(530, 570, 191, 20))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setObjectName("label_13")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 411, 241))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/output_red_hist.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 320, 411, 241))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/output_green_hist.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(830, 320, 411, 241))
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("result_pic/HE_to_RGB/output_blue_hist.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(540, 270, 191, 20))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RGB histogram"))
        self.label_13.setText(_translate("MainWindow", "Output rgb histogram"))
        self.label_15.setText(_translate("MainWindow", "Input rgb histogram"))

