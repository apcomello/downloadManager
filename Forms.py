#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import Manager

class MainWindow:

    def __init__(self):
    
        # Main widgets
        self.window = QtGui.QMainWindow()
        self.main_widget = QtGui.QWidget()
        
        self.window.setCentralWidget(self.main_widget)
        
        # Layout
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
        self.new_file_names = None
    
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
        
        self.new_folder_box = QtGui.QCheckBox()
        self.new_folder_box.setText("Create new folder")
        self.first_column.addWidget(self.new_folder_box)
        
        self.folder_name_input = QtGui.QLineEdit()
        self.first_column.addWidget(self.folder_name_input)
        
        self.always_box = QtGui.QCheckBox()
        self.always_box.setText("Always repeat")
        self.first_column.addWidget(self.always_box)
		
        self.delete_box = QtGui.QCheckBox()
        self.delete_box.setText("Delete")
        self.first_column.addWidget(self.delete_box)

        self.rename_box = QtGui.QCheckBox()
        self.rename_box.setText("Rename files")
        self.first_column.addWidget(self.rename_box)
                
        self.rename_patterns_input = QtGui.QLineEdit()
        self.first_column.addWidget(self.rename_patterns_input)
        
        self.origin_folder = QtGui.QLineEdit()
        self.origin_folder.setMinimumWidth(300)
        self.first_row.addWidget(self.origin_folder)
        
        self.origin_folder_button = QtGui.QPushButton("Source")
        self.origin_folder_button.clicked.connect(self._set_origin_folder)
        self.first_row.addWidget(self.origin_folder_button)
        
        self.destination_folder = QtGui.QLineEdit()
        self.destination_folder.setMinimumWidth(300)
        self.second_row.addWidget(self.destination_folder)
        
        self.destination_folder_button = QtGui.QPushButton("Destination")
        self.destination_folder_button.clicked.connect(self._set_destination_folder)
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
        
    def _set_origin_folder(self):
        self.assistent.origin_folder = QtGui.QFileDialog.getExistingDirectory(None, "Select folder: ", "C:\Users\Ana Paula Mello\Downloads", QtGui. QFileDialog.ShowDirsOnly)
        self.origin_folder.setText(self.assistent.origin_folder)
    
    def _set_destination_folder(self):
        self.assistent.destination_folder = QtGui.QFileDialog.getExistingDirectory(None, "Select folder: ", "C:\Users\Ana Paula Mello\Downloads", QtGui. QFileDialog.ShowDirsOnly)
        self.destination_folder.setText(self.assistent.destination_folder)

    def save(self):
        pass
    
    def run(self):
    
        if self.rename_box.isChecked():
            pattern = self.rename_patterns_input.text()
            self.new_file_names = self.assistent.rename(pattern)
        if self.new_folder_box.isChecked():
            folder_name = self.folder_name_input.text()
            self.assistent.new_folder(str(folder_name), self.new_file_names)
        elif self.delete_box.isChecked():
            self.assistent.delete()
        else:
            self.assistent.move_files(self.new_file_names)
