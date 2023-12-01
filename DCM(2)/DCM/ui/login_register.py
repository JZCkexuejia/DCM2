# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginRegister(object):
    def setupUi(self, LoginRegister):
        LoginRegister.setObjectName("LoginRegister")
        LoginRegister.resize(1091, 505)
        self.centralwidget = QtWidgets.QWidget(LoginRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:white\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color:rgb(42, 42, 42)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("background:rgb(255, 255, 255)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem2)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color:white;\n"
"border-radius:20px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("background:transparent;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_login_register = QtWidgets.QLabel(self.frame_7)
        self.label_login_register.setStyleSheet("color:rgb(85, 170, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_login_register.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_register.setObjectName("label_login_register")
        self.verticalLayout_6.addWidget(self.label_login_register)
        self.label_login_register_detail = QtWidgets.QLabel(self.frame_7)
        self.label_login_register_detail.setStyleSheet("color: rgb(0, 0, 207);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_login_register_detail.setWordWrap(True)
        self.label_login_register_detail.setObjectName("label_login_register_detail")
        self.verticalLayout_6.addWidget(self.label_login_register_detail)
        self.line_3 = QtWidgets.QFrame(self.frame_7)
        self.line_3.setStyleSheet("background-color:rgb(195, 195, 195)")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setStyleSheet("color: rgb(0, 0, 207);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.lineEdit_username = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_username.setStyleSheet("border:2px solid #55aaff;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout_6.addWidget(self.lineEdit_username)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setStyleSheet("color: rgb(0, 0, 207);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_password.setStyleSheet("border:2px solid #55aaff;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_6.addWidget(self.lineEdit_password)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.btn_login_register = QtWidgets.QPushButton(self.frame_10)
        self.btn_login_register.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_login_register.setStyleSheet("background-color:rgb(0, 0, 255);\n"
"padding:10px 20px;\n"
"border:2px solid #55aaff;\n"
"border-radius:10px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.btn_login_register.setObjectName("btn_login_register")
        self.horizontalLayout_3.addWidget(self.btn_login_register)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setStyleSheet("background:transparent;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_2 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setStyleSheet("border:1px solid white;\n"
"background-color:white;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setMinimumSize(QtCore.QSize(0, 10))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet("border:1px solid white;\n"
"background-color:white;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet("background:transparent;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.label_register_login = QtWidgets.QLabel(self.frame_8)
        self.label_register_login.setStyleSheet("color:rgb(85, 170, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.label_register_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_register_login.setObjectName("label_register_login")
        self.verticalLayout_5.addWidget(self.label_register_login)
        self.label_register_login_detail = QtWidgets.QLabel(self.frame_8)
        self.label_register_login_detail.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_register_login_detail.setWordWrap(True)
        self.label_register_login_detail.setObjectName("label_register_login_detail")
        self.verticalLayout_5.addWidget(self.label_register_login_detail)
        self.line_4 = QtWidgets.QFrame(self.frame_8)
        self.line_4.setStyleSheet("background-color:rgb(195, 195, 195)")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem8)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.btn_register_login = QtWidgets.QPushButton(self.frame_11)
        self.btn_register_login.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_register_login.setStyleSheet("background-color:rgb(85, 85, 0);\n"
"padding:10px 20px;\n"
"border:2px solid #55aaff;\n"
"border-radius:10px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.btn_register_login.setObjectName("btn_register_login")
        self.horizontalLayout_4.addWidget(self.btn_register_login)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_5.addWidget(self.frame_11)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_7.addWidget(self.frame_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem12)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setStyleSheet("background:white")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(20, 279, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        LoginRegister.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginRegister)
        QtCore.QMetaObject.connectSlotsByName(LoginRegister)

    def retranslateUi(self, LoginRegister):
        _translate = QtCore.QCoreApplication.translate
        LoginRegister.setWindowTitle(_translate("LoginRegister", "Pacemaker: Device Controller Monitor"))
        self.label.setText(_translate("LoginRegister", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">Device Controller Monitor</span></p></body></html>"))
        self.label_login_register.setText(_translate("LoginRegister", "LOGIN"))
        self.label_login_register_detail.setText(_translate("LoginRegister", "Please enter your credentials for login"))
        self.label_3.setText(_translate("LoginRegister", "Username"))
        self.label_6.setText(_translate("LoginRegister", "Password"))
        self.btn_login_register.setText(_translate("LoginRegister", "Login"))
        self.label_5.setText(_translate("LoginRegister", "OR"))
        self.label_register_login.setText(_translate("LoginRegister", "REGISTER"))
        self.label_register_login_detail.setText(_translate("LoginRegister", "Don\'t have an account? Please register here."))
        self.btn_register_login.setText(_translate("LoginRegister", "Register"))
