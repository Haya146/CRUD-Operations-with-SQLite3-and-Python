# delete data


import sqlite3 
db = sqlite3.connect('movies.db')
cur = db.cursor()
# غير اسم الtitle الي في الصف ال 3
cur.execute("DELETE FROM movie WHERE rowid = 3")
cur.execute("DELETE FROM movie WHERE title = 'oppinhiemer'")

#  عايز تحذف الجدول كله 
cur.execute("DROP TABLE movie")

cur.execute("SELECT rowid, * FROM movie")

data = cur.fetchall()
for row in data:
    print (row)
    
db.commit()
db.close()