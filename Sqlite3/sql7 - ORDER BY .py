import sqlite3

db = sqlite3.connect('movies.db')

cur = db.cursor()
cur.execute("SELECT * FROM movie ORDER BY title")
# cur.execute("SELECT * FROM movie ORDER BY title DESC")
# cur.execute("SELECT * FROM movie ORDER BY title ASC")

data = cur.fetchall()

for row in data: 
    print(row)

db.commit()
db.close()