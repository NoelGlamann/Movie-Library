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


#CONSTANTS-----------------------------------------------------------------


#CLASSES-------------------------------------------------------------------
class MainMenu(tk.Frame):
    def __init__(self):
        '''This function creates a main menu for the database,
        inlcuding positioning and jobs of widgets'''
        
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Movie Database",
                             font = ("Times", "50"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news")
        
        self.btn_add = tk.Button(self, text = "Add New Movie",
                            font = ("Courier", "16"))
        self.btn_add.grid(row = 2, 
                     column = 1, 
                       sticky = "news")
        
        self.btn_edit = tk.Button(self, text = "Edit Existing Movie",
                             font = ("Courier", "16"))
        self.btn_edit.grid(row = 3, 
                      column = 1, 
                       sticky = "news")
        
        self.btn_search = tk.Button(self, text = "Search Library",
                               font = ("Courier", "16"))
        self.btn_search.grid(row = 4, 
                        column = 1, 
                       sticky = "news")
        
        self.btn_remove = tk.Button(self, text = "Remove Existing",
                              font = ("Courier", "16"))
        self.btn_remove.grid(row = 5, 
                        column = 1, 
                       sticky = "news")      
        
        self.btn_save = tk.Button(self, text = "Save Changes",
                             font = ("Courier", "16"))
        self.btn_save.grid(row = 6, 
                      column = 1, 
                       sticky = "news") 
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(1, weight = 2)
        self.grid_rowconfigure(7, weight = 2)
        
        
        
        
class Search(tk.Frame):
    '''This Frame will be the Print All/Search By page'''
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Search Library",
                             font = ("Times", 50))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3, 
                       sticky = "news")
        
        self.lbl_sb = tk.Label(self, text = "Search By: ",
                          font = ("Times", 20))
        self.lbl_sb.grid(row = 1, 
                    column = 0, 
                    #columnspan = 2,
                   sticky = "news")
        
        '''MAKE DROP DOWN'''
        
        self.tkvar = tk.StringVar(self)
        
        choices = ['Title', 'Genre', 'Director', 
                        'Top-Billed Actors', 'Release Year', 
                        'Viewer Rating', 'Star Rating']
        
        self.tkvar.set('Title')
        
        self.drop_down = tk.OptionMenu(self, self.tkvar, *choices)
        
        self.drop_down.grid(row = 2, 
                            column = 0, 
                            #columnspan = 2,
                            sticky = "news")
        
        self.check_boxes = ChkBoxes(self)
        self.check_boxes.grid(row = 1,
                              rowspan = 5,
                              column = 2,
                              #columnspan = 2,
                              sticky = "news")
        
        self.lbl_sf = tk.Label(self, text = "Search For: ",
                               font = ("Times", 20))
        self.lbl_sf.grid(row = 4, 
                    column = 0,
                    #columnspan = 2,
                   sticky = "news")
        
        self.ent_sf = tk.Entry(self)
        
        self.ent_sf.grid(row = 5,
                    column = 0,
                    #columnspan = 2,
                   sticky = "news")
        
        self.scrtxt = ScrolledText(self, height = 10,
                                   width = 20)
        self.scrtxt.grid(row = 6, 
                         column = 0,
                         columnspan = 3,
                         sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Back",
                                  font = ("Times", 20))
        self.btn_back.grid(row = 7, 
                           column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset",
                                   font = ("Times", 20))
        self.btn_reset.grid(row = 7,
                            column = 1)
        
        self.btn_submit = tk.Button(self, text = "Submit", 
                                    font = ("Times", 20))
        self.btn_submit.grid(row = 7, 
                             column = 2)
        
        self.grid_columnconfigure(0, weight = 1)
        #self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        """self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_rowconfigure(4, weight = 1)
        self.grid_rowconfigure(5, weight = 1)
        self.grid_rowconfigure(6, weight = 1)
        self.grid_rowconfigure(7, weight = 1)"""
        
class AddEdit(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Title: ",
                                  font = ("Courier", 12))
        self.lbl_title.grid(row = 0,
                            column = 0,
                            sticky = "news")
        
        self.lbl_genre = tk.Label(self, text = "Genre: ",
                             font = ("Courier", 12))
        self.lbl_genre.grid(row = 1,
                       column = 0,
                            sticky = "news")
        
        self.lbl_dir = tk.Label(self, text = "Director(s): ",
                           font = ("Courier", 12))
        self.lbl_dir.grid(row = 2,
                       column = 0,
                            sticky = "news")        
        
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 0, 
                       column = 1,
                       columnspan = 3,
                            sticky = "news")
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 1, 
                       column = 1,
                       columnspan = 3,
                            sticky = "news")
        
        self.ent_dir = tk.Entry(self)
        self.ent_dir.grid(row = 2, 
                       column = 1,
                       columnspan = 3,
                            sticky = "news")  
        
        self.lbl_releaseyr = tk.Label(self, text = "Release Year: ",
                                 font = ("Courier", 12))
        self.lbl_releaseyr.grid(row = 3,
                           column = 0,
                            sticky = "news")
        
        self.ent_releaseyr = tk.Entry(self)
        self.ent_releaseyr.grid(row = 3, 
                           column = 1,
                            sticky = "news")
        
        self.lbl_rate = tk.Label(self, text = "Viewer Rating: ",
                            font = ("Courier", 12))
        self.lbl_rate.grid(row = 3,
                      column = 2,
                            sticky = "news")        
        
        self.ent_rate = tk.Entry(self)
        self.ent_rate.grid(row = 3,
                      column = 3,
                            sticky = "news")
        
        self.lbl_1star = tk.Label(self, text = "Star Rating",
                             font = ("Courier", 12))
        self.lbl_1star.grid(row = 4, 
                       column = 0,
                            sticky = "news")
        
        self.ent_stars = tk.Entry(self)
        self.ent_stars.grid(row = 4,
                       column  = 1,
                            sticky = "news")
        
        self.lbl_2star = tk.Label(self, text = "/10",
                             font = ("Courier", 12))
        self.lbl_2star.grid(row = 4,
                       column = 2,
                            sticky = "news")
        
        self.lbl_tb = tk.Label(self, text = "Top-Billed: ",
                          font = ("Courier", 12))
        self.lbl_tb.grid(row = 5,
                    column = 0,
                            sticky = "news")
        
        self.ent_tb = tk.Entry(self)
        
        self.ent_tb.grid(row = 6, 
                    column = 0,
                            sticky = "news")
        
        self.lbl_sb = tk.Label(self, text = "Second-Billed: ",
                          font = ("Courier", 12))
        self.lbl_sb.grid(row = 7,
                    column = 0,
                            sticky = "news")
        
        self.ent_sb = tk.Entry(self)
        
        self.ent_sb.grid(row = 8, 
                    column = 0,
                            sticky = "news")
        
        self.lbl_thb = tk.Label(self, text = "Third-Billed: ",
                          font = ("Courier", 12))
        self.lbl_thb.grid(row = 9,
                    column = 0,
                            sticky = "news")
        
        self.ent_thb = tk.Entry(self)
        
        self.ent_thb.grid(row = 10, 
                    column = 0,
                            sticky = "news")        
        
        self.scrtxt = ScrolledText(self, height = 8,
                                  width = 40)
        self.scrtxt.grid(row = 5,
                    rowspan = 6,
                    column = 2,
                    columnspan = 2,
                            sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Back", 
                             font = ("Courier", 12))
        self.btn_back.grid(row = 11,
                      column = 0,
                            sticky = "news")
        
        self.btn_reset = tk.Button(self, text = "Reset", 
                             font = ("Courier", 12))
        self.btn_reset.grid(row = 11,
                      column = 2,
                            sticky = "news") 
        
        self.btn_submit = tk.Button(self, text = "Submit", 
                             font = ("Courier", 12))
        self.btn_submit.grid(row = 11,
                        column = 3,
                            sticky = "news") 
        
        self.grid_columnconfigure(0, weight = 3)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 2)
        self.grid_columnconfigure(3, weight = 2)
        
        
class Remove(tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        
        self.lbl_rem1 = tk.Label(self, text = "These titles are ",
                            font = ("Times", "35"))
        self.lbl_rem1.grid(row = 0,
                      column = 0, 
                      columnspan = 2)
        self.lbl_rem2 = tk.Label(self, text = "marked for removal!",
                                 font = ("Times", "35"))
        self.lbl_rem2.grid(row = 1, 
                           column = 0, 
                           columnspan = 2)
        
        self.scrtxt = ScrolledText(self, height = 8,
                                   width = 40)
        self.scrtxt.grid(row = 2, 
                         column = 0,
                         columnspan = 2)  
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                    font = ("Times", "35"))
        
        self.btn_cancel.grid(row = 3, 
                             column = 0)
        
        self.btn_conf = tk.Button(self, text = "Confirm",
                                  font = ("Times", "35"))
        
        self.btn_conf.grid(row = 3,
                           column = 1)
   
class ChkBoxes(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, master = parent)
        
        self.lbl_pf = tk.Label(self, text = "Print Filters: ",
                               font = ("Times", 15))
        self.lbl_pf.grid(row = 0, 
                    column = 0, 
                    columnspan = 2)        
        
        self.chk1 = tk.Checkbutton(self, text = "Title",
                                   font = ("Times", 15))
        self.chk1.grid(row = 1, 
                  column = 0)
        
        self.chk2 = tk.Checkbutton(self, text = "Genre",
                                   font = ("Times", 15))
        self.chk2.grid(row = 2, 
                  column = 0)
        
        self.chk3 = tk.Checkbutton(self, text = "Director",
                                   font = ("Times", 15))
        self.chk3.grid(row = 3, 
                  column = 0)
        
        self.chk4 = tk.Checkbutton(self, text = "Viewer Rating",
                                   font = ("Times", 15))
        self.chk4.grid(row = 1, 
                  column = 1)
        
        self.chk5 = tk.Checkbutton(self, text = "Star Rating",
                                   font = ("Times", 15))
        self.chk5.grid(row = 2, 
                  column = 1)
        
        self.chk6 = tk.Checkbutton(self, text = "Release Year",
                                   font = ("Times", 15))
        self.chk6.grid(row = 3, 
                  column = 1)  
        
        self.chk7 = tk.Checkbutton(self, text = "Top-Billed",
                                   font = ("Times", 15))
        self.chk7.grid(row = 4, 
                  column = 0)
        

        
#FUNCTIONS-----------------------------------------------------------------

#MAIN-----------------------------------------------------------------------
if __name__ == "__main__":
    
    in_file = open("movie_lib.pickle", "rb")
    movies = p.load(in_file)  
    in_file.close()
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry('1000x600')
    root.title("Movie Library NG")
    
    main_menu = Search()
    main_menu.grid(row = 0, column = 0, sticky = "news") 
    root.grid_columnconfigure(0, weight = 1)

    
    root.mainloop()           