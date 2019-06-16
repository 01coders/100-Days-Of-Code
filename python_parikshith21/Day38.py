# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:05:46 2019

@author: Parikshith.H
"""

import sqlite3

conn=sqlite3.connect('music.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT,plays INTEGER)')
cur.execute('''INSERT INTO Tracks(title,plays) VALUES ('Thunder2',100)''')
cur.execute('''INSERT INTO Tracks VALUES ('Thunder3',100)''')
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Thunderstuck',200))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Dangerous',20))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Myway',150))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Newway',30))

cur.execute('SELECT * FROM Tracks')
for row in cur:
    print(row)
    
cur.execute('SELECT title,plays FROM Tracks')
for row in cur:
    print(row)

cur.execute('SELECT title FROM Tracks')
for row in cur:
    print(row)
    
cur.close()
conn.close()
# =============================================================================
# #output:
# ('Thunder2', 100)
# ('Thunder3', 100)
# ('Thunderstuck', 200)
# ('Dangerous', 20)
# ('Myway', 150)
# ('Newway', 30)
# ('Thunder2', 100)
# ('Thunder3', 100)
# ('Thunderstuck', 200)
# ('Dangerous', 20)
# ('Myway', 150)
# ('Newway', 30)
# ('Thunder2',)
# ('Thunder3',)
# ('Thunderstuck',)
# ('Dangerous',)
# ('Myway',)
# ('Newway',)
# =============================================================================