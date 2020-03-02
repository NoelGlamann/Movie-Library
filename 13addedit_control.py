#!usr/bin/python3
#Noel Glamann
#25 February 2020

'''
This program will develop the Graphical User 
Interface (GUI) for the Movie Library function. 
          
This file last updated: 02 March 2020
          
'''

#IMPORTS-------------------------------------------------------------------
import pickle as p
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

#CONSTANTS-----------------------------------------------------------------


#CLASSES-------------------------------------------------------------------

class Screen(tk.Frame):
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
    def main():
        Screen.current = 0
        Screen.switch_frame()     
    
    
class MainMenu(Screen):
    def __init__(self):
        '''This function creates a main menu for the database,
        inlcuding positioning and jobs of widgets'''
        
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Movie Database",
                             font = ("Times", "50"))
        self.lbl_title.grid(row = 0, 
                       column = 0, 
                       columnspan = 3,
                       sticky = "news")
        
        self.btn_add = tk.Button(self, text = "Add New Movie",
                                 command = self.addedit,
                                 font = ("Courier", "16"))
        self.btn_add.grid(row = 2, 
                     column = 1, 
                       sticky = "news")
        
        self.btn_edit = tk.Button(self, text = "Edit Existing Movie",
                                  command = self.checkedit,
                                  font = ("Courier", "16"))
        self.btn_edit.grid(row = 3, 
                      column = 1, 
                       sticky = "news")
        
        self.btn_search = tk.Button(self, text = "Search Library",
                                    command = self.search,
                                    font = ("Courier", "16"))
        self.btn_search.grid(row = 4, 
                        column = 1, 
                       sticky = "news")
        
        self.btn_remove = tk.Button(self, text = "Remove Existing",
                                    command = self.checkremove,
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
        
    '''Frames'''
    def search(self):
        Screen.current = 1
        Screen.switch_frame()
    def addedit(self):
        Screen.current = 2
        screens[Screen.current].ent_genre.delete(0,"end")
        screens[Screen.current].ent_title.delete(0,"end")
        screens[Screen.current].ent_director.delete(0,"end")
        screens[Screen.current].ent_1b.delete(0,"end")
        screens[Screen.current].ent_2b.delete(0,"end")
        screens[Screen.current].ent_3b.delete(0,"end")
        screens[Screen.current].ent_releaseyr.delete(0,"end")
        screens[Screen.current].ent_viewrate.delete(0,"end")        
        screens[Screen.current].ent_starnum.delete(0,"end")
        screens[Screen.current].scr_notes.delete(0.0, "end")
        screens[Screen.current].edit_key = 0
        Screen.switch_frame()
        
    '''Pop Ups'''   
    def checkedit(self):
        popup = tk.Tk()
        popup.title("Edit Select")
        frm_checkedit = CheckEdit(popup)
        frm_checkedit.grid(row = 0, column = 0)
    def checkremove(self):
        popup = tk.Tk()
        popup.title("Remove Select")
        frm_checkremove = CheckRemove(popup)
        frm_checkremove.grid(row = 0, column = 0)
        
class Search(Screen):
    '''This Frame will be the Print All/Search By page'''
    
    def __init__(self):
        Screen.__init__(self)        
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
                   sticky = "e")
        
        '''MAKE DROP DOWN'''
        
        self.tkvar = tk.StringVar(self)
        
        self.choices = ['Title', 'Genre', 'Director', 
                        'Top-Billed Actors', 'Release Year', 
                        'Viewer Rating', 'Star Rating']
        
        self.tkvar.set('Title')
        
        self.dbx_searchby = tk.OptionMenu(self, self.tkvar, *self.choices)
        
        self.dbx_searchby.grid(row = 2, 
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
                   sticky = "e")
        
        self.ent_sf = tk.Entry(self)
        
        self.ent_sf.grid(row = 5,
                    column = 0,
                    #columnspan = 2,
                   sticky = "news")
        
        self.scr_movielist = ScrolledText(self, height = 10,
                                          width = 20)
        
        self.scr_movielist.grid(row = 6, 
                                column = 0,
                                columnspan = 3,
                                sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Back",
                                  command = Screen.main,
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
        
        #self.grid_columnconfigure(0, weight = 1)
               
        
        
class AddEdit(Screen):
    
    def __init__(self):
        
        Screen.__init__(self)        
        
        self.edit_key = 0
        
        
        self.lbl_title = tk.Label(self, text = "Title: ",
                                  font = ("Courier", 12))
        
        self.lbl_title.grid(row = 0,
                            column = 0,
                            sticky = "e")
        
        self.lbl_genre = tk.Label(self, text = "Genre: ",
                                  font = ("Courier", 12))    
        
        self.lbl_genre.grid(row = 1,
                            column = 0,
                            sticky = "e")
        
        self.lbl_director = tk.Label(self, text = "Director(s): ",
                                     font = ("Courier", 12))
        
        self.lbl_director.grid(row = 2,
                               column = 0,
                               sticky = "e")        
        
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
        
        self.ent_director = tk.Entry(self)
        
        self.ent_director.grid(row = 2, 
                               column = 1,
                               columnspan = 3,
                               sticky = "news")  
        
        self.lbl_releaseyr = tk.Label(self, text = "Release Year: ",
                                      font = ("Courier", 12))
        
        self.lbl_releaseyr.grid(row = 3,
                                column = 0,
                                sticky = "e")
        
        self.ent_releaseyr = tk.Entry(self)
        
        self.ent_releaseyr.grid(row = 3, 
                                column = 1,
                                sticky = "news")
        
        self.lbl_viewrate = tk.Label(self, text = "Viewer Rating: ",
                                     font = ("Courier", 12))
        
        self.lbl_viewrate.grid(row = 3,
                               column = 2,
                               sticky = "e")        
        
        self.ent_viewrate = tk.Entry(self)
        
        self.ent_viewrate.grid(row = 3,
                               column = 3,
                               sticky = "news")
        
        self.lbl_1star = tk.Label(self, text = "Star Rating",
                                  font = ("Courier", 12))
        
        self.lbl_1star.grid(row = 4, 
                            column = 0,
                            sticky = "e")
        
        self.ent_starnum = tk.Entry(self)
        
        self.ent_starnum.grid(row = 4,
                              column  = 1,
                              sticky = "news")
        
        self.lbl_2star = tk.Label(self, text = "/10",
                             font = ("Courier", 12))
        
        self.lbl_2star.grid(row = 4,
                            column = 2,
                            sticky = "w")
        
        self.lbl_1b = tk.Label(self, text = "Top-Billed: ",
                               font = ("Courier", 12))
        
        self.lbl_1b.grid(row = 5,
                         column = 0,
                         sticky = "w")
        
        self.ent_1b = tk.Entry(self)
        
        self.ent_1b.grid(row = 6, 
                         column = 0,
                         sticky = "news")
        
        self.lbl_2b = tk.Label(self, text = "Second-Billed: ",
                               font = ("Courier", 12))
        
        self.lbl_2b.grid(row = 7,
                         column = 0,
                         sticky = "w")
        
        self.ent_2b = tk.Entry(self)
        
        self.ent_2b.grid(row = 8, 
                         column = 0,
                         sticky = "news")
        
        self.lbl_3b = tk.Label(self, text = "Third-Billed: ",
                               font = ("Courier", 12))
        
        self.lbl_3b.grid(row = 9,
                         column = 0,
                         sticky = "w")
        
        self.ent_3b = tk.Entry(self)
        
        self.ent_3b.grid(row = 10, 
                         column = 0,
                         sticky = "news")   
        
        '''scrolled text bar for notes'''
        
        self.scr_notes = ScrolledText(self, 
                                      wrap = 'word', #wrap text at full words only 
                                      height = 8,    
                                      width = 40)
        self.scr_notes.grid(row = 5,
                            rowspan = 6,
                            column = 1,
                            columnspan = 3,
                            sticky = "news")
        
        mytext = '''
        '''
        
        self.scr_notes.insert('insert', mytext)
        
        self.btn_back = tk.Button(self, text = "Back",
                                  command = self.go_back, 
                                  font = ("Courier", 12))
        self.btn_back.grid(row = 11,
                           column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset",
                                   command = self.reset,
                                   font = ("Courier", 12))
        self.btn_reset.grid(row = 11,
                            column = 2) 
        
        self.btn_submit = tk.Button(self, text = "Submit", 
                                    command = self.submit,
                                    font = ("Courier", 12))
        self.btn_submit.grid(row = 11,
                             column = 3) 
        
        self.grid_columnconfigure(0, weight = 3)
        
        
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_rowconfigure(4, weight = 1)
        self.grid_rowconfigure(5, weight = 1)
        self.grid_rowconfigure(6, weight = 1)
        self.grid_rowconfigure(7, weight = 1)
        self.grid_rowconfigure(8, weight = 1)
        self.grid_rowconfigure(9, weight = 1)
        self.grid_rowconfigure(10, weight = 1)
        self.grid_rowconfigure(11, weight = 1)
        
    def go_back(self):
        '''back button
        removes contents of entry boxes, and goes back to main menu'''      
        Screen.main()
        
    def reset(self):
        '''reset button
        removes contents of entry boxes, and puts back what it was before
        this way if they edit a movie and realize they put the wrong thing - maybe don't remember what
        it should be - they can push reset and get the correct info put back in'''
        self.delete_contents()
        if self.edit_key > 0:
            self.update()
        return
    
    def submit(self):
        '''submit button
        creates a list to contain the new contents of the entry boxes after it's been edited.
        must append in order of my original datafile
        
        ALSO:: In my dictionary definition, one of my items is a list in itself, 
        so I had to make that and then append that list to my dictionary definition list.
        
        then takes list and dictionary key (self.edit_key) and changes the dictionary.'''
        actors = []
        actors.append(self.ent_1b.get())
        actors.append(self.ent_2b.get())
        actors.append(self.ent_3b.get())
        
        entry = []
        entry.append(self.ent_genre.get())
        entry.append(self.ent_title.get())
        entry.append(self.ent_director.get())
        entry.append(actors)
        entry.append(self.ent_releaseyr.get())
        self.delete_contents()  
        entry.append(self.ent_viewrate.get())
        entry.append(self.ent_starnum.get())
        entry.append(self.scr_notes.get(0.0, "end"))
        if self.edit_key > 0:
            movies[self.edit_key] = entry
        else:
            movies[len(movies) + 1] = entry
        Screen.main()       
        
    def delete_contents(self):
        '''removes contents of entry boxes
        too much typing and I didn't want to keep retyping it'''
        self.ent_genre.delete(0,"end")
        self.ent_title.delete(0,"end")
        self.ent_director.delete(0,"end")
        self.ent_1b.delete(0,"end")
        self.ent_2b.delete(0,"end")
        self.ent_3b.delete(0,"end")
        self.ent_releaseyr.delete(0,"end")
        self.ent_viewrate.delete(0,"end")        
        self.ent_starnum.delete(0,"end")
        self.scr_notes.delete(0.0, "end")
        return
        
    def update(self):
        self.delete_contents()  
        '''put in the info of a selected movie
        used coming from checkedit()'''
        entry = movies[self.edit_key]
        self.delete_contents()
        self.ent_genre.insert(0, entry[0])
        self.ent_title.insert(0, entry[1])
        self.ent_director.insert(0, entry[2])
        self.ent_1b.insert(0, entry[3][0])
        self.ent_2b.insert(0, entry[3][1])
        self.ent_3b.insert(0, entry[3][2])
        self.ent_releaseyr.insert(0, entry[4])
        self.ent_viewrate.insert(0, entry[5])
        self.ent_starnum.insert(0, entry[6])
        self.scr_notes.insert(0.0, entry[7])
        
     
        
       
class CheckEdit(tk.Frame):
    def __init__(self, parent):
        
        tk.Frame.__init__(self, master = parent)        
        
        self.parent = parent 
        
        self.lbl_remove1 = tk.Label(self, text = "Which movie would ",
                                    font = ("Times", 30))
        
        self.lbl_remove1.grid(row = 0, 
                              column = 0,
                              columnspan = 2,
                              sticky = "news")
        
        self.lbl_remove2 = tk.Label(self, text = "you like to edit?",
                                    font = ("Times", 30))
        self.lbl_remove2.grid(row = 1, 
                              column = 0,
                              columnspan = 2,
                              sticky ="news")
        
        '''DROP DOWN'''
        self.tkvar = tk.StringVar(self)
        self.movie_choices = ["Select Movie"]
        
        for key in range(1, (len(movies)+1)):
            contents = movies[key]
            self.movie_choices.append(contents[1])
        
        self.tkvar.set(self.movie_choices[0])
        
        self.dbx_movieedit = tk.OptionMenu(self, self.tkvar, *self.movie_choices)
        
        self.dbx_movieedit.grid(row = 2, 
                                  column = 0, 
                                  columnspan = 2,
                                  sticky = "news")  
        '''DD DONE'''
        
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                    command = self.parent.destroy,
                                    font = ("Times", 20))
        
        self.btn_cancel.grid(row = 3,
                             column = 0)
        
        self.btn_continue = tk.Button(self, text = "Continue",
                                      command = self.continue_to_edit,
                                      font = ("Times", 20))
        
        self.btn_continue.grid(row = 3,
                               column = 1)    
        
        
    def continue_to_edit(self):
        if self.tkvar.get() == self.movie_choices[0]:
            self.dbx_movieedit.configure(bg = "red")  
        else:
            Screen.current = 2
            Screen.switch_frame()            
            
            for i in range(len(self.movie_choices)):
                if self.tkvar.get() == self.movie_choices[i]:
                    screens[2].edit_key = i
                    break
                
            screens[2].update()    
            self.parent.destroy()            
        
        
