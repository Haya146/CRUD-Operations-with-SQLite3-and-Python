import sqlite3

db = sqlite3.connect('movies.db')

cur = db.cursor()
cur.execute("SELECT rowid, * FROM movie ORDER BY title LIMIT 2")
data = cur.fetchall()

for row in data: 
    print(row)

db.commit()
db.close()