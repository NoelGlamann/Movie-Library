#!/usr/bin/python3
#Noel Glamann
#22 January 2020

''' this is going to be used to develop my own program 
following in the footsteps of our example with big_brother.py.'''

'''last updated: Jan 30, 2020'''

#---IMPORT-------------------------------------------

import pickle as p

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
    print()
    print()    
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
    
    key_list = movies.keys()
    
    for key in key_list:
        info = movies[key]
        actors = info[3]
        
        print()
        print(info[1])
        print()
        print("    Genre:", info[0])
        print("    Director(s):", info[2])
        print("    Top 3 Billed Actors:", actors[0] + 
              ",\n                        ", actors[1] + 
              ",\n                        ", "and", actors[2])
        print("    Release Year:", info[4])
        print("    Rating:", info[5])
        print("    IMDb Star Rate:", info[6] + "/10")
        #print("    Description:", info[7])
        print("----------------------")        
    
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
    D. Director
    E. Release Year
    F. Rating (G, PG, etc)
    G. Star - Rating (5/10, etc
    
    R. Return
    ''')
    
    search_by = input("How would you like to search? ")
    
    if search_by == 'A' or search_by == 'a':
        sb_title()
    elif search_by == 'B' or search_by == 'b':
        sb_genre()
    elif search_by == 'C' or search_by == 'c':
        sb_tb()
    elif search_by == 'D' or search_by == 'd':
        sb_director()        
    elif search_by == 'E' or search_by == 'e':
        sb_year()
    elif search_by == 'F' or search_by == 'f':
        sb_rating()
    elif search_by == 'G' or search_by == 'g':
        sb_stars()     
        
    elif search_by == 'R' or search_by == 'r':
        reset()
        
    else:
        print("*NOT A VALID CHOICE*")
        search()
        
#search

#by

def sb_title():
    
    '''this function allows user to seach library by title'''
    
    print()
    title = input("Keyword (Begin With Capital Letter) ? ")
    key_list = movies.keys()
    
    print("Here is what we found: ")
    print()
    
    count = 0
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        if title in info[1]:
            count += 1
            
            printrecord(info, actors)
            
    if count == 0:
        print("Sorry! We cannot find a title to match your search.")
        
    answer = input("Would you like to try again? (y/N): ")
    
    if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
        search()
    else:
        reset() 
        
        
    
    
def sb_genre():
    
    '''this function allows user to seach library by genre'''
    
    print()
    genre = input("Please type genre: ")
    key_list = movies.keys()
    usr_genre = genre.upper()
  
    
    print("Here is what we found: ")
    print()
    
    count = 0 
    
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        dic_genre = info[0].upper()  
        
        if usr_genre == dic_genre:
            count += 1
            
            printrecord(info, actors)
        
    if count == 0:
        print("Sorry! Our movie genre's do not match your search. ")
        
    answer = input("Would you like to try again? (y/N): ")
    
    if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
        search()
    else:
        reset()         

    
def sb_tb():
    
    '''this function allows user to seach library by 
    top-billed cast'''
    
    print('''To search by actors, please type their name with a capital letter.
             First and/or Last names are available.''')
    actor = input("Name? ")
    
    key_list = movies.keys()
    
    print() 
    print("Here is what we found: ")
    print()    
     
    for key in key_list:
        
        count = 0 
        
        info = movies[key]
        actors = info[3]
        first = actors[0]
        second = actors[1]
        third = actors[2]
        
        if actor in first:
            count += 1
            
            printrecord(info, actors)
            
        if actor in second:
            count += 1
            
            printrecord(info, actors)
            
        if actor in third:
            count += 1
            
            printrecord(info, actors)       
        
    if count == 0:
        print("Sorry! That actor was not top-billed in any of our movies.")
        
        answer = input("Would you like to try again? (y/N): ")
    
        if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
            search()
        else:
            reset()             


def sb_director():
    
    '''This function will search for a movie with director'''
    
    print()
    director = input("Name? ")
    key_list = movies.keys()
    
    print("Here is what we found: ")
    print()
    
    count = 0
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        if director in info[2]:
            count += 1
            
            printrecord(info, actors)
            
    if count == 0:
        print("Sorry! We cannot find a movie directed by your search.")
        
    answer = input("Would you like to try again? (y/N): ")
    
    if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
        search()
    else:
        reset()     
   
def sb_year():
    ''' this function allows user to input a release year
    and all movies released in that year will be displayed'''
    print()
    year = input("What year was the movie released? ")
    
    key_list = movies.keys()
    
    print("Here is what we found: ")
    print()
    
    count = 0
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        if year in info[4]:
            count += 1
            
            printrecord(info, actors)
            
    if count == 0:
        print("Sorry! We cannot find a movie released that year. ")
        
    answer = input("Would you like to try again? (y/N): ")
    
    if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
        search()
    else:
        reset()
        
      
def sb_rating():
    '''this function allows user to input a viewer rating
    such as pg or pg-13 etc and will display all movies with
    that rating'''
    
    print()
    rate = input("Viewer Rating? ")
    usr_rate = rate.upper()
    
    key_list = movies.keys()
    
    print("Here is what we found: ")
    print()
    
    count = 0
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        dic_rate = info[5].upper() 
        
        if usr_rate == dic_rate:
            count += 1
            
            printrecord(info, actors)
            
    if count == 0:
        print("Sorry! We cannot find a movie released that year. ")
        
    answer = input("Would you like to try again? (y/N): ")
    
    if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
        search()
    else:
        reset()    
    
def sb_stars():
    
    '''this function allows user to seach by star rating
    the user can input their smallest number of stars / 10
    and the program will display all with that number or more. '''
    
    print()
    star_rate = input("Minimum number of stars (out of 10) ? ")
    key_list = movies.keys()
    usr_stars = float(star_rate)
    
    print("Here is what we found: ")
    print()
    
    count = 0
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        dic_stars = float(info[6])
        
        if usr_stars <= dic_stars:
            count += 1
            
            printrecord(info, actors)
            
            
    if count == 0:
        print("Sorry! We have no movies rated so high. ")
        
    answer = input("Would you like to try again? (y/N): ")
    
    if answer == 'YES' or answer == 'yes' or answer == 'Y' or answer == 'y':
        search()
    else:
        reset()     
        
def printrecord(info, actors):
    print()
    print(info[1])
    print()
    print("    Genre:", info[0])
    print("    Director(s):", info[2])
    print("    Top 3 Billed Actors:", actors[0] + 
          ",\n                        ", actors[1] + 
          ",\n                        ", "and", actors[2])
    print("    Release Year:", info[4])
    print("    Rating:", info[5])
    print("    IMDb Star Rate:", info[6])
    #print("    Description:", info[7])
    print("----------------------")   

 
    print() 
    
    return
#done 

#with 

#search 

#by

def add():

    
    '''this function allows user to add new movie'''
    print()
    print("Add New Movie")
    print()
    
    title = input("Title of Movie: ")
    
    key_list = movies.keys()
    for key in key_list:
        
        info = movies[key]
        
        if title == info[1]:
            print("This movie already exists in our library.")
            reset()
        
    num = len(movies.keys())
    this_key = num + 1
    
    genre = input("Genre: ")
    director = input("Director: ")
    actor1 = input("Top-Billed Actor: ")
    actor2 = input("Second-Billed Actor: ")
    actor3 = input("Third Billed Actor: ")
    year = input("Release Year: ")
    rating = input("Viewer Rating: ")
    star = input("Star Rating (out of 10): ")
    
    print()
    print("------------------------------------------")
    print(title)
    print(genre)
    print(director)
    print(actor1 + ", " + actor2 + ", and " + actor3)
    print(year)
    print(rating)
    print(star)
    print("------------------------------------------")
    print()
    
    answer = input("Is this information correct (Y/n)? ")
    
    if answer == "N" or answer == "NO" or answer == "n" or answer == "no":
        ans = input("Would you like to try again (Y/n)? ")
        
        if ans == "N" or ans == "NO" or ans == "n" or ans == "no": 
            reset()
        else:
            add()
    else:
        movies[this_key] = [genre, title, director, [actor1, actor2, actor3], year, rating, star] 
        save(False)
    
def edit():
    
    '''this function allows user to edit existing movie'''
    print("Editing an Existing Function")
    print()
    print("Here is your library: ")
    print()
    
    count = 1
    while count <= len(movies):
        contains = movies[count]
        movie_title = contains[1]
        num = str(count)
        
        print(num + ". " + movie_title)
        count += 1 
      
    print()
    number = input("Which movie would you like to edit (1, 2, 3)? ")
    this_key = int(number)
    print()
    
    info = movies[this_key]
    actors = info[3]
    
    print("Current Title:", info[1])
    title = input("New Title: ")
    print()
    print("Current Genre:", info[0])
    genre = input("New Genre: ")
    print()
    print("Current Director(s):", info[2])
    director = input("New Director: ")
    print()
    print("Current Top-Billed Actor:", actors[0])
    actor1 = input("New Actor: ")
    print()
    print("Current Second-Billed Actor:", actors[1])
    actor2 = input("New Actor: ")
    print()
    print("Current Third-Billed Actor:", actors[2])
    actor3 = input("New Actor: ")
    print()    
    print("Current Release Year:", info[4])
    year = input("New Year: ")
    print()  
    print("Current Viewer Rating:", info[5])
    rating = input("New Rating: ")
    print()  
    print("Current Star Rating:", info[6] + "/10")
    star = input("New Rating (out of 10): ")
    
    print()  
    print()  
    print()
    print("------------------------------------------")
    print(title)
    print(genre)
    print(director)
    print(actor1 + ", " + actor2 + ", and " + actor3)
    print(year)
    print(rating)
    print(star)
    print("------------------------------------------")
    print()
    
    answer = input("Is this information correct (Y/n)? ")
    
    if answer in ("N", "NO", "n", "no"):
        ans = input("Would you like to try again (Y/n)? ")
        
        if ans in ("N", "NO", "n", "no"):
            reset()
        else:
            add()
    else:
        movies[this_key] = [genre, title, director, [actor1, actor2, actor3], year, rating, star] 
        save(False)       
    
    
def remove():
    
    '''this function will remove an existing movie from 
    the database'''
    
    title = input("Title of movie to delete: ")
    found = False
    key_list = movies.keys()
    
    for key in key_list:
        
        info = movies[key]
        actors = info[3]
        
        if title in info[1]:
            found = True
    
    key = title.keys()
    print(key)
            
    if found:
        entry = movies.pop(title)
        print(title, "was", "removed.")
              
    else:
        print("That movie was not found in our library.")
         
    save(False)
    
def save(exit):
    
    '''this fuction will serve as both a save and an exit function
    depending on the user's menu selection. '''
    dictionary = movies
    save = open("movie_lib.pickle", "wb")
    p.dump(dictionary, save)
    save.close() 
    
    
    if exit:
        return
    else:
        reopen = open("movie_lib.pickle", "rb")
        dictionary = p.load(reopen)  
        reopen.close()
        print("Save Complete!")
        #movies = dictionary 
        
        reset()
        
    
    
def reset():
    
    ''' this function reset's the screen so the program is easier to read'''
    
    print()
    print()
    print()
    print()
    print()
    menu()

    
    

#---MAIN PROGRAM-------------------------------------

movies = {}
in_file = open("movie_lib.pickle", "rb")
movies = p.load(in_file)  
in_file.close()
'''print(movies)'''

menu()

print("Goodbye --------")


'''
TODO

Search by top billed does not work!!

I would like to add a way for the user to select how to sort the display
ex. display sorted by genre, alphebetical, etc

'''