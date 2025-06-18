import sqlite3

db = sqlite3.connect('movies.db')

cur = db.cursor()

cur.execute("SELECT rowid, * FROM movie WHERE title = 'oppenhiemer'")
cur.execute("SELECT rowid, * FROM movie WHERE genre != 'drama'")
cur.execute("SELECT rowid, * FROM movie WHERE year >= 2023")
cur.execute("SELECT rowid, * FROM movie WHERE genre = 'drama' OR year = 2023")
cur.execute("SELECT rowid, * FROM movie WHERE genre = 'drama' AND year = 2023")
cur.execute("SELECT rowid, * FROM movie WHERE title = LOWER ('OPpenhiemer')")  
cur.execute("SELECT rowid, * FROM movie WHERE UPPER(title) = UPPER ('OPpenhiemer')")  
cur.execute("SELECT rowid, * FROM movie WHERE year BETWEEN 2020 AND 2023")  
cur.execute("SELECT rowid, * FROM movie WHERE year NOT BETWEEN 2020 AND 2023")  


data = cur.fetchall()

for row in data: 
    print(row)

db.commit()
db.close()