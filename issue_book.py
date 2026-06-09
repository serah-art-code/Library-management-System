from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date

root = Tk()
root.title("Issue Book")
root.geometry("400x300")

Label(root, text="Student Registration Number").pack()
student = Entry(root)
student.pack()

Label(root, text="Book Title").pack()
book = Entry(root)
book.pack()

def issue_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO issued_books(student_reg, book_title, issue_date) VALUES(?,?,?)",
        (student.get(), book.get(), str(date.today()))
    )

    cursor.execute(
        "UPDATE books SET status='Issued' WHERE title=?",
        (book.get(),)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Book Issued Successfully")

Button(root, text="Issue Book", command=issue_book).pack(pady=20)

root.mainloop()