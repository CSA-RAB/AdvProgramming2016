#Ryan Blaschke
#9/20/16
#Advanced Computer Programming
#states

from tkinter import *
from tkinter import ttk

def greet(*args):                        #Hello <name> from <state> function
    ttk.Label(mainframe, text="Hello " + namevar.get() + " from " + statevar.get() + "!").grid(column=1, row=3)
    
    
    
root = Tk()
root.title("Name and State")   #Title

mainframe = ttk.Frame(root, padding="6 6 12 12")         #Frame design
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

namevar = StringVar()              #String variable for name
name_entry = ttk.Entry(mainframe, width=7, textvariable=namevar)    #Name entry bar
name_entry.grid(column=2, row=1, sticky=(W, E))        #Name entry place in grid

statevar = StringVar()                           #String variable for state
state = ttk.Combobox(root, textvariable=statevar)        #Combo box for state selection
state.grid(column=1, row=2)          #State entry place in grid
state['values'] = ('Texas', 'New York', 'California', 'Florida', 'Illinois')           #State choices



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)     

name_entry.focus()        #Focus towards name
state.bind('<<ComboboxSelected>>', greet)    #Run greet function when state is selected

root.mainloop()                #start
