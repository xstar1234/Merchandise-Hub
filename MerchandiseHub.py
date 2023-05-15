#Everything is subject to change, not all ideas/features have been implemented
import tkinter
#Imports everything needed for tkinter, and some extra modules
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning
from tkinter import filedialog
import os, shutil
import pickle
import csv

#Creates a class for the add button, so it has another window
class AddWindow(Toplevel):

    def __init__(self, master = None):
        super().__init__(master = master)
        self.title('Add new item')

        #Creates all of the "add" buttons windows variables
        #(centers it, doesn't let it be resizeable, etc.)
        window_width = 500
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.name_section()
        self.description_section()
        self.currency_section()
        self.save_section()

    def name_section(self):
        #Creates the "name" label area
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        name = StringVar()
        self.name_label = Label(self, text='Name:')
        self.name_label.pack(anchor=NW, **options1)
        self.name_entry = Entry(self, textvariable=name)
        self.name_entry.pack(anchor=NW, **options2)

    def description_section(self):
        #Creates the "description" label area
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        description = StringVar()
        self.description_label = Label(self, text='Description:')
        self.description_label.pack(anchor=NW, **options1)
        self.description_entry = Entry(self, textvariable=description)
        self.description_entry.pack(anchor=NW, **options2)

    def currency_section(self):
        #Creates the "currency" label area
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        currency = StringVar()
        self.currency_label = Label(self, text='Price:')
        self.currency_label.pack(anchor=NW, **options1)
        self.currency_entry = Entry(self, textvariable=currency)
        self.currency_entry.pack(anchor=NW, **options2)

    def save_section(self):
        #Creates the "save" button
        options4 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 25}
        self.save_button = Button(self, text='Save and Create', command=self.save_button_clicked)
        self.save_button.pack(anchor=S, **options4)

    def save_button_clicked(self):
        """ Handle save button click event
        """
        #Gets each entry, turns it into a variable
        name_input = self.name_entry.get()
        description_input = self.description_entry.get()
        price_input = self.currency_entry.get()

        #Input validation of each variable above
        if not name_input:
            showwarning(title='Alert', message='No input!')
            return

        if not description_input:
            showwarning(title='Alert', message='No input!')
            return

        if not price_input:
            showwarning(title='Alert', message='No input!')
            return

        #Saves all of the user inputs into an excel file
        with open('saved_text.csv', 'a', newline='') as f:
            w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.currency_entry.get()
            w.writerow([name, description, price])
        msg = "Item has been saved!"
        showwarning(title='Alert', message=msg)
        self.destroy()

#Creates a class for the edit button, so it has another window
class EditWindow(Toplevel):

    def __init__(self, master = None):
        super().__init__(master = master)
        self.title('Edit and Remove Item')

        #Creates all of the "edit" buttons windows variables
        #(centers it, doesn't let it be resizeable, etc.)
        window_width = 500
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.saved_section()
        self.edit_label()
        self.edit_section()
        self.remove_section()
        self.load()
        self.remove_button_clicked()

    def saved_section(self):
        #Shows the listbox of saved items
        self.saved_items = Listbox(self, selectmode=SINGLE)
        self.saved_items.place(relx=0.5, rely=0.5, width=350, height=350, anchor="center")

    def edit_label(self):
        #Creates the label shown above the listbox
        options1 = {'ipadx': 0, 'ipady': 20, 'padx': 10, 'pady': 5}
        self.edit_label = Label(self, text='Pick a save here below:')
        self.edit_label.pack(anchor=N, **options1)

    def edit_section(self):
        #Creates the edit button
        self.edit_button = Button(self, text='Edit')
        self.edit_button.bind('<Button>', lambda e: EditButtonClickedWindow(root))
        self.edit_button.place(relx=0.3, rely=0.9)

    def remove_section(self):
        #Creates the remove button
        self.remove_button = Button(self, text='Remove', command=self.remove_button_clicked)
        self.remove_button.place(relx=0.55, rely=0.9)

    def load(self):
        #Inserts saved data into listbox
        with open('saved_text.csv', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for item in reader:
                self.saved_items.insert(END, item)

    def remove_button_clicked(self):
        """ Handle remove button click event
        """
        #Allows for the remove button to function (although, it seems to be quite busted, and I don't know how to make it stop showing
        #the message when you first open the edit menu)
        selected_index = self.saved_items.curselection()
        if len(selected_index) == 1:
            selected_item = self.saved_items.get(selected_index)
            self.saved_items.delete(selected_index)
            with open("saved_text.csv", "r") as f:
                lines = f.readlines()
            with open("saved_text.csv", "w") as f:
                for line in lines:
                    if line.strip() != selected_item:
                        f.write(line)
        msg = "Item has been deleted!"
        showwarning(title='Alert', message=msg)

#Creates a class for the edit button located in the edit screen, so it has another window
class EditButtonClickedWindow(Toplevel):

    def __init__(self, master = None):
        super().__init__(master = master)
        self.title('Edit item')

        #Creates all of the "add" buttons windows variables
        #(centers it, doesn't let it be resizeable, etc.)
        window_width = 500
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.name_section()
        self.description_section()
        self.currency_section()
        self.save_section()

    def name_section(self):
        #Creates the "name" label area
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        name = StringVar()
        self.name_label = Label(self, text='Name:')
        self.name_label.pack(anchor=NW, **options1)
        self.name_entry = Entry(self, textvariable=name)
        self.name_entry.pack(anchor=NW, **options2)

    def description_section(self):
        #Creates the "description" label area
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        description = StringVar()
        self.description_label = Label(self, text='Description:')
        self.description_label.pack(anchor=NW, **options1)
        self.description_entry = Entry(self, textvariable=description)
        self.description_entry.pack(anchor=NW, **options2)

    def currency_section(self):
        #Creates the "currency" label area
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        currency = StringVar()
        self.currency_label = Label(self, text='Price:')
        self.currency_label.pack(anchor=NW, **options1)
        self.currency_entry = Entry(self, textvariable=currency)
        self.currency_entry.pack(anchor=NW, **options2)

    def save_section(self):
        #Creates the "save" button
        options4 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 25}
        self.save_button = Button(self, text='Save and Recreate', command=self.save_button_clicked)
        self.save_button.pack(anchor=S, **options4)

    def save_button_clicked(self):
        """ Handle save button click event
        """
        #Gets each entry, turns it into a variable
        name_input = self.name_entry.get()
        description_input = self.description_entry.get()
        price_input = self.currency_entry.get()

        #Input validation of each variable above
        if not name_input:
            showwarning(title='Alert', message='No input!')
            return

        if not description_input:
            showwarning(title='Alert', message='No input!')
            return

        if not price_input:
            showwarning(title='Alert', message='No input!')
            return

        #Saves all of the user inputs into an excel file
        with open('saved_text.csv', 'a', newline='') as f:
            w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.currency_entry.get()
            w.writerow([name, description, price])
        msg = "Item has been saved!"
        showwarning(title='Alert', message=msg)
        self.destroy()

#Creates all of the main windows variables (centers it, doesn't let it be resizeable, etc.)
root = Tk()
root.title('Merchandise Hub')
window_width = 350
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

#Configures how the button/label is placed
options = {'ipadx': 20, 'ipady': 20, 'padx': 20, 'pady': 20}

#Creates the add button
add_button = Button(root, text='Add')
add_button.bind('<Button>', lambda e: AddWindow(root))
add_button.pack(**options)

#Creates the edit and remove button
edit_button = Button(root, text='Edit and Delete')
edit_button.bind('<Button>', lambda e: EditWindow(root))
edit_button.pack(**options)

#Allows the program to be ran
mainloop()