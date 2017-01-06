#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

class Manager:

    def __init__(self):
        self.origin_folder = "C:\Users\Ana Paula Mello\Downloads"
        self.dentination_folder = None
        self.selected_files = []
        self.new_file_names = None
        
    def set_keyword(self, word):
        pass
        
    def move_files(self, new_file_names):

        for file in self.selected_files:
            if new_file_names:
                new_name = new_file_names[file[1]]
            else:
                new_name = file[1]
                
            current_file_name = os.path.join(file[0], file[1])
            new_file_name = os.path.join(str(self.destination_folder), new_name)
            os.rename(current_file_name, new_file_name)
            
    def find_all_files(self, keyword, display):
        self.selected_files = []
        display.clear()
        
        for root, dirs, files in os.walk(unicode(self.origin_folder)):
            for file in files:
                match_object = re.match(r'(.*)'+keyword.lower()+'(.*)', file.lower())
                if match_object:
                    display.append(file)
                    self.selected_files.append((root, file))
           
    def create_new_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
        except WindowsError, e:
            print "Folder already exists"
            
    def rename(self, pattern):
    
        season_episode = None
        new_file_names = {}
        
        for file in self.selected_files:
            file_extension = str(file[1]).split(".")[-1]
            modify_pattern = str(pattern)
            season_episode = None
            if 'S%dE%d' in pattern:
                replacement = 'S%dE%d'
                season_episode = re.search("S[0-9]{1,2}E[0-9]{1,2}", file[1])
            elif '%dX%d' in pattern:
                replacement = '%dX%d'
                season_episode = re.search("[0-9]{1,2}(X|x)[0-9]{1,2}", file[1])
                            
            if season_episode:
                new_pattern = modify_pattern.replace(replacement, season_episode.group(0)) + "." + file_extension
                new_file_names[file[1]] = new_pattern
        
        return new_file_names

    def delete(self):
        
        for file in self.selected_files:
            file_path = str(self.origin_folder) + "\\" + file
            os.remove(file_path)
        
    def new_folder(self, folder_name, new_file_names):
        
        new_folder = os.path.join(str(self.destination_folder), folder_name)
        self.create_new_folder(new_folder)
        self.destination_folder = new_folder
        self.move_files(new_file_names)
