import tkinter as tk
from tkinter import messagebox

class ATMSimulator:
    def __init__(self,root):
        self.root= root
        self.root.title("ATM Simulator")
        self.user = {
            "user1" : {"pin" : "1234" , "balance" : 1000.00},
             "user2" : {"pin": "5678" , "balance" : 2000.00},
        }
        self.current_user = None
        self.create_login()

    def create_login(self):
        self.clear_page()
        tk.Label(self.root, text="ATM Simulator").pack(pady=5)
        tk.Label(self.root, text="USERNAME").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="PIN").pack(pady=5)
        self.pin_entry = tk.Entry(self.root)
        self.pin_entry.pack(pady=5)
        tk.Button(self.root, text="LOGIN", command=self.login).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        pin = self.pin_entry.get()
        if username in self.user and self.user[username]["pin"] == pin:
            self.current_user = username
            messagebox.showinfo("successfully" , "successfully login")
            self.create_main_menu()
        else:
            messagebox.showerror("error" ,"invalid username and pin")

    def create_main_menu(self):
        self.clear_page()

        tk.Button(self.root , text="WITHDRAW" , command = self.withdraw_screen).pack(pady=5)
        tk.Button(self.root , text="DEPOSIT" , command = self.deposit_screen).pack(pady=5)
        tk.Button(self.root , text="CHANGE PIN" , command = self.change_pin_screen).pack(pady=5)
        tk.Button(self.root , text="BACK" , command = self.back).pack(pady=5)
        tk.Button(self.root , text="LOGOUT" , command = self.logout).pack(pady=5)

    def withdraw_screen(self):
        self.clear_page()
        tk.Label(self.root , text="WITHDRAW").pack(pady=5)
        tk.Label(self.root , text="enter your ammount to withdraw" ).pack(pady=5)
        self.withdraw_entry= tk.Entry(self.root)
        self.withdraw_entry.pack(pady=5)
        tk.Button(self.root , text="WITHDRAW" , command = self.withdraw_amount).pack(pady=5)
        tk.Button(self.root , text="BACK" , command = self.create_login).pack(pady=5)

    def withdraw_amount(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount <=0:
                raise ValueError
        except ValueError:
            messagebox.showerror("invalid , enter valid amount")
            return
        if amount > self.user[self.current_user]["balance"]:
            messagebox.showerror("invalid , insufficient amount")
            return
        self.user[self.current_user]["balance"] -= amount
        messagebox.showinfo("successfully withdraw" , f"new withdrawl: {self.user[self.current_user]['balance']:.2f}")
        self.create_main_menu()

    def deposit_screen(self):
        self.clear_page()
        tk.Label(self.root , text="DEPOSIT").pack(pady=5)
        tk.Label(self.root , text="enter your ammount to deposit" ).pack(pady=5)
        self.deposit_entry= tk.Entry(self.root)
        self.deposit_entry.pack(pady=5)
        tk.Button(self.root , text="deposit" , command = self.deposit_amount).pack(pady=5)
        tk.Button(self.root , text="BACK" , command = self.create_login)

    def deposit_amount(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount<=0:
                raise ValueError
        except ValueError:
            messagebox.showerror("invalid , enter valid ammount")
            return
        self.user[self.current_user]['balance'] += amount
        messagebox.showinfo("successfully deposit" ,f"new deposit {self.user[self.current_user]['balance']:.2f}")
        self.create_main_menu()

    def change_pin_screen(self):
        self.clear_page()

        tk.Label(self.root, text="Change PIN", font=("Helvetica", 14)).pack(pady=10)
        tk.Label(self.root, text="Enter New PIN").pack(pady=5)
        self.new_pin_entry = tk.Entry(self.root)
        self.new_pin_entry.pack(pady=5)

        tk.Label(self.root, text="Confirm New PIN").pack(pady=5)
        self.confirm_pin_entry = tk.Entry(self.root)
        self.confirm_pin_entry.pack(pady=5)

        tk.Button(self.root, text="Change PIN", command=self.change_pin).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=5)

    def change_pin(self):
        new_pin = self.new_pin_entry.get()
        confirm_pin = self.confirm_pin_entry.get()
        if len(new_pin) !=4 or not new_pin.isdigit():
            messagebox.showerror("invalid" , "pin must be 4 digit")
            return
        if new_pin != confirm_pin:
            messagebox.showerror("invalid" , "pin must be same of new pin")
            return
        self.user[self.current_user]['pin'] = new_pin
        messagebox.showinfo("successfully" , "pin changed")
        self.create_main_menu()

    def back(self):
        self.create_login()

    def logout(self):
        self.current_user = None
        messagebox.showinfo("successfully" ," logout")
        self.create_login()


    def clear_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__== "__main__":
    root = tk.Tk()
    app =  ATMSimulator(root)
    root.mainloop()






