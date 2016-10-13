#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

class Manager:

    def __init__(self):
        pass
        self.folder = "C:\Users\Ana Paula Mello\Downloads"
        
    def set_keyword(self, word):
        pass
        
    def move_files(self, *file):
        pass
        
    def find_all_files(self, keyword, display):
        all_files = os.listdir(unicode(self.folder))
        display.clear()
        
        for file in all_files:
            match_object = re.match(r'(.*)'+keyword.lower()+'(.*)', file.lower())
            if match_object:
                display.append(file)
            
    def __create_new_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
        except WindowsError, e:
            print "Folder already exists"
            
    def __rename(self, pattern):
        pass
        
	def __delete(self, pattern):
		pass