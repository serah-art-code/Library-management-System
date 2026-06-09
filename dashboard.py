from tkinter import *
import sqlite3
import os

root = Tk()
root.title("Library Management System")
root.geometry("600x400")

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
students = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM books")
books = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM issued_books")
issued = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM books WHERE status='Available'")
available = cursor.fetchone()[0]

conn.close()

Label(
    root,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
).pack(pady=20)

Label(
    root,
    text=f"Total Students: {students}",
    font=("Arial", 12)
).pack()

Label(
    root,
    text=f"Total Books: {books}",
    font=("Arial", 12)
).pack(pady=10)
Label(
    root,
    text=f"Books Issued: {issued}",
    font=("Arial", 12)
).pack()

Label(
    root,
    text=f"Books Available: {available}",
    font=("Arial", 12)
).pack() 

Button(
    root,
    text="Add Book",
    width=20,
    command=lambda: os.system("py add_book.py")
).pack(pady=5)

Button(
    root,
    text="Issue Book",
    width=20,
    command=lambda: os.system("py issue_book.py")
).pack(pady=5)

Button(
    root,
    text="Return Book",
    width=20,
    command=lambda: os.system("py return_book.py")
).pack(pady=5)

Button(
    root,
    text="Add student",
    width=20,
    command=lambda:os.system("py add_student.py")
    ).pack(pady=5)

Button(
    root,
    text="view students",
    width=20,
    command=lambda: os.system("py view_students.py")
).pack(pady=5)

Button(
    root,
    text="View Books",
    width=20,
    command=lambda: os.system("py view_books.py")
).pack(pady=5)

Button(
    root,
    text="View Issued Books",
    width=20,
    command=lambda: os.system("py view_issued_books.py")
).pack(pady=5)

Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
).pack(pady=20)

root.mainloop()