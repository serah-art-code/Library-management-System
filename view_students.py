from tkinter import *
import sqlite3

root = Tk()
root.title("Students List")
root.geometry("600x400")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, width=70, yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH, expand=True)

scrollbar.config(command=listbox.yview)

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    listbox.insert(END, student)

conn.close()

root.mainloop()