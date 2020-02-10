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
          
'''

#IMPORTS-------------------------------------------------------------------
import pickle as p
import tkinter as tk
from tkinter import scrolledtext

#CONSTANTS-----------------------------------------------------------------


#CLASSES-------------------------------------------------------------------
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        lbl_title = tk.Label(text = "Movie Database",
                             font = ("Times", "35"))
        lbl_title.grid(row = 0, column = 0,
                       sticky = "news")
        
        btn_add = tk.Button(text = "Add New Movie",
                            font = ("Arial", "16"))
        btn_add.grid(row = 1, column = 0)
        
        btn_edit = tk.Button(text = "Edit Existing Movie",
                             font = ("Arial", "16"))
        btn_edit.grid(row = 2, column = 0)
        
        btn_search = tk.Button(text = "Search Library",
                               font = ("Arial", "16"))
        btn_search.grid(row = 3, column = 0)
        
        btn_remove = tk.Button(text = "Remove Existing",
                              font = ("Arial", "16"))
        btn_remove.grid(row = 4, column = 0)      
        
        btn_save = tk.Button(text = "Save Changes",
                             font = ("Arial", "16"))
        btn_save.grid(row = 5, column = 0)        
        
        
#FUNCTIONS-----------------------------------------------------------------


#MAIN-----------------------------------------------------------------------
if __name__ == "__main__":
    
    in_file = open("movie_lib.pickle", "rb")
    movies = p.load(in_file)  
    in_file.close()
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Movie Library NG")
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0,
                   sticky = "news")
    
    root.mainloop()           