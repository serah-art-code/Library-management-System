from tkinter import *
import sqlite3

root = Tk()
root.title("Issued Books")
root.geometry("700x400")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, width=100, yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH, expand=True)

scrollbar.config(command=listbox.yview)

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM issued_books")
records = cursor.fetchall()

for record in records:
    listbox.insert(END, record)

conn.close()

root.mainloop()