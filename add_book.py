from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Add Book")
root.geometry("400x250")

Label(root, text="Book Title").pack()
title = Entry(root, width=30)
title.pack()

Label(root, text="Author").pack()
author = Entry(root, width=30)
author.pack()

def add_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books(title, author, status) VALUES(?,?,?)",
        (title.get(), author.get(), "Available")
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Book Added Successfully")

    title.delete(0, END)
    author.delete(0, END)

Button(root, text="Add Book", command=add_book).pack(pady=20)

root.mainloop()