from tkinter import *
import os

root = Tk()
root.title("Library Management System")
root.geometry("600x400")

Label(
    root,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 16, "bold")
).pack(pady=20)

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
    text="Exit",
    width=20,
    command=root.destroy
).pack(pady=5)

root.mainloop()