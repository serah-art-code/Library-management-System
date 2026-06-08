import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

books = [
("Python Programming", "John Smith", "Available"),
("Database Systems", "Mark David", "Available"),
("Computer Networks", "James Brown", "Available"),
("Web Development", "Peter Jones", "Available"),
("Operating Systems", "Kevin White", "Available")
]

cursor.executemany(
"INSERT INTO books(title, author, status) VALUES(?,?,?)",
books
)

conn.commit()
conn.close()

print("Books added successfully")