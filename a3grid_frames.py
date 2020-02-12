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
from tkinter.scrolledtext import ScrolledText
from tkinter import *

#CONSTANTS-----------------------------------------------------------------


#CLASSES-------------------------------------------------------------------
class MainMenu(tk.Frame):
    def __init__(self):
        '''This function creates a main menu for the database,
        inlcuding positioning and jobs of widgets'''
        
        tk.Frame.__init__(self)
        
        '''NOT WORKING to configure columns
        self.columnconfigure(0, weight = 100)
        self.columnconfigure(1, weight = 100)
        self.columnconfigure(2, weight = 100)          
        '''
        
        lbl_title = tk.Label(text = "Movie Database",
                             font = ("Times", "35"))
        lbl_title.grid(row = 0, 
                       column = 1, 
                       sticky = "news")
        
        btn_add = tk.Button(text = "Add New Movie",
                            font = ("Courier", "16"))
        btn_add.grid(row = 1, 
                     column = 1)
        
        btn_edit = tk.Button(text = "Edit Existing Movie",
                             font = ("Courier", "16"))
        btn_edit.grid(row = 2, 
                      column = 1)
        
        btn_search = tk.Button(text = "Search Library",
                               font = ("Courier", "16"))
        btn_search.grid(row = 3, 
                        column = 1)
        
        btn_remove = tk.Button(text = "Remove Existing",
                              font = ("Courier", "16"))
        btn_remove.grid(row = 4, 
                        column = 1)      
        
        btn_save = tk.Button(text = "Save Changes",
                             font = ("Courier", "16"))
        btn_save.grid(row = 5, 
                      column = 1) 
        
        
class Search(tk.Frame):
    '''This Frame will be the Print All/Search By page'''
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        lbl_title = tk.Label(text = "Search Library",
                             font = ("Times", "35"))
        lbl_title.grid(row = 0, 
                       column = 1, 
                       columnspan = 2, 
                       sticky = "news")
        
        lbl_sb = tk.Label(text = "Search By: ",
                          font = ("Times", 15))
        lbl_sb.grid(row = 1, 
                    column = 0, 
                    columnspan = 2)
        
        lbl_pf = tk.Label(text = "Print Filters: ",
                          font = ("Times", 15))
        lbl_pf.grid(row = 1, 
                    column = 2, 
                    columnspan = 2)
        
        '''MAKE DROP DOWN'''
        dd_sb = tk.Entry()
        dd_sb.grid(row = 2, 
                   column = 0, 
                   columnspan = 2)
        
        chk1 = tk.Checkbutton(text = "Title",
                              font = ("Times", 15))
        chk1.grid(row = 2, 
                  column = 2)
        
        chk2 = tk.Checkbutton(text = "Genre",
                              font = ("Times", 15))
        chk2.grid(row = 3, 
                  column = 2)
        
        chk3 = tk.Checkbutton(text = "Director",
                              font = ("Times", 15))
        chk3.grid(row = 4, 
                  column = 2)
        
        chk4 = tk.Checkbutton(text = "Viewer Rating",
                              font = ("Times", 15))
        chk4.grid(row = 2, 
                  column = 3)
        
        chk5 = tk.Checkbutton(text = "Star Rating",
                              font = ("Times", 15))
        chk5.grid(row = 3, 
                  column = 3)
        
        chk6 = tk.Checkbutton(text = "Release Year",
                              font = ("Times", 15))
        chk6.grid(row = 4, 
                  column = 3)  
        
        chk7 = tk.Checkbutton(text = "Top-Billed",
                              font = ("Times", 15))
        chk7.grid(row = 5, 
                  column = 2)        
        
        
        lbl_sf = tk.Label(text = "Search For: ",
                          font = ("Times", 15))
        lbl_sf.grid(row = 4, 
                    column = 0,
                    columnspan = 2)
        
        ent_sf = tk.Entry()
        
        ent_sf.grid(row = 5,
                    column = 0,
                    columnspan = 2)
        
        scrtxt = ScrolledText(height = 8,
                              width = 40)
        scrtxt.grid(row = 6, 
                    column = 0,
                    columnspan = 4)
        
        btn_back = tk.Button(text = "Back",
                             font = ("Times", 15))
        btn_back.grid(row = 7, 
                      column = 0)
        
        btn_reset = tk.Button(text = "Reset",
                              font = ("Times", 15))
        btn_reset.grid(row = 7,
                       column = 2)
        
        btn_submit = tk.Button(text = "Submit", 
                               font = ("Times", 15))
        btn_submit.grid(row = 7, 
                        column = 3)
        
