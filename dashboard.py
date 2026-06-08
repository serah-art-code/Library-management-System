from tkinter import *
import sqlite3

root = Tk()
root.title("Library Dashboard")
root.geometry("500x400")

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
students = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM books")
books = cursor.fetchone()[0]

conn.close()

Label(root, text="Library Management System",
      font=("Arial", 16, "bold")).pack(pady=20)

Label(root, text=f"Total Students: {students}",
      font=("Arial", 12)).pack(pady=10)

Label(root, text=f"Total Books: {books}",
      font=("Arial", 12)).pack(pady=10)

root.mainloop()