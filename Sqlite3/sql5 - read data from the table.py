# read data from the table

import sqlite3

db = sqlite3.connect('movies.db')

cur = db.cursor()
data = cur.execute("SELECT * FROM movie")
# data = cur.execute("SELECT title FROM movie")
# data = cur.execute("SELECT title,genre FROM movie")
for row in data :
    print(row)
    
db.commit()
db.close()