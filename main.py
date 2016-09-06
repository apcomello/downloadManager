import Forms
import Manager
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)

main_window = Forms.MainWindow()

main_window.open_window()

sys.exit(app.exec_())

# manager = Manager.Manager()

# manager.find_all_files()