class Remove(Screen):
    
    def __init__(self):
        
        tk.Frame.__init__(self)        
        
        self.lbl_removal1 = tk.Label(self, text = "These titles are ",
                            font = ("Times", "35"))
        self.lbl_removal1.grid(row = 0,
                      column = 1, 
                      columnspan = 2)
        self.lbl_removal2 = tk.Label(self, text = "marked for removal!",
                                 font = ("Times", "35"))
        self.lbl_removal2.grid(row = 1, 
                           column = 1, 
                           columnspan = 2)
        
        self.scr_removelist = ScrolledText(self, height = 8,
                                   width = 40)
        self.scr_removelist.grid(row = 2, 
                         column = 1,
                         columnspan = 2)  
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                    command = Screen.main,
                                    font = ("Times", "25"))
        
        self.btn_cancel.grid(row = 3, 
                             column = 1)
        
        self.btn_conf = tk.Button(self, text = "Confirm",
                                  font = ("Times", "25"))
        
        self.btn_conf.grid(row = 3,
                           column = 2,
                           sticky = "w")
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        
        
        
class CheckRemove(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, master = parent)        
        
        self.lbl_remove1 = tk.Label(self, text = "Which movie would you",
                                    font = ("Times", 30))
        
        self.lbl_remove1.grid(row = 0, 
                              column = 0,
                              columnspan = 2,
                              sticky = "news")
        
        self.lbl_remove2 = tk.Label(self, text = "like to remove?",
                                    font = ("Times", 30))
        self.lbl_remove2.grid(row = 1, 
                              column = 0,
                              columnspan = 2,
                              sticky ="news")
        
        '''DROP DOWN'''
        
        self.tkvar = tk.StringVar(self)
        
        choices = ['movie1', 'movie2', 'movie3']
        
        self.tkvar.set('movie1')
        
        self.dbx_movieremove = tk.OptionMenu(self, self.tkvar, *choices)
        
        self.dbx_movieremove.grid(row = 2, 
                                  column = 0, 
                                  columnspan = 2,
                                  sticky = "news")  
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                    command = self.parent.destroy,
                                    font = ("Times", 20))
        
        self.btn_cancel.grid(row = 3,
                             column = 0)
        
        self.btn_continue = tk.Button(self, text = "Continue",
                                      command = self.removed,
                                      font = ("Times", 20))
        
        self.btn_continue.grid(row = 3,
                               column = 1)    
        
    def continue_to_remove(self):
        Screen.current = 3
        Screen.switch_frame()
        self.parent.destroy()        
        
