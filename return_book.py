from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Return Book")
root.geometry("400x250")

Label(root, text="Book Title").pack()

book = Entry(root)
book.pack()

def return_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM issued_books WHERE book_title=?",
        (book.get(),)
    )

    cursor.execute(
        "UPDATE books SET status='Available' WHERE title=?",
        (book.get(),)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Book Returned Successfully")

Button(root, text="Return Book", command=return_book).pack(pady=20)

root.mainloop()