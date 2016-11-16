#Ryan Blaschke
#9/16/16
#Adv. Comp. Prog.

from tkinter import *
from tkinter import ttk

    
def Submit(*args):
    mainframe.destroy()
    
    
    
    
    

def deletename(*args):
    name.delete(0,END)


def deleteage(*args):
    age.delete(0,END)
    
       





root = Tk()
root.title("Name Age Gender")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

name = StringVar()
age = IntVar()

name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
name_entry.insert(0, 'username')
name_entry.grid(column=1, row=1, sticky=(W, E))
age_entry = ttk.Entry(mainframe, width=7, textvariable=age)
age_entry.grid(column=1, row=2, sticky=(W, E))


gender=StringVar()

male = ttk.Radiobutton(root, text='Male', variable=gender, value='male')
male.grid(column=1, row=3)
female = ttk.Radiobutton(root, text='Female', variable=gender, value='female')
female.grid(column=2, row=3)
other = ttk.Radiobutton(root, text='Other', variable=gender, value='other')
other.grid(column=3, row=3)

ttk.Button(mainframe, text="Submit", command=Submit).grid(column=3, row=4, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

name_entry.focus()

age.bind("<Button-1>", deleteage)
name.bind("<Button-1>", deletename)
root.bind('<Return>', Submit)

root.mainloop()
