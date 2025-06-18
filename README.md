# SqLite3-Tutorials
SQLite3-Tutorials 🗃️
A collection of easy‑to‑follow Python tutorials demonstrating the power of SQLite3 via step‑by‑step examples.

📚 Tutorials Overview
This repo guides you through SQLite database operations in Python—from setup to advanced usage:

Tutorial 1 – Introduction & Creating a Database
Connect to a .db file with sqlite3.connect() and initialize your database.

Tutorial 2 – Creating Tables
Use CREATE TABLE IF NOT EXISTS … syntax to define your schema safely.

Tutorial 3 – Inserting Records
Insert data directly and via parameterized queries with ? placeholders.

Tutorial 4 – Using Variables for INSERT
Pass Python variables into SQL commands securely to prevent SQL injection.

Tutorial 5 – Reading Data
Fetch rows with cursor.execute(), use fetchone() & fetchall(), and iterate through results.

Tutorial 6 – Updating a Record
Learn to modify existing rows and commit transactions properly.

Tutorial 7 – Deleting a Record
Remove unwanted data using DELETE FROM … WHERE …, with commit safety.

Tutorial 8 – Bonus & Conclusion
Summary insights, advanced tips, and suggested next steps.

(Adjust tutorial numbering/naming according to your actual files.)

⚙️ Why SQLite and Python?
Zero‑configuration – SQLite uses a single file, no server needed.

Built into Python – The sqlite3 module requires no installation.

Lightweight & reliable – Ideal for small‑to‑medium projects, scripting, development prototyping.

✅ Getting Started
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Haya146/SqLite3-Tutorials.git
cd SqLite3-Tutorials
Run each tutorial:

bash
Copy
Edit
python "Python SQLite3 Tutorial 1 - Introduction and Creating a Database.py"
Inspect the generated .db files (e.g., Our_data.db) using tools like:

Command-line: sqlite3 Our_data.db, then .tables, SELECT * FROM ...;

GUI: DB Browser for SQLite or SQLite Studio.

🧩 Example: Insert & Read
python
Copy
Edit
import sqlite3

conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
  )
""")

# Insert data
cursor.execute(
  "INSERT INTO users (name, email) VALUES (?, ?)",
  ("Alice", "alice@example.com")
)

# Read data
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
💡 Best Practices
Use parameterized queries (? or :named) for safety.

Commit regularly, rollback on failures.

Close connections when done.

Be mindful of SQLite limitations: no stored procedures, limited concurrency.

🚀 Next Steps
Learn advanced features: transactions, row factories, Blobs, foreign keys.

Use Pandas integration via pd.read_sql().

Explore SQLite Studio and migration to other RDBMS.

📝 License
This project is available under the MIT License – see the LICENSE file.

❤️ Contributing
PRs and suggestions are welcome! Feel free to:

Add new tutorial steps (e.g. transactions, exporting CSV)

Improve scripts with error handling

Enhance documentation or examples

Enjoy learning SQLite3 with Python! 🎉
