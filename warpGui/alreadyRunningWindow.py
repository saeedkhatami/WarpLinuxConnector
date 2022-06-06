from warpGui.UI.alreadyRunningWindowUI import *
import sys
import os


def already_running():
    app = QtWidgets.QApplication(sys.argv)
    Already_running = QtWidgets.QDialog()
    ui = Ui_alreadyRunningWindow()
    ui.setupUi(Already_running)
    app.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/../icons/sign-error-icon.png"))
    Already_running.show()
    sys.exit(app.exec_())
