from warpGui.ConnectWindow import GUIConnect
import sys
import warpGui.alreadyRunningWindow
import socket

try:
    # check program already running or not
    s = socket.socket()
    s.bind(('', 45367))
except:
    warpGui.alreadyRunningWindow.already_running()
    sys.exit(-1)

gui = GUIConnect()
if len(sys.argv) == 2 and sys.argv[1] == '--hide':
    # hide mode (only tray icon)
    gui.show(hide=True)
else:
    # normal mode
    gui.show(hide=False)
