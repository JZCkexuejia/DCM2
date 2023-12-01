# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(1071, 554)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setStyleSheet("border:1px solid rgb(212, 212, 212)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("color:rgb(255, 219, 241);\n"
"font: 16pt \"MS Sans Serif\";")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setStyleSheet("border:1px solid rgb(212, 212, 212)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.my_progressBar = QtWidgets.QProgressBar(self.frame)
        self.my_progressBar.setStyleSheet("QProgressBar{\n"
"    background-color:rgb(36, 72, 108);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    color:white;\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 10px;\n"
"}")
        self.my_progressBar.setProperty("value", 24)
        self.my_progressBar.setObjectName("my_progressBar")
        self.verticalLayout.addWidget(self.my_progressBar)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../resources/images/splash_img.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_2.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:24pt; color:#55aaff;\">PACEMAKER</span></p><p><span style=\" font-size:24pt; color:#ffffff;\">Device Controller Monitor</span></p></body></html>"))
        self.label_4.setText(_translate("SplashScreen", "A pacemaker is a device that sends small electrical impulses to the heart muscle to maintain a suitable heart rate or to stimulate the lower chambers of the heart (ventricles). A pacemaker may also be used to treat fainting spells (syncope), congestive heart failure and hypertrophic cardiomyopathy."))
        self.label_3.setText(_translate("SplashScreen", "Loading..."))
