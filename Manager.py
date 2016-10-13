#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

class Manager:

    def __init__(self):
        self.origin_folder = "C:\Users\Ana Paula Mello\Downloads"
        self.dentination_folder = None
        self.selected_files = []
        
    def set_keyword(self, word):
        pass
        
    def move_files(self):
        
        for file in self.selected_files:
            current_file_name = self.origin_folder + "\\" + file
            new_file_name = self.destination_folder + "\\" + file
            os.rename(current_file_name, new_file_name)
        
    def find_all_files(self, keyword, display):
        all_files = os.listdir(unicode(self.origin_folder))
        display.clear()
        
        for file in all_files:
            match_object = re.match(r'(.*)'+keyword.lower()+'(.*)', file.lower())
            if match_object:
                display.append(file)
                self.selected_files.append(file)
            
    def create_new_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
        except WindowsError, e:
            print "Folder already exists"
            
    def __rename(self, pattern):
        pass

    def delete(self):
        
        for file in self.selected_files:
            file_path = str(self.origin_folder) + "\\" + file
            os.remove(file_path)
        