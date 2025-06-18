import sqlite3

db = sqlite3.connect('movies.db')

cur = db.cursor()


cur.execute("SELECT rowid, * FROM movie LIKE 'opPENhiemer'") # بيجيب الي شبههم   
cur.execute("SELECT rowid, * FROM movie LIKE 'o%'") # بيبدا بحرف ال o   
cur.execute("SELECT rowid, * FROM movie LIKE '%a%'") # اي كلمة بتحتوي على حرف ال a
cur.execute("SELECT rowid, * FROM movie LIKE '%e'") # اي كلمة اخر حرف فيها هو حرف ال e
cur.execute("SELECT rowid, * FROM movie LIKE '_e'") # اي كلمة تاني حرف فيها هو حرف ال e




data = cur.fetchall()

for row in data: 
    print(row)

db.commit()
db.close()