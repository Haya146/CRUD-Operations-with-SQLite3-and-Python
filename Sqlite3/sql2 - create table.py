# create tables in the database
import sqlite3
con = sqlite3.connect('movies.db')

#بتسمحلي ان انا اكتب بلغة sql هنا
cursor = con.cursor()
#create table 
cursor.execute(" CREATE TABLE movie(title TEXT, genre TEXT, year INTEGER)")
con.commit()
con.close() 