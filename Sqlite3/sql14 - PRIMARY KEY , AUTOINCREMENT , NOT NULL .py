import sqlite3 

db = sqlite3.connect("movies.db")
cur = db.cursor()

# ازاي اعمل  عمود لل id تلقائي 
# primmary key -> يعني القييمه بتاعته مينفعش انها تتكرر
# autoincrement -> معناه يجخل القيمة دي بنفسه وكل مره يزيد 1 
# not null -> يعني مينفعش اسيب القيمة دي فاضي لازم يكتب فيها حاجه 

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            age INTEGER
)""")

cur.execute("INSERT INTO users(name,age) VALUES('ahmed',17)")
cur.execute("SELECT * FROM users")

data = cur.fetchall()
for row in data :
    print(row)

db.commit()
db.close()