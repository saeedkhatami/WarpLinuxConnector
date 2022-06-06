import os
import sys
import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction, QMessageBox
from warpGui.toggle import AnimatedToggle
from warpGui.commands import Command
from warpGui.UI.connectWindowUI import Ui_ConnectWindow


class GUIConnect:
    def __init__(self):
        self.msg = None
        self.__menu_tray_quit = None
        self.__menu_tray_hide = None
        self.__menu_tray_connect = None
        self.menu_tray = None
        self.tray_icon = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = QtWidgets.QMainWindow()
        self.UI = Ui_ConnectWindow()
        self.commend = Command()
        self.UI.setupUi(self.mainWindow)
        self.need_stop = False
        self.last_status = self.commend.status()
        self.connected = self.commend.is_connected()
        threading.Thread(target=self.status_thread).start()
        self.init_tray_icon()
        self.toggle_color = "#FF6633"
        self.toggle = self.init_toggle(self.toggle_color)
        self.init_signals()
        self.set_icon()

    def init_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(QIcon(os.path.dirname(__file__) + '/../icons/offline.png'), self.mainWindow)
        self.menu_tray = QMenu()
        self.__menu_tray_connect = QAction("Connect / Disconnect")
        self.menu_tray.addAction(self.__menu_tray_connect)
        self.__menu_tray_hide = QAction("Hide / Show")
        self.menu_tray.addAction(self.__menu_tray_hide)
        self.__menu_tray_quit = QAction("Quit")
        self.menu_tray.addAction(self.__menu_tray_quit)
        self.tray_icon.setContextMenu(self.menu_tray)
        self.tray_icon.show()

    def set_tray_icon(self, connected):
        if connected:
            self.tray_icon.setIcon(QIcon(os.path.dirname(__file__) + '/../icons/online.png'))
        else:
            self.tray_icon.setIcon(QIcon(os.path.dirname(__file__) + '/../icons/offline.png'))

    def init_toggle(self, color):
        toggle = AnimatedToggle(checked_color=color, pulse_checked_color="#FFFFFF")
        status = self.commend.status()
        # print(self.commend.status())
        if self.connected and status == "Connected":
            self.set_sub_status_message('private', 'FF6633')
            toggle.setChecked(True)
            self.UI.StatusLabel.setStyleSheet(u"color:rgb(255, 255, 255);")  # label color to green
            self.set_tray_icon(True)
        toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        toggle.setMinimumSize(132, 65)
        toggle.setBaseSize(132, 65)
        toggle.setMaximumSize(132, 65)
        self.UI.pushButton_start_end.close()
        self.UI.gridLayout.addWidget(toggle, 0, 1, 1, 1)
        return toggle

    def set_icon(self):
        self.mainWindow.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/../icons/logo.png"))

    def init_signals(self):
        self.toggle.clicked.connect(self.connect_button_clicked)
        self.UI.BUGButton.clicked.connect(self.bug_button_clicked)
        self.__menu_tray_connect.triggered.connect(self.tray_connect_disconnect_clicked)
        self.__menu_tray_hide.triggered.connect(self.tray_hide_show_clicked)
        self.__menu_tray_quit.triggered.connect(self.app.quit)

    def tray_hide_show_clicked(self):
        if self.mainWindow.isHidden():
            self.mainWindow.show()
        else:
            self.mainWindow.hide()

    def tray_connect_disconnect_clicked(self):
        if not self.commend.is_connected():
            self.commend.connect()
        else:
            self.commend.disconnect()

    def connect_button_clicked(self):
        if self.toggle.isChecked():

            self.commend.connect()
        else:
            self.commend.disconnect()

    def bug_button_clicked(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Please open an issue in Github repository")
        self.msg.setInformativeText('And raise your problem')
        self.msg.setWindowTitle("BUG report")
        self.msg.exec_()
        # self.warpGui.bug.bug()

    def show(self, hide=False):
        if not hide:
            self.mainWindow.show()
        self.app.aboutToQuit.connect(self.end_program)
        sys.exit(self.app.exec_())

    def end_program(self):
        self.need_stop = True

    def status_thread(self):
        while not self.need_stop:
            status = self.commend.status()
            if status:
                self.UI.StatusLabel.setText(status)

            if self.last_status != status:
                if status == 'Connected':
                    self.toggle.setChecked(True)
                    self.UI.StatusLabel.setStyleSheet(u"color:rgb(255, 255, 255);")
                    self.set_sub_status_message('private', 'FF6633')
                    self.connected = True
                    self.set_tray_icon(True)
                elif status == 'Disconnected' or \
                        status == 'No network':
                    self.toggle.setChecked(False)
                    self.set_sub_status_message('not private', 'FFFFFF')
                    self.UI.StatusLabel.setStyleSheet(u"color:rgb(255, 255, 255);")
                    self.connected = False
                    self.set_tray_icon(False)
                self.last_status = status
            time.sleep(3)

    def set_sub_status_message(self, text, color):
        self.UI.YourInternetLabel.setText(
            "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Your internet is </span><span "
            "style=\" font-size:11pt; font-weight:600; color:#{color};\">{text}</span></p></body></html>".format(
                text=text, color=color))
