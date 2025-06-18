# delete data


import sqlite3 
db = sqlite3.connect('movies.db')
cur = db.cursor()

# if not exist -> علشان نتجنب ايرور التكرار
# ان لو الجدول ده مش موجود هيعمله جديد ولو موجود مش هيطلع ايرور
cur.execute("CREATE TABLE IF NOT EXISTS x (name TEXT)")


cur.execute("SELECT rowid, * FROM movie")

data = cur.fetchall()
for row in data:
    print (row)
    
db.commit()
db.close()