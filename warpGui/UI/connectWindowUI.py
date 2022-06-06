# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnectWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.WARPLabel = None
        self.DashLabel = None
        self.LinuxLabel = None
        self.StatusLabel = None
        self.widget = None
        self.FooterLabel = None
        self.SecondFooterLabel = None
        self.BUGButton = None
        self.YourInternetLabel = None
        self.layoutWidget = None
        self.gridLayout = None
        self.pushButton_start_end = None

    def setupUi(self, ConnectWindow):
        ConnectWindow.setObjectName("ConnectWindow")
        ConnectWindow.resize(390, 439)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectWindow.sizePolicy().hasHeightForWidth())
        ConnectWindow.setSizePolicy(sizePolicy)
        ConnectWindow.setMinimumSize(QtCore.QSize(390, 439))
        ConnectWindow.setMaximumSize(QtCore.QSize(390, 439))
        ConnectWindow.setBaseSize(QtCore.QSize(390, 439))
        ConnectWindow.setStyleSheet("background:#000000;\n"
                                    "border-radius:10px;")
        self.centralwidget = QtWidgets.QWidget(ConnectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WARPLabel = QtWidgets.QLabel(self.centralwidget)
        self.WARPLabel.setGeometry(QtCore.QRect(20, 15, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.WARPLabel.setFont(font)
        self.WARPLabel.setStyleSheet("color:rgb(244, 42, 38);background:transparent;")
        self.WARPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WARPLabel.setIndent(1)
        self.WARPLabel.setOpenExternalLinks(False)
        self.WARPLabel.setObjectName("WARPLabel")
        self.DashLabel = QtWidgets.QLabel(self.centralwidget)
        self.DashLabel.setGeometry(QtCore.QRect(200, 16, 20, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.DashLabel.setFont(font)
        self.DashLabel.setStyleSheet("background:transparent;\n"
                                     "color:rgb(240, 98, 54)")
        self.DashLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DashLabel.setIndent(1)
        self.DashLabel.setOpenExternalLinks(False)
        self.DashLabel.setObjectName("DashLabel")
        self.LinuxLabel = QtWidgets.QLabel(self.centralwidget)
        self.LinuxLabel.setGeometry(QtCore.QRect(220, 16, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.LinuxLabel.setFont(font)
        self.LinuxLabel.setStyleSheet("background:transparent;\n"
                                      "color:rgb(250, 130, 58);")
        self.LinuxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LinuxLabel.setIndent(1)
        self.LinuxLabel.setOpenExternalLinks(False)
        self.LinuxLabel.setObjectName("LinuxLabel")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(120, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setObjectName("StatusLabel")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 400, 393, 40))
        self.widget.setStyleSheet("background:rgb(41, 49, 50);\n"
                                  "border-radius:0px, 0px, 10px, 10px;")
        self.widget.setObjectName("widget")
        self.FooterLabel = QtWidgets.QLabel(self.widget)
        self.FooterLabel.setGeometry(QtCore.QRect(20, 0, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(8)
        self.FooterLabel.setFont(font)
        self.FooterLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.FooterLabel.setObjectName("FooterLabel")
        self.SecondFooterLabel = QtWidgets.QLabel(self.widget)
        self.SecondFooterLabel.setGeometry(QtCore.QRect(20, 15, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(6)
        self.SecondFooterLabel.setFont(font)
        self.SecondFooterLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.SecondFooterLabel.setObjectName("SecondFooterLabel")
        self.BUGButton = QtWidgets.QPushButton(self.widget)
        self.BUGButton.setGeometry(QtCore.QRect(350, 5, 25, 25))
        self.BUGButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUGButton.setStyleSheet("image: url(icons/Button.svg);")
        self.BUGButton.setText("")
        self.BUGButton.setObjectName("BUGButton")
        self.YourInternetLabel = QtWidgets.QLabel(self.centralwidget)
        self.YourInternetLabel.setGeometry(QtCore.QRect(70, 200, 241, 24))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.YourInternetLabel.setFont(font)
        self.YourInternetLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.YourInternetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.YourInternetLabel.setObjectName("YourInternetLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 80, 391, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(104, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushButton_start_end = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start_end.sizePolicy().hasHeightForWidth())
        self.pushButton_start_end.setSizePolicy(sizePolicy)
        self.pushButton_start_end.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_end.setStyleSheet("QPushButton{\n"
                                                "    background-color: #fff; /* Green */\n"
                                                "    border: none;\n"
                                                "    color: #000;\n"
                                                "    padding: 105px 60px;\n"
                                                "    text-align: center;\n"
                                                "    text-decoration: none;\n"
                                                "    font-size: 20px;\n"
                                                "    border-radius:30px;\n"
                                                "}\n"
                                                "QPushButton:hover\n"
                                                "{\n"
                                                "        background-color:#3bb300;\n"
                                                "        color: #fff;\n"
                                                "}\n"
                                                "")
        self.pushButton_start_end.setObjectName("pushButton_start_end")
        self.gridLayout.addWidget(self.pushButton_start_end, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(105, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.WARPLabel.raise_()
        self.DashLabel.raise_()
        self.LinuxLabel.raise_()
        self.widget.raise_()
        self.layoutWidget.raise_()
        self.YourInternetLabel.raise_()
        self.StatusLabel.raise_()
        ConnectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConnectWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnectWindow)

    def retranslateUi(self, ConnectWindow):
        _translate = QtCore.QCoreApplication.translate
        ConnectWindow.setWindowTitle(_translate("ConnectWindow", "Cloudflare WARP"))
        self.WARPLabel.setText(_translate("ConnectWindow", "WARP"))
        self.DashLabel.setText(_translate("ConnectWindow", "-"))
        self.LinuxLabel.setText(_translate("ConnectWindow", "Linux"))
        self.StatusLabel.setText(_translate("ConnectWindow", "Disconnected"))
        self.FooterLabel.setText(_translate("ConnectWindow", "WARP-Linux"))
        self.SecondFooterLabel.setText(_translate("ConnectWindow", "by Cloudflare\n"
                                                                   "and 0xb4dc0d3x"))
        self.YourInternetLabel.setText(_translate("ConnectWindow",
                                                  "<html><head/><body><p><span style=\" font-size:11pt; "
                                                  "color:#ffffff;\">your internet is </span><span style=\" "
                                                  "font-size:11pt; font-weight:600; color:#ffffff;\">not "
                                                  "private</span><span style=\" font-size:11pt; font-weight:600; "
                                                  "color:#ffffff;\"> .</span></p></body></html>"))
        self.pushButton_start_end.setText(_translate("ConnectWindow", "Start"))