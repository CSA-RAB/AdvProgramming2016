
from tkinter import *
from tkinter import ttk
root = Tk()
l = Listbox(root, height=5)
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=0, row=0, sticky=(N,S))
l.grid(column=0, row=0, sticky=(N,W,E,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)

p = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate', value=10)
p.grid(column=0,row=2, sticky=(N,S))
root.mainloop()
