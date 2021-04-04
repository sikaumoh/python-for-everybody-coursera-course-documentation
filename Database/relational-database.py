# check http://en.wikipedia.org/wiki/Relational database
# download 'DB Browser for SQLite'
# A relation is a set of tuples that have the same attributes
# Structured Query Language (SQL)
# SQL Functions: Create, Read, Update and Delete, CRUD

# SQL Insert
# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')

# Delete and Update
# DELETE FROM Users WHERE email='ted@umich.edu'
# UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

# Retrieving Records
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@gmail.com'

# Sorting Records
# SELECT * FROM Users ORDER BY email

import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cur = connection.cursor()

# Drop any TABLE and Create TABLE
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

filename = input('Enter file name: ')
if (len(filename) < 1): filename = 'mbox-short.txt'
data = open(filename)
for line in data:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    connection.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

# Exercise 

connection = sqlite3.connect('orgdb.sqlite')
cur = connection.cursor()

# Clean and Create TABLE
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# dealing with file
data = open('mbox.txt')
for line in data:
    if not line.startswith('From '): continue
    email = line.split()[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
connection.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
