import Forms
import Manager
from PyQt4 import QtGui

# app = QtGui.QApplication(sys.argv)

# main = Forms.MainWindow()

# main.open_window()

# sys.exit(app.exec_())

manager = Manager.Manager()

manager.find_all_files()
manager._Manager__create_new_folder("C:\Users\Ana Paula Mello\Hub\Series\Veep")