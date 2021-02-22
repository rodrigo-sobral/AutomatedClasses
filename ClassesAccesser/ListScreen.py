from tkinter import *
from tkinter import messagebox
from webbrowser import get

class CoursesWindow:
    LIST_COLORS= ["dark green", "dark blue", "red", "orange", "purple", "brown"]

    def __init__(self, database: dict):
        self.database= database
        self.window = Tk(className=' Classes Selector') 
        self.window.geometry('400x200+350+250')
        yscrollbar = Scrollbar(self.window) 
        yscrollbar.pack(side = RIGHT, fill = Y) 
        self.listing = Listbox(self.window, selectmode='unique', yscrollcommand = yscrollbar.set) 
        self.listing.pack(padx = 10, pady = 10, expand = YES, fill = "both") 
    
    def listingBox(self):
        counter=0
        for colorID, course in enumerate(self.database):
            for classtype in self.database[course]:
                self.listing.insert(END, course+' '+classtype)
                self.listing.itemconfig(counter, bg = self.LIST_COLORS[colorID], fg='white')
                counter+=1
        self.listing.bind("<<ListboxSelect>>", self.returnSelection)
    
    def returnSelection(self, event):
        selection = event.widget.curselection()
        if selection:
            class_selected = event.widget.get(selection[0])
            confirmation = messagebox.askyesno(title='Confirmation', message='Do you want to enter in {} meeting?'.format(class_selected))
            if confirmation: 
                class_selected= class_selected.split(' ')
                self.window.destroy()
                get(using=None).open(self.database[class_selected[0]][class_selected[1]], new=2)
