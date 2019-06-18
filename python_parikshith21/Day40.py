# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:09:59 2019

@author: Parikshith.H
"""

import sqlite3

conn=sqlite3.connect('music.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT,plays INTEGER)')
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Thunderstuck',200))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Dangerous',20))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Myway',150))
cur.execute('INSERT INTO Tracks(title,plays) VALUES (?,?)',('Newway',30))

cur.execute('SELECT * FROM Tracks')
for row in cur:
    print(row)
print("********************") 
cur.execute('SELECT * FROM Tracks ORDER BY title') #or can use ASC for ascending
for row in cur:
    print(row)

# =============================================================================
# #output:
# ('Thunderstuck', 200)
# ('Dangerous', 20)
# ('Myway', 150)
# ('Newway', 30)
# ********************
# ('Dangerous', 20)
# ('Myway', 150)
# ('Newway', 30)
# ('Thunderstuck', 200)
# =============================================================================
 
cur.execute('SELECT * FROM Tracks ORDER BY title DESC')
for row in cur:
    print(row)
    
# =============================================================================
# #ouput:
# ('Thunderstuck', 200)
# ('Newway', 30)
# ('Myway', 150)
# ('Dangerous', 20)
# =============================================================================