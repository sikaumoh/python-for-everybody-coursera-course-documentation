# Basic Rules
# Don't put the same string data twice
# Model the real world

# JOIN Operation
# Join Operation links different tables together based on keys
# SELECT table1.title, table2.name FROM table1 JOIN table2 on table1.table2_id = table2.id

import xml.etree.ElementTree as ET
import sqlite3
import json

# Exercise 1
# Connect to DataBase
connection = sqlite3.connect('trackdb.sqlite')
cur = connection.cursor()

# Read file
# filename = input('Enter file name: ')
# if ( len(filename) < 1 ) : filename = 'Library.xml'
# content = ET.parse(filename)
# data = content.findall('dict/dict/dict')

# Retrieval function
def retrieve(element, value):
    found = False
    for child in element:
        if found: return child.text
        if child.tag == 'key' and child.text == value :
            found = True
    return None


# Use Data
for item in data:
    if retrieve(item, 'Track ID') is None: continue

    get Data
    name = retrieve(item, 'Name')
    artist = retrieve(item, 'Artist')
    album = retrieve(item, 'Album')
    count = retrieve(item, 'Play Count')
    rating = retrieve(item, 'Rating')
    length = retrieve(item, 'Total Time')
    genre = retrieve(item, 'Genre')

    Insert into DataBase
    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, count, rating, length)

    Insert Artist details
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    Insert Album details
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    Insert Genre details
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    Insert Track details
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, len, rating, count, genre_id)
        VALUES ( ?, ?, ?, ?, ?, ? )''', ( name, album_id, length, rating, count, genre_id) )

connection.commit()

# Many to Many Relationship
# Like knowing if a user does a particular course or other course
# Courses (course_id) <- Members (user_id, course_id) -> Users (user_id)
# This can be used to Know which Users study which Courses

# Exercise 2

connection = sqlite3.connect('roster_data.sqlite')
cur = connection.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file = open('roster_data.json')
data = json.load(file)
for details in data:
    name = details[0]
    title = details[1]
    role = details[2]
    print((name, title))
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role, ) )
connection.commit()
