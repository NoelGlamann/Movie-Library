#!/usr/bin/python3
#Noel Glamann
#28 January 2020

''' data file for movie library file '''

import pickle as p


'''just so i do not forget:
          the list following the # key in the dictionary is-
          
          1. Genre
          2. Title
          3. Director(s)
          4. Top 3 Actors/Actress'
          5. Year Released
          6. Rating
          7. IMDb Star Rate
          8. Notes/Description
          
'''

movies = {1:['Horror', 
           'The Bye Bye Man', 
           'Stacy Title', 
           ['Douglas Smith (Elliot)', 'Lucien Laviscount(John)', 'Cressida Bonas (Sasha)'], 
           '2017', 
           'PG-13', 
           '4.2/10'], 
          2:['Romance', 
            'The Notebook', 
            'Nick Cassavetes', 
            ['Ryan Gosling (Noah)', 'Rachel McAdams (Allie)', 'James Marsden (Lon)'], 
            '2004', 
            'PG-13', 
            '7.8/10'],
          3:['Adventure',
            'Big Hero 6',
            'Don Hall and Chris Williams',
            ['Scott Adsit (Baymax - Voice)', 'Ryan Potter (Hiro - Voice)', 'Daniel Henney (Tadashi - Voice)'],
            '2014',
            'PG',
            '7.8/10'],
          4:['Fantasy', 
            'The Nightmare Before Christmas', 
            'Henry Selick',
            ['Danny Elfman (Jack Skellington - Singing Voice/Clown with Tear-Away Face)', 'Chris Sarandon (Jack Skellington - Voice)', 'Catherine OHara (Sally/Shock - Voice)'],
            '1993',
            'PG',
            '8.0/10'],
          5:['Horror',
            'The Ring',
            'Gore Verbinski',
            ['Naomi Watts (Rachel)', 'Martin Henderson (Noah)', 'David Dorfman (Aidan)'],
            '2002',
            'PG-13',
            '7.1/10'],
          6:['Adventure',
            'Frozen',
            'Chris Buck and Jennifer Lee',
            ['Kristen Bell (Anna - Voice)', 'Idina Menzel (Elsa - Voice)', 'Jonathan Groff (Kristoff - Voice)'],
            '2013',
            'PG',
            '7.5/10']}

datafile = open('movie_lib.pickle', 'wb')
p.dump(movies, datafile)
datafile.close()

