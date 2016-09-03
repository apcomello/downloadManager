#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Manager:

    def __init__(self):
        pass
        self.default_folder = "C:\Users\Ana Paula Mello\Downloads"
        
    def set_keyword(self, word):
        pass
        
    def move_files(self, *file):
        pass
        
    def find_all_files(self):
        print os.listdir(os.getcwd())
            
    def __create_new_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
        except WindowsError, e:
            print "Folder already exists"
    def __rename(self, pattern):
        pass
