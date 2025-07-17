import random as r
import string as s
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Button, Radiobutton, Label, Entry

def PassEasy(length):
    return ''.join(r.choice(s.digits) for i in range(length))

def PassMed(length):
    return ''.join(r.choice(s.ascii_letters + s.digits) for i in range(length))

def PassHard(length):
    return ''.join(r.choice(s.ascii_letters + s.digits + s.punctuation) for i in range(length))


window = tb.Window(themename="flatly")
window.title("Password Generator")
window.geometry('600x500')
window.configure(bg="#FFD6A5") 


title_label = Label(window, text="Password Generator",font=("Arial", 28, "bold"), bootstyle="warning")
title_label.pack(pady=20)


radio_var = StringVar(value="EASY")
radio_frame = Frame(window, bg="#FFE5B4")
radio_frame.pack(pady=10)

choices = ["EASY" , "MEDIUM" , "HIGH"]
for choice in choices:
    Radiobutton(radio_frame, text = choice, variable=radio_var,value=choice,
                bootstyle="success").pack(side=LEFT, padx=10)


label1 = Label(window, text="Enter Password Length:", font=("Arial", 14), bootstyle="warning")
label1.pack(pady=10)

length_entry = Entry(window, font=("Arial", 12), bootstyle="warning")
length_entry.pack(pady=5)

result_label = Label(window,text="", font=("Courier New", 20, "bold"), bootstyle="warning",
                      background="#fcefee")
result_label.pack(pady=20)


def PasswordGenerator():
    try:
        length = int(length_entry.get())
        complexity = radio_var.get()

        if length <= 0:
            messagebox.showerror("Invalid Input", "Please enter a number greater than 0.")
            return

        if complexity == "HIGH":
            pwd = PassHard(length)
        elif complexity == "MEDIUM":
            pwd = PassMed(length)
        else:
            pwd = PassEasy(length)

        result_label.config(text=pwd)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

submit = Button(window, text="Generate Password", bootstyle="success-outline", width=22, 
                padding=10, command=PasswordGenerator)
submit.pack(pady=10)

window.mainloop()
