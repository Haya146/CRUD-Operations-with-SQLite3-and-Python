# read data using fetch 


import sqlite3

db = sqlite3.connect('movies.db')

cur = db.cursor()
data = cur.execute("SELECT * FROM movie")
# بتوصل لاول صف موجود عندك
print( cur.fetchone() )
#بحدد عدد الصفوف الي انا عايزاها
print( cur.fetchmany(2) )
# بتطبع كل الصفوف الي انا كنت محددها
print( cur.fetchall() )

db.commit()
db.close()