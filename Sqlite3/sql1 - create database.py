import sqlite3

# Create Database file
con = sqlite3.connect('movies.db')

con.close()