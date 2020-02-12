#!usr/bin/python3
#Noel Glamann
#10 February 2020

'''
This program will develop the Graphical User 
Interface (GUI) for the Movie Library function. 

Most updated version of movie database is under
the name 
          7fixed_remove.py
          last updated: 4 Feb 2020
          
This file last updated: 11 Feb 2020
          
'''

#IMPORTS-------------------------------------------------------------------
import pickle as p
import tkinter as tk
from tkinter import scrolledtext

#CONSTANTS-----------------------------------------------------------------


#CLASSES-------------------------------------------------------------------
class MainMenu(tk.Frame):
    def __init__(self):
        '''This function creates a main menu for the database,
        inlcuding positioning and jobs of widgets'''
        
        tk.Frame.__init__(self)
        
        
        self.columnconfigure(0, weight = 100)
        self.columnconfigure(1, weight = 100)
        self.columnconfigure(2, weight = 100)          
        
        lbl_title = tk.Label(text = "Movie Database",
                             font = ("Times", "35"))
        lbl_title.grid(row = 0, column = 1, 
                       sticky = "news")
        
        btn_add = tk.Button(text = "Add New Movie",
                            font = ("Courier", "16"))
        btn_add.grid(row = 1, column = 1)
        
        btn_edit = tk.Button(text = "Edit Existing Movie",
                             font = ("Courier", "16"))
        btn_edit.grid(row = 2, column = 1)
        
        btn_search = tk.Button(text = "Search Library",
                               font = ("Courier", "16"))
        btn_search.grid(row = 3, column = 1)
        
        btn_remove = tk.Button(text = "Remove Existing",
                              font = ("Courier", "16"))
        btn_remove.grid(row = 4, column = 1)      
        
        btn_save = tk.Button(text = "Save Changes",
                             font = ("Courier", "16"))
        btn_save.grid(row = 5, column = 1) 
        
               
        
        
#FUNCTIONS-----------------------------------------------------------------


#MAIN-----------------------------------------------------------------------
if __name__ == "__main__":
    
    in_file = open("movie_lib.pickle", "rb")
    movies = p.load(in_file)  
    in_file.close()
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Movie Library NG")
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0,
                   sticky = "news")  
    
    root.mainloop()           