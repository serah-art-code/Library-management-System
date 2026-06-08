from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Library Management System")
root.geometry("400x300")

Label(root, text="Library Login", font=("Arial", 16)).pack(pady=10)

Label(root, text="Username").pack()
username = Entry(root)
username.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

def login():
    if username.get() == "admin" and password.get() == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()