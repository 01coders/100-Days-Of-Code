#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:01:23 2019

@author: athreya
"""

import sqlite3

conn=sqlite3.connect('movie.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Movies')

cur.execute('CREATE TABLE Movies(title TEXT,ratings INTEGER)')
cur.execute('INSERT INTO Movies(title,ratings) VALUES (?,?)',('KGF',5))
cur.execute('INSERT INTO Movies(title,ratings) VALUES (?,?)',('Natasarvabhouma',3))
cur.execute('''INSERT INTO MOVIES VALUES('Yajamana','4')''')
cur.execute('''INSERT INTO MOVIES VALUES('99','3.5')''')
cur.execute('SELECT * FROM Movies')
    
cur.execute('SELECT title,ratings FROM Movies')
for row in cur:
    print(row)
# =============================================================================
# OUTPUT:
# ('KGF', 5)
# ('Natasarvabhouma', 3)
# ('Yajamana', 4)
# ('99', 3.5)
# =============================================================================
cur.execute('''UPDATE Movies SET ratings=4.5 WHERE title='Yajamana' ''')
cur.execute('SELECT * FROM Movies')
for row in cur:
    print(row)
# =============================================================================
# OUTPUT:
# ('KGF', 5)
# ('Natasarvabhouma', 3)
# ('Yajamana', 4.5)
# ('99', 3.5)
# =============================================================================
cur.execute('''DELETE FROM Movies WHERE ratings<4 ''')
cur.execute('SELECT * FROM Movies')

for row in cur:
    print(row)
# =============================================================================
# OUTPUT:
# ('KGF', 5)
# ('Yajamana', 4.5)    
# =============================================================================
cur.execute('SELECT * FROM Movies ORDER BY title DESC')
for row in cur:
    print(row)
# =============================================================================
# OUTPUT:
# ('Yajamana', 4.5)
# ('Natasarvabhouma', 3)
# ('KGF', 5)
# ('99', 3.5)
# =============================================================================

cur.execute('SELECT * FROM Movies ORDER BY title ASC')
for row in cur:
    print(row)
# =============================================================================
# OUTPUT:
# ('99', 3.5)
# ('KGF', 5)
# ('Natasarvabhouma', 3)
# ('Yajamana', 4.5)
# =============================================================================
cur.close()
conn.close()

