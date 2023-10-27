'''
Finance Dashboard - JPMC StrongStart

Defects Demo
'''

import tkinter as tk
from tkinter import messagebox

class MainDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("JPMC StrongStart Defects Demo")

        self.create_widgets()

    def create_widgets(self):
        # banner
        banner_label = tk.Label(root, text="Finance Dashboard Sign-On", bg="green", fg="white", font=("Arial", 16))
        banner_label.grid(row=0, column=0, columnspan=2, sticky="ew")  # Span two columns and expand horizontally

        username_label = tk.Label(self.root, text="Username:")
        username_label.grid(row=1, column=0, sticky="e")

        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1) 

        password_label = tk.Label(self.root, text="Password:")
        password_label.grid(row=2, column=0, sticky="e")

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=2, column=1)

        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=3)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace this with your authentication logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")
    app = MainDashboard(root)
    root.mainloop()
