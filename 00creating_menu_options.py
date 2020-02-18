#!/usr/bin/python3
#Noel Glamann
#22 January 2020

''' this is going to be used to develop my own program 
following in the footsteps of our example with big_brother.py.'''

#---IMPORT-------------------------------------------



#---FUNCTIONS----------------------------------------

def menu():
    print('''
              MOVIE DATABASE
                MAIN MENU
            ------------------
            
    1. Display All
    2. Search Library
    3. Add New Movie
    4. Edit Existing Movie
    5. Remove Existing Movie
    6. Save Database
    
    Q. Quit ( also saves )
    ''')
    choice = input("Select the option by number (1, 2, 3) or letter (Q): ")
    selection(choice)    

def selection(choice):
    if choice == '1':
        display()
    elif choice == '2':
        search()
    elif choice == '3':
        add()
    elif choice == '4':
        edit()
    elif choice == '5':
        remove()
    elif choice == '6':
        save(False)
    elif choice == 'Q' or choice == 'q':
        save(True)
    else:
        print("*NOT A VALID CHOICE*")
        menu()
        
def display():
    
    '''this function will display all items existing 
    in the library. 
    I would like to implement a sort option.'''
    
    print("DISPLAY")
    reset()
    
def search():
    
    '''this function will allow the user to search
    the database with their own key'''
    
    print('''
     SEARCH BY:
    ------------
    
    A. Title
    B. Genre
    C. Top-Billed Actor/Actress
    
    R. Return
    ''')
    
    search_by = input("How would you like to search? ")
    
    if search_by == 'A' or search_by == 'a':
        sb_title()
    elif search_by == 'B' or search_by == 'b':
        sb_genre()
    elif search_by == 'C' or search_by == 'c':
        sb_tb()
    elif search_by == 'R' or search_by == 'r':
        reset()
    else:
        print("*NOT A VALID CHOICE*")
        search()
        
        

def sb_title():
    
    '''this function allows user to seach library by title'''
    print("search by title")
    reset()
    
def sb_genre():
    
    '''this function allows user to seach library by genre'''
    print("search by genre")
    reset()
    
def sb_tb():
    
    '''this function allows user to seach library by 
    top-billed cast'''
    print("search by top-billed")
    reset()

   
def add():
    
    '''this function allows user to add new movie'''
    print("Add New")
    update()
    
def edit():
    
    '''this function allows user to edit existing movie'''
    print("Edit")
    update()
    
def update():
    
    '''this function exists to complete edit() and add()'''
    print("Update")
    reset()
    
def remove():
    
    '''this function will remove an existing movie from 
    the database'''
    
    print("Remove")
    reset()
    
def save(exit):
    
    '''this function will save the database without making the
    user exit and reopen the program'''
    
    print("Save")
    
    if exit:
        quit()
    else:
        reset()
    
    
    
def reset():
    
    ''' this function reset's the screen so the program is easier to read'''
    
    print()
    print()
    print()
    print()
    print()
    menu()
    
def quit():
    
    '''this function will quit the program'''
    
    print("Quit")
    return
    
    

#---MAIN PROGRAM-------------------------------------

menu()

print("Goodbye --------")


'''
TODO

I would like to add a way for the user to select how to sort the display
ex. display sorted by genre, alphebetical, etc
'''
