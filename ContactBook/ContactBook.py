import json
from tkinter import *
from tkinter import messagebox , simpledialog , Toplevel
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Button, Radiobutton, Label

class Contact:
    def __init__(self, name, contact, email, address):
        self.name = name
        self.contact = contact
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact_obj):
        for detail in self.contact_list:
            if detail.name == contact_obj.name:
                return False
        else:
            self.contact_list.append(contact_obj)
            return True

    def view_contacts(self):
        if not self.contact_list:
            return "No contacts found"
        result = ""
        for detail in self.contact_list:
            result += f"Name    : {detail.name} Contact : {detail.contact} Email   : {detail.email} Address : {detail.address}\n\n"
        return result

    def search_contact(self, entry):
        for detail in self.contact_list:
            if detail.name == entry or detail.contact == entry:
                return f"Name    : {detail.name} Contact : {detail.contact} Email   : {detail.email} Address : {detail.address}"
        return "Contact not found"

    def update_contact(self, contact_obj):
        for detail in self.contact_list:
            if detail.name == contact_obj.name:
                detail.contact = contact_obj.contact
                detail.email = contact_obj.email
                detail.address = contact_obj.address
                return True
        return False

    def remove_contact(self, name):
        for detail in self.contact_list:
            if detail.name == name:
                self.contact_list.remove(detail)
                return True
        return False

    def save_to_json(self, filename):
        try:
            data = []
            for contact in self.contact_list:
                data.append({
                    "name": contact.name,
                    "contact": contact.contact,
                    "email": contact.email,
                    "address": contact.address
                })
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print("Contacts saved to JSON file.")
        except Exception as e:
            print("Error saving to JSON:", e)

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contact_list.clear()
                for item in data:
                    contact = Contact(
                        item["name"],
                        item["contact"],
                        item["email"],
                        item["address"]
                    )
                    self.contact_list.append(contact)
                print("Contacts loaded from JSON file.")
        except FileNotFoundError:
            print("JSON file not found.")
            
book = ContactBook()
book.load_from_json("ContactBook.json")
window = tb.Window(themename="minty")
window.title("Contact book")
window.geometry('1200x500')
window.configure(bg="#E5D5FA") 

title_label = Label(window, text="Contact Book",font=("Arial", 28, "bold"), bootstyle="primary" )
title_label.pack(pady=20)

radio_var = StringVar(value="Add Contacts")
radio_frame = Frame(window)
radio_frame.pack(pady=10)

options = ['Add contacts', 'Delete contacts', 'Update contacts', 'Search contacts', 'View contacts', 'Save Changes']
for option in options:
    Radiobutton(radio_frame, text = option, variable=radio_var, value=option, bootstyle="info").pack(side=LEFT, padx=10)

def perform_operation():
    choice = radio_var.get()

    if choice == "Add contacts":
        name = simpledialog.askstring("Input", "Enter Name:")
        contact = simpledialog.askstring("Input", "Enter Contact:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")
        if name and contact:
            added = book.add_contact(Contact(name, contact, email, address))
            messagebox.showinfo("Add Contact", "Contact is added!" if added else "Contact already exists")

    elif choice == "Delete contacts":
        name = simpledialog.askstring("Input", "Name of the contact you want to delete")
        removed = book.remove_contact(name)
        messagebox.showinfo("Delete Contact", "Contact is deleted" if removed else "Contact does not exists")

    elif choice == "Update contacts":
        name = simpledialog.askstring("Input", "Enter existing name:")
        new_contact = simpledialog.askstring("Input", "Enter new Phone:")
        new_email = simpledialog.askstring("Input", "Enter new Email:")
        new_address = simpledialog.askstring("Input", "Enter new Address:")
        updated = book.update_contact(Contact(name, new_contact, new_email, new_address))
        messagebox.showinfo("Update Contact", "Contact is updated" if updated else "Contact does not exists")

    elif choice == "Search contacts":
        entry = simpledialog.askstring("Input", "Enter Name or Contact")
        searched = book.search_contact(entry)
        messagebox.showinfo("Search Contact", searched)

    elif choice == "View contacts":
        viewed = book.view_contacts()
        view_window = Toplevel(window)
        view_window.title("All Contacts")
        view_window.geometry('1500x1500')
        window.config(bg="#D8B7DD")

        view_label = Label(view_window, text=viewed, font=("Arial", 12), bootstyle="info")
        view_label.pack(padx=20, pady=20)

    elif choice == "Save Changes":
        book.save_to_json("ContactBook.json")
        messagebox.showinfo("Save Contact", "Contacts saved successfully.")

submit = Button(window, text="Submit", bootstyle="info-outline",
                 width=22, padding=10, command=perform_operation)
submit.pack(pady=10)

window.mainloop()