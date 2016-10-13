from PyQt4 import QtGui, QtCore
import sys
import Manager

class MainWindow:

    def __init__(self):
    
        self.window = QtGui.QMainWindow()
        self.main_widget = QtGui.QWidget()
        
        self.window.setCentralWidget(self.main_widget)
        
        self.horizontal_box = QtGui.QHBoxLayout()
        self.first_column = QtGui.QVBoxLayout()
        self.second_column = QtGui.QVBoxLayout()
        self.first_row = QtGui.QHBoxLayout()
        self.second_row = QtGui.QHBoxLayout()
        self.third_row = QtGui.QHBoxLayout()
        
        self.second_column.addLayout(self.first_row)
        self.second_column.addLayout(self.second_row)
        self.first_column.addLayout(self.third_row)
        self.horizontal_box.addLayout(self.first_column)
        self.horizontal_box.addLayout(self.second_column)
        self.horizontal_box.setAlignment(QtCore.Qt.AlignRight)
        self.main_widget.setLayout(self.horizontal_box)
        
        self.assistent = Manager.Manager()
    
    def open_window(self):
                
        self.keyword_search_input = QtGui.QLineEdit()
        self.first_column.addWidget(self.keyword_search_input)
        self.keyword_search_input.setMinimumWidth(300)
        
        search_files_button = QtGui.QPushButton("Set keyword")
        self.third_row.addWidget(search_files_button)
        search_files_button.setMaximumWidth(100)
        search_files_button.clicked.connect(self.get_info)
        
        run_button = QtGui.QPushButton("Run")
        self.third_row.addWidget(run_button)
        run_button.setMaximumWidth(100)
        run_button.clicked.connect(self.run)
                    
        save_button = QtGui.QPushButton("Save preferences")
        self.third_row.addWidget(save_button)
        save_button.setMaximumWidth(100)
        save_button.clicked.connect(self.save)
        
        new_folder_box = QtGui.QCheckBox()
        new_folder_box.setText("Create new folder")
        self.first_column.addWidget(new_folder_box)
        
        always_box = QtGui.QCheckBox()
        always_box.setText("Always repeat")
        self.first_column.addWidget(always_box)
		
        delete_box = QtGui.QCheckBox()
        delete_box.setText("Delete")
        self.first_column.addWidget(delete_box)

        rename_box = QtGui.QCheckBox()
        rename_box.setText("Rename files")
        self.first_column.addWidget(rename_box)
        
        self.rename_patterns_input = QtGui.QLineEdit()
        self.first_column.addWidget(self.rename_patterns_input)
        
        self.origin_folder = QtGui.QLineEdit()
        self.origin_folder.setMinimumWidth(300)
        self.first_row.addWidget(self.origin_folder)
        
        self.origin_folder_button = QtGui.QPushButton("...")
        self.origin_folder_button.clicked.connect(self._set_folder)
        self.first_row.addWidget(self.origin_folder_button)
        
        self.destination_folder = QtGui.QLineEdit()
        self.destination_folder.setMinimumWidth(300)
        self.second_row.addWidget(self.destination_folder)
        
        self.destination_folder_button = QtGui.QPushButton("...")
        self.second_row.addWidget(self.destination_folder_button)
        
        self.all_folders_list = QtGui.QTextEdit()
        self.all_folders_list.setReadOnly(True)
        self.second_column.addWidget(self.all_folders_list)
        
        self.window.move(100, 100)
        self.window.setWindowTitle("Download Manage")
        self.window.show()
        
    def get_info(self):
        self.keyword = self.keyword_search_input.text()
        self.assistent.find_all_files(str(self.keyword), self.all_folders_list)
        
    def _set_folder(self):
        self.assistent.folder = QtGui.QFileDialog.getExistingDirectory(None, "Select folder: ", "C:\Users\Ana Paula Mello\Downloads", QtGui. QFileDialog.ShowDirsOnly)
        
    def save(self):
        pass
    
    def run(self):
        pass