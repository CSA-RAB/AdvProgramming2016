#Ryan Blaschke
#Advanced Computer Programming
#9/2/16


from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        a=open('items.txt','r')
        b=item.get().lower()
        price.set((value)+(value * .0825)+(shippingcost))
    except ValueError:
        pass


root = Tk()
root.title("Order Form")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

item = StringVar()
days = StringVar()


item_entry = ttk.Entry(mainframe, width=7, textvariable=item)
item_entry.grid(column=1, row=1, sticky=(W, E))
ship_entry = ttk.Entry(mainframe, width=2, textvariable=days)
ship_entry.grid(column=1, row=2, sticky=(W,E))

ttk.Label(mainframe, textvariable=price).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Calculate Price", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Item").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Shipping Days").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Price").grid(column=2, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

item_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
