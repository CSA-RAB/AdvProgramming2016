#Ryan Blaschke
#10/4/16

from tkinter import *
from tkinter import ttk


def successful(*args):
    ttk.Label(mainframe, text="Login Success").grid(column=2, row=4, sticky=W)

root=Tk()

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="Username:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Password:").grid(column=1, row=2, sticky=W)


username = StringVar()
password = StringVar()

user_entry = ttk.Entry(mainframe, width=7, textvariable=username)
user_entry.grid(column=2, row=1, sticky=(W, E))
pass_entry = ttk.Entry(mainframe, width=7, show="*", textvariable=password)
pass_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Login", command=successful).grid(column=2, row=3, sticky=W)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

user_entry.focus()
root.bind('<Return>', successful)

root.mainloop()
