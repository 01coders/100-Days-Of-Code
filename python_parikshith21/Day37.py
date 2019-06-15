# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:13:54 2019

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
    
# =============================================================================
# #output:
# #('Thunderstuck', 200)  #tuple
# #('Dangerous', 20)
# #('Myway', 150)
# #('Newway', 30)
# =============================================================================

cur.execute('SELECT title,plays FROM Tracks')
for row in cur:
    print(row)
   
# =============================================================================
# #output:
# #('Thunderstuck', 200)  #tuple
# #('Dangerous', 20)
# #('Myway', 150)
# #('Newway', 30)
# =============================================================================

cur.execute('SELECT title FROM Tracks')
for row in cur:
    print(row)
    
# =============================================================================
# #output:
# #('Thunderstuck',)
# #('Dangerous',)
# #('Myway',)
# #('Newway',)
# =============================================================================
    
cur.close()
conn.close()