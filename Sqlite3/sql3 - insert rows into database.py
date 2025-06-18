# insert rows into database

import sqlite3
con = sqlite3.connect('movies.db')

#بتسمحلي ان انا اكتب بلغة sql هنا
cursor = con.cursor()
#create table 

#method 1 to inseert rows
# cursor.execute(" INSERT INTO movie(title,genre,year) VALUES('oppenheimer','drama',2024)")
#method 2 
cursor.execute("INSERT INTO movie VALUES('oppenheimer','drama',2024)")
con.commit()
con.close() 