# insert many rows into database

import sqlite3
con = sqlite3.connect('movies.db')
cursor = con.cursor()

movies = [
    ('the godfather','crime',1970),
    ('oppenhiemer','drama',2023),
    ('the whale','drama',2023),
    ('Delete History','comedy',2020),
    ('Apples','fantasy',2020),
    ('Nomadland','drama',2020),
]

cursor.executemany("INSERT INTO movie VALUES(?,?,?)",movies)
con.commit()
con.close() 