class AddEdit(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        
        lbl_title = tk.Label(text = "Title: ",
                             font = ("Courier", 12))
        lbl_title.grid(row = 0,
                       column = 0)
        
        lbl_genre = tk.Label(text = "Genre: ",
                             font = ("Courier", 12))
        lbl_genre.grid(row = 1,
                       column = 0)
        
        lbl_dir = tk.Label(text = "Director(s): ",
                           font = ("Courier", 12))
        lbl_dir.grid(row = 2,
                       column = 0)        
        
        ent_title = tk.Entry()
        ent_title.grid(row = 0, 
                       column = 1,
                       columnspan = 3)
        
        ent_genre = tk.Entry()
        ent_genre.grid(row = 1, 
                       column = 1,
                       columnspan = 3)
        
        ent_dir = tk.Entry()
        ent_dir.grid(row = 2, 
                       column = 1,
                       columnspan = 3)  
        
        lbl_releaseyr = tk.Label(text = "Release Year: ",
                                 font = ("Courier", 12))
        lbl_releaseyr.grid(row = 3,
                           column = 0)
        
        ent_releaseyr = tk.Entry()
        ent_releaseyr.grid(row = 3, 
                           column = 1)
        
        lbl_rate = tk.Label(text = "Viewer Rating: ",
                            font = ("Courier", 12))
        lbl_rate.grid(row = 3,
                      column = 2)        
        
        ent_rate = tk.Entry()
        ent_rate.grid(row = 3,
                      column = 3)
        
        lbl_1star = tk.Label(text = "Star Rating",
                             font = ("Courier", 12))
        lbl_1star.grid(row = 4, 
                       column = 0,
                       columnspan = 2)
        
        ent_stars = tk.Entry()
        ent_stars.grid(row = 4,
                       column  = 2)
        
        lbl_2star = tk.Label(text = "/10",
                             font = ("Courier", 12))
        lbl_2star.grid(row = 4,
                       column = 3)
        
        lbl_tb = tk.Label(text = "Top-Billed: ",
                          font = ("Courier", 12))
        lbl_tb.grid(row = 5,
                    column = 0)
        
        ent_tb = tk.Entry()
        
        ent_tb.grid(row = 6, 
                    column = 0)
        
        lbl_sb = tk.Label(text = "Second-Billed: ",
                          font = ("Courier", 12))
        lbl_sb.grid(row = 7,
                    column = 0)
        
        ent_sb = tk.Entry()
        
        ent_sb.grid(row = 8, 
                    column = 0)
        
        lbl_thb = tk.Label(text = "Third-Billed: ",
                          font = ("Courier", 12))
        lbl_thb.grid(row = 9,
                    column = 0)
        
        ent_thb = tk.Entry()
        
        ent_thb.grid(row = 10, 
                    column = 0)        
        
        scrtxt = ScrolledText(height = 8,
                                  width = 40)
        scrtxt.grid(row = 5,
                    rowspan = 6,
                    column = 2,
                    columnspan = 2)
        
        btn_back = tk.Button(text = "Back", 
                             font = ("Courier", 12))
        btn_back.grid(row = 11,
                      column = 0)
        
        btn_reset = tk.Button(text = "Reset", 
                             font = ("Courier", 12))
        btn_reset.grid(row = 11,
                      column = 2) 
        
        btn_submit = tk.Button(text = "Submit", 
                             font = ("Courier", 12))
        btn_submit.grid(row = 11,
                        column = 3)        
        
class Remove(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        
        lbl_rem1 = tk.Label(text = "These titles are ",
                            font = ("Times", "35"))
        lbl_rem1.grid(row = 0,
                      column = 0, 
                      columnspan = 2)
        lbl_rem2 = tk.Label(text = "marked for removal!",
                            font = ("Times", "35"))
        lbl_rem2.grid(row = 1, 
                      column = 0, 
                      columnspan = 2)
        
        scrtxt = ScrolledText(height = 8,
                                  width = 40)
        scrtxt.grid(row = 2, 
                    column = 0,
                    columnspan = 2)  
        
        btn_cancel = tk.Button(text = "Cancel",
                               font = ("Times", "35"))
        btn_cancel.grid(row = 3, 
                        column = 0)
        btn_conf = tk.Button(text = "Confirm",
                             font = ("Times", "35"))
        btn_conf.grid(row = 3,
                      column = 1)

        
#FUNCTIONS-----------------------------------------------------------------
'''
THIS DOES NOT WORK 
NEED TO FIGURE THIS OUT

def check_edit_mb():
    messagebox.showinfo("Edit Movie", "Which movie would you like to Edit?")
'''


#MAIN-----------------------------------------------------------------------
if __name__ == "__main__":
    
    in_file = open("movie_lib.pickle", "rb")
    movies = p.load(in_file)  
    in_file.close()
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry("1000x500")
    root.title("Movie Library NG")
    
    main_menu = Remove()
    main_menu.grid(row = 0, column = 0,
                   sticky = "news")  
    
    root.mainloop()           