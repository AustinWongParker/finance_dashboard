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

        self.balance = 500
        self.create_widgets()

    def create_widgets(self):
        # banner
        banner_label = tk.Label(root, text="Finance Dashboard Sign-On", bg="green", fg="white", font=("Arial", 16))
        banner_label.grid(row=0, column=0, columnspan=2, sticky="ew")  # Span two columns and expand horizontally

        # Connect to Database button
        connect_button = tk.Button(self.root, text="Connect to Database", command=self.connect_to_database)
        connect_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))  # Span two columns and add padding to the top

        # Show Balance button (initially disabled)
        self.balance_button = tk.Button(self.root, text="Show Balance", command=self.show_balance_window, state="disabled")
        self.balance_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Withdraw Money entry and button (initially disabled)
        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money, state="disabled")
        self.withdraw_amount_entry = tk.Entry(self.root)

        self.withdraw_button.grid(row=5, column=0, pady=5, padx=5, sticky="e")  # Button on the left
        self.withdraw_amount_entry.grid(row=5, column=1, pady=5, padx=5, sticky="e")  # Entry on the right

        # Deposit Money entry and button (initially disabled)
        self.deposit_button = tk.Button(self.root, text="Deposit Money", command=self.deposit_money, state="disabled")
        self.deposit_amount_entry = tk.Entry(self.root)

        self.deposit_button.grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.deposit_amount_entry.grid(row=4, column=1, pady=5, padx=5, sticky="w")

    def connect_to_database(self):
        # Add your database connection code here
        messagebox.showinfo("Database Connection", "Connecting to the database...")

        # Enable the Show Balance button
        self.balance_button.config(state="normal")
        self.withdraw_button.config(state="normal")
        self.deposit_button.config(state="normal")

    def show_balance_window(self):
        # Create a new window to display the balance information
        balance_window = tk.Toplevel(self.root)
        balance_window.title("Balance Information")

        # Create a label to display the balance
        balance_label = tk.Label(balance_window, text=f"Balance: ${self.balance}")
        balance_label.pack(padx=50, pady=50)

    def withdraw_money(self):
        # Get the withdrawal amount from the entry
        withdrawal_amount = self.withdraw_amount_entry.get()

        # Check if the withdrawal amount is a valid number
        try:
            withdrawal_amount = float(withdrawal_amount)
        except ValueError:
            messagebox.showerror("Withdrawal Error", "Invalid withdrawal amount")
            return

        if withdrawal_amount > 0:
            if self.balance >= withdrawal_amount:
                self.balance -= withdrawal_amount
                messagebox.showinfo("Withdrawal", f"Withdrew ${withdrawal_amount}")
            else:
                messagebox.showerror("Withdrawal Error", "Insufficient balance")
        else:
            messagebox.showerror("Withdrawal Error", "Invalid withdrawal amount")

    def deposit_money(self):
        deposit_amount = self.deposit_amount_entry.get()
        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            messagebox.showerror("Deposit Error", "Invalid deposit amount")
            return

        if deposit_amount > 0:
            self.balance += deposit_amount
            messagebox.showinfo("Deposit", f"Deposited ${deposit_amount}")
        else:
            messagebox.showerror("Deposit Error", "Invalid deposit amount")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")
    app = MainDashboard(root)
    root.mainloop()
