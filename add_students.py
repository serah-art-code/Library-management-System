from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Add Student")
root.geometry("400x250")

Label(root, text="Student Name").pack()
name = Entry(root, width=30)
name.pack()

Label(root, text="Registration Number").pack()
reg = Entry(root, width=30)
reg.pack()

def add_student():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, reg_no) VALUES(?, ?)",
        (name.get(), reg.get())
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Added Successfully")

    name.delete(0, END)
    reg.delete(0, END)

Button(root, text="Add Student", command=add_student).pack(pady=20)

root.mainloop()