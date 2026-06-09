from tkinter import *
import sqlite3

root = Tk()
root.title("Books List")
root.geometry("600x400")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, width=80, yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH, expand=True)

scrollbar.config(command=listbox.yview)

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for book in books:
    listbox.insert(END, book)

conn.close()

root.mainloop()