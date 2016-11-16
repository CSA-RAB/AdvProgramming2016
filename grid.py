#Ryan Blaschke
#10/7/16

from tkinter import *
from tkinter import ttk


def successful(*args):
    user_entry.delete(0,END)
    pass_entry.delete(0,END)


root=Tk()

topMenu=Menu(root)
root.config(menu=topMenu)
subMenu=Menu(topMenu)
topMenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Exit",command=root.quit)


mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="Username:").grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text="Password:").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="         ").grid(column=2, row=0, sticky=W)
ttk.Label(mainframe, text="         ").grid(column=2, row=1, sticky=W)

username = StringVar()
password = StringVar()

user_entry = ttk.Entry(mainframe, width=7, textvariable=username)
user_entry.grid(column=1, row=0, sticky=(W, E))
pass_entry = ttk.Entry(mainframe, width=7, show="*", textvariable=password)
pass_entry.grid(column=1, row=1, sticky=(W, E))

login=ttk.Button(mainframe, text="Login", command=successful)
login.grid(column=1, row=2, columnspan=2, sticky=W)




for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

user_entry.focus()
root.bind('<Return>', successful)

root.mainloop()
