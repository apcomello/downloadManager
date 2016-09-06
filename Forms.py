from PyQt4 import QtGui, QtCore
import sys

class MainWindow:

    def __init__(self):
    
        self.window = QtGui.QWidget()
        
        self.horizontal_box = QtGui.QHBoxLayout()
        self.first_column = QtGui.QVBoxLayout()
        self.second_column = QtGui.QVBoxLayout()
        self.first_row = QtGui.QHBoxLayout()
        self.second_row = QtGui.QHBoxLayout()
        
        self.second_column.addLayout(self.first_row)
        self.second_column.addLayout(self.second_row)
        self.horizontal_box.addLayout(self.first_column)
        self.horizontal_box.addLayout(self.second_column)
        self.horizontal_box.setAlignment(QtCore.Qt.AlignRight)
        self.window.setLayout(self.horizontal_box)
    
    def open_window(self):
                
        self.keyword_search_input = QtGui.QLineEdit()
        self.first_column.addWidget(self.keyword_search_input)
        self.keyword_search_input.setMinimumWidth(300)
                    
        search_files_button = QtGui.QPushButton("Search")
        self.first_column.addWidget(search_files_button)
        search_files_button.setMaximumWidth(50)
        search_files_button.clicked.connect(self.get_info)
        
        new_folder_box = QtGui.QCheckBox()
        new_folder_box.setText("Create new folder")
        self.first_column.addWidget(new_folder_box)
        
        always_box = QtGui.QCheckBox()
        always_box.setText("Always repeat")
        self.first_column.addWidget(always_box)
        
        rename_box = QtGui.QCheckBox()
        rename_box.setText("Rename files")
        self.first_column.addWidget(rename_box)
        
        self.rename_patterns_input = QtGui.QLineEdit()
        self.first_column.addWidget(self.rename_patterns_input)
        
        self.origin_folder = QtGui.QLineEdit()
        self.origin_folder.setMinimumWidth(300)
        self.first_row.addWidget(self.origin_folder)
        
        self.origin_folder_button = QtGui.QPushButton("...")
        self.first_row.addWidget(self.origin_folder_button)
        
        self.destination_folder = QtGui.QLineEdit()
        self.destination_folder.setMinimumWidth(300)
        self.second_row.addWidget(self.destination_folder)
        
        self.destination_folder_button = QtGui.QPushButton("...")
        self.second_row.addWidget(self.destination_folder_button)
        
        all_folders_list = QtGui.QLabel()
        self.second_column.addWidget(all_folders_list)
        
        all_folders_list.resize(50, 100)
        all_folders_list.setText("Hello, world")
        all_folders_list.setStyleSheet('background-color: white; padding: 5%;')
        
        self.window.move(100, 100)
        self.window.setWindowTitle("Download Manage")
        self.window.show()
        
    def get_info(self):
        print self.keyword_search_input.text()