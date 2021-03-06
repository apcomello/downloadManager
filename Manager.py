#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import shutil

class Manager:

    def __init__(self):
        
        ## CHANGE THIS## CHANGE THIS## CHANGE THIS## CHANGE THIS## CHANGE THIS
        self.origin_folder = "C:\Users\Ana Paula Mello\Downloads"
        ## CHANGE THIS## CHANGE THIS## CHANGE THIS## CHANGE THIS## CHANGE THIS
        
        self.dentination_folder = None
        self.selected_files = []
        self.selected_directories = []
        self.new_file_names = None
        
    # def set_keyword(self, word):
        # pass
        
    def move_files(self, new_file_names):
        '''
        Moves selected files to the destination folder, using the appropriate name
        '''

        for file in self.selected_files:
        
            # Treats the renaming (or not) of files
            if new_file_names:
                new_name = new_file_names[file[1]]
            else:
                new_name = file[1]
                
            current_file_name = os.path.join(file[0], file[1])
            new_file_name = os.path.join(str(self.destination_folder), new_name)
            os.rename(current_file_name, new_file_name)
            
    def find_all_files(self, keyword, display):
        '''
        Selects all files in the source directory that match the keyword
        '''

        self.selected_files = []
        self.selected_directories = []
        display.clear()
        
        for root, dirs, files in os.walk(unicode(self.origin_folder)):      # Finds files with the  keywords even inside folders
        
            # Keyword is not a wildcard
            if not re.match(r'\*\.(.*)', keyword.lower()):
                # Finds all directoris with the keyword
                for dir in dirs:
                    matching_keyword = re.match(r'(.*)'+keyword.lower()+'(.*)', dir.lower())
                    if matching_keyword:
                        display.append(dir)
                        self.selected_directories.append(os.path.join(root, dir))
                
                # Finds all the files with the keyword
                for file in files:
                    matching_keyword = re.match(r'(.*)'+keyword.lower()+'(.*)', file.lower())
                    if matching_keyword:
                        display.append(file)
                        self.selected_files.append((root, file))
            
            # Keyword is a wildcard
            else:
                file_extension = str(keyword.lower()).split(".")[-1]
                for file in files:
                    matching_keyword = re.match(r'(.*)\.'+ file_extension.lower(), file.lower())
                    if matching_keyword:
                        display.append(file)
                        self.selected_files.append((root, file))
                                            
    def create_new_folder(self, folder_name):
        '''
        Creates a new folder with the given name
        '''
        
        ## Might need to change all of this. I don't like it very much
        
        new_folder = os.path.join(str(self.destination_folder), folder_name)
        self.destination_folder = new_folder

        try:
            os.mkdir(new_folder)
            return True
        except WindowsError, e:
            return False
            
    def rename(self, pattern):
        '''
        Renames all files selected according to a given pattern
        '''

        season_episode = None
        new_file_names = {}
        
        for file in self.selected_files:
            file_extension = str(file[1]).split(".")[-1]
            modify_pattern = str(pattern)
            season_episode = None
            
            # Treats two possible renaming patterns
            ## TODO: Add more patterns
            ##       Make option to add custom patterns
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
        '''
        Deletes all selected folders and directories
        '''
        
        for dir in self.selected_directories:   # For directories
            shutil.rmtree(dir)
        
        for file in self.selected_files:    # For files
            if file[0] not in self.selected_directories:       # Doesn't include the path for files inside selected folder
                file_path =  os.path.join(file[0], file[1])
                os.remove(file_path)
                
    def save_preferences(self):
        pass
        