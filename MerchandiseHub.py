#Everything is subject to change, not all ideas/features have been implemented

#Imports everything needed for tkinter, and some extra modules
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning
import os, shutil

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

        #Defines all the padding for labels/entrys
        options1 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 5}
        options2 = {'ipadx': 35, 'ipady': 5, 'padx': 10, 'pady': 5}
        options3 = {'ipadx': 35, 'ipady': 30, 'padx': 10, 'pady': 5}
        options4 = {'ipadx': 20, 'ipady': 20, 'padx': 10, 'pady': 25}

        #Creates the "name" label area
        name = StringVar()
        name_label = Label(self, text='Name:')
        name_label.pack(anchor=NW, **options1)
        name_entry = Entry(self, textvariable=name)
        name_entry.pack(anchor=NW, **options2)

        #Creates the "description" label area
        description = StringVar()
        description_label = Label(self, text='Description:')
        description_label.pack(anchor=NW, **options1)
        description_entry = Entry(self, textvariable=description)
        description_entry.pack(anchor=NW, **options2)

        #Creates the "currency" label area
        currency = StringVar()
        currency_label = Label(self, text='Price:')
        currency_label.pack(anchor=NW, **options1)
        currency_entry = Entry(self, textvariable=currency)
        currency_entry.pack(anchor=NW, **options2)

        #Creates the "save" button
        save_button = Button(self, text='Save and Create', command=save_button_clicked)
        save_button.pack(anchor=S, **options4)

#Creates all of the main windows variables (centers it, doesn't let it be resizeable, etc.)
root = Tk()
root.title('Merchandise Hub')
window_width = 350
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

options = {'ipadx': 20, 'ipady': 20, 'padx': 20, 'pady': 20}

#Handles the save button in the add section
def save_button_clicked():
    """ Handle save button click event
    """
    msg = "Item has been saved!"
    showwarning( title='Alert', message=msg)

#Creates the add button
add_button = Button(root, text='Add')
add_button.bind('<Button>', lambda e: AddWindow(root))
add_button.pack(**options)

#Creates the edit button
edit_button = Button(root, text='Edit')
edit_button.pack(**options)

#Creates the delete button
delete_button = Button(root, text='Delete')
delete_button.pack(**options)

#Allows the program to be ran
mainloop()