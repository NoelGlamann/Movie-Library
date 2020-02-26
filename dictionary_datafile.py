#!/usr/bin/python3
#Noel Glamann
#28 January 2020

''' data file for movie library file '''

import pickle as p


'''just so i do not forget:
          the list following the # key in the dictionary is-
          
          0. Genre
          1. Title
          2. Director(s)
          3. Top 3 Actors/Actress'
          4. Year Released
          5. Rating
          6. IMDb Star Rate
          7. Notes/Description
        
'''

movies = {1:['Horror', 
           'Bye Bye Man, The', 
           'Stacy Title', 
           ['Douglas Smith (Elliot)', 'Lucien Laviscount(John)', 'Cressida Bonas (Sasha)'], 
           '2017', 
           'PG-13', 
           '4.2',
           'Good Movie. A couple jump scares. Nothing too bloody.'], 
          2:['Romance', 
            'Notebook, The', 
            'Nick Cassavetes', 
            ['Ryan Gosling (Noah)', 'Rachel McAdams (Allie)', 'James Marsden (Lon)'], 
            '2004', 
            'PG-13', 
            '7.8',
            'Classic love story. Older man tells women with alzeimers their love story.'],
          3:['Adventure',
            'Big Hero 6',
            'Don Hall and Chris Williams',
            ['Scott Adsit (Baymax - Voice)', 'Ryan Potter (Hiro - Voice)', 'Daniel Henney (Tadashi - Voice)'],
            '2014',
            'PG',
            '7.8',
            'Good animation. Band of teens and inflatabe robot. Humorous.'],
          4:['Fantasy', 
            'Nightmare Before Christmas, The', 
            'Henry Selick',
            ['Danny Elfman (Jack Skellington - Singing Voice/Clown with Tear-Away Face)', 'Chris Sarandon (Jack Skellington - Voice)', 'Catherine OHara (Sally/Shock - Voice)'],
            '1993',
            'PG',
            '8.0',
            'Best Christmas Movie Ever. Best Halloween Movie Ever. Good music, good animation, good story.'],
          5:['Horror',
            'Ring, The',
            'Gore Verbinski',
            ['Naomi Watts (Rachel)', 'Martin Henderson (Noah)', 'David Dorfman (Aidan)'],
            '2002',
            'PG-13',
            '7.1',
            'Really good scary movie. If a person watches this short cursed video, they will die in seven days.'],
          6:['Adventure',
            'Frozen',
            'Chris Buck and Jennifer Lee',
            ['Kristen Bell (Anna - Voice)', 'Idina Menzel (Elsa - Voice)', 'Jonathan Groff (Kristoff - Voice)'],
            '2013',
            'PG',
            '7.5',
            'Disney musical, great story!'],
          7:['Comedy',
             'Heat, The',
             'Paul Feig',
             ['Sandra Bullock (Ashburn)', 'Melissa McCarthy (Mullins)', 'Michael McDonald (Julian)'],
             '2013',
             'R',
             '6.6',
             'Slightly bloody and violent, but mostly funny.'],
          8:['Horror',
             'Forest, The',
             'Jason Zada',
             ['Natalie Dormer (Sara/Jess Price)', 'Eoin Macken (Rob)', 'Stephanie Vogt (Valerie)'],
             '2016',
             'PG-13',
             '4.8',
             'Girl searches for twin sister that disappeared in the haunted Japanese suicide forest.'],
          9:['Adventure',
             'Aladdin',
             'Ron Clements and John Musker',
             ['Scott Weinger (Aladdin - Voice)', 'Robin Williams (Genie/Peddler - Voice)', 'Linda Larkin (Princess Jasmine - Voice)'],
             '1992',
             'G',
             '8.0',
             'Best Disney movie ever made.'],
          10:['Drama',
              'Help, The',
              'Tate Taylor',
              ['Emma Stone (Skeeter Phelan)', 'Viola Davis (Aibileen Clark)', 'Octavia Spencer (Minny Jackson)'],
              '2011',
              'PG-13',
              '8.1',
              'Good movie. Have not seen in a while'],
          11:['Comedy',
              'Murder Mystery',
              'Kyle Newacheck',
              ['Adam Sandler (Nick Spitz)', 'Jennifer Aniston (Audrey Spitz)', 'Luke Evans (Charles Cavendish)'],
              '2019',
              'PG-13',
              '6.0',
              'Really funny murder mystery couple ends up involved in while on vacation.'],
          12:['Drama',
              'Burlesque',
              'Steve Antin',
              ['Cher (Tess)', 'Christina Aguilera (Ali)', 'Cam Gigandet (Jack)'],
              '2010',
              'PG-13',
              '6.4',
              'Musical/Drama about girl with nothing starring in burlesque lounge.'],
          13:['Musical',
              'Mamma Mia!',
              'Phyllida Lloyd',
              ['Amanda Seyfried (Sophie)', 'Meryl Streep (Donna)', 'Pierce Brosnan (Sam)'],
              '2008',
              'PG-13',
              '6.4',
              'Wonderful story, wonderful music.'],
          14:['Musical',
              'Mamma Mia! Here We Go Again',
              'Ol Parker',
              ['Lily James (Young Donna)', 'Amanda Seyfried (Sophie)', 'Meryl Streep (Donna)'],
              '2018',
              'PG-13',
              '6.7',
              'Mamma Mia part 2'],
          15:['Comedy',
              'Devil Wears Prada, The',
              'David Frankel',
              ['Meryl Streep (Miranda Priestly)', 'Anne Hathaway (Andy Sachs)', 'Stanley Tucci (Nigel)'],
              '2006',
              'PG-13',
              '6.9',
              'Really good movie. Have not seen in a while.']}

datafile = open('movie_lib.pickle', 'wb')
p.dump(movies, datafile)
datafile.close()