class Save(Screen):
    def __init__(self):
        
        Screen.__init__(self)
        
        self.lbl_filesaved = tk.Label(self, text = "File Save Success",
                                      font = ("Times", 25))
        
        self.lbl_filesaved.grid(row = 0, column = 0)
        
        self.btn_okay = tk.Button(self, text = "Okay",
                                  font = ("Times", 20))
        
        self.btn_okay.grid(row = 1, column = 0)
   
class ChkBoxes(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, master = parent)
        
        self.lbl_printfilt = tk.Label(self, text = "Print Filters: ",
                               font = ("Times", 20))
        self.lbl_printfilt.grid(row = 0, 
                                column = 0)        
        
        self.chk_1 = tk.Checkbutton(self, text = "Title",
                                   font = ("Times", 15))
        self.chk_1.grid(row = 1, 
                        column = 0,
                        sticky = "w")
        
        self.chk_2 = tk.Checkbutton(self, text = "Genre",
                                    font = ("Times", 15))
        self.chk_2.grid(row = 2, 
                        column = 0,
                        sticky = "w")
        
        self.chk_3 = tk.Checkbutton(self, text = "Director",
                                    font = ("Times", 15))
        self.chk_3.grid(row = 3, 
                        column = 0,
                        sticky = "w")
        
        self.chk_4 = tk.Checkbutton(self, text = "Viewer Rating",
                                    font = ("Times", 15))
        self.chk_4.grid(row = 1, 
                        column = 1,
                        sticky = "w")
        
        self.chk_5 = tk.Checkbutton(self, text = "Star Rating",
                                    font = ("Times", 15))
        self.chk_5.grid(row = 2, 
                        column = 1,
                        sticky = "w")
        
        self.chk_6 = tk.Checkbutton(self, text = "Release Year",
                                    font = ("Times", 15))
        self.chk_6.grid(row = 3, 
                        column = 1,
                        sticky = "w")  
        
        self.chk_7 = tk.Checkbutton(self, text = "Top-Billed",
                                    font = ("Times", 15))
        self.chk_7.grid(row = 4, 
                        column = 0,
                        sticky = "w")
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

#MAIN-----------------------------------------------------------------------
if __name__ == "__main__":
    
    in_file = open("movie_lib.pickle", "rb")
    movies = p.load(in_file)  
    in_file.close()
    
    '''creating a main screen'''
    root = tk.Tk()
    #root.geometry('1000x600')
    root.title("Movie Library NG")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    screens = []
    
    screens.append(MainMenu())   #MainMenu  =  screens[0]    
    screens.append(Search())     #Search    =  screens[1]
    screens.append(AddEdit())    #AddEdit   =  screens[2]
    screens.append(Remove())     #Remove    =  screens[3]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")  
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    
    Screen.current = 0
    Screen.switch_frame()
    
    root.mainloop()           