import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
reg_no TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
status TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_reg TEXT,
book_title TEXT,
issue_date TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")