#Ryan Blaschke
#Advanced Computer Programming
#11/1/16
#travellog.py


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
########################

########################################################################
'''This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
##############################################################################

root = Tk()

def about():
    messagebox.showinfo(title="About", message="travellog.py Version .1")


def submitbtn():
    root.quit()

def clearbtn():
    root.destroy()



countries = ('United States Of America', 'Canada', 'Mexico', 'Spain', 'Germany', 'France', 'Italy', 'England', 'Japan', 'Russia')
topMenu = Menu(root)
root.config(menu=topMenu)
topMenu = Menu(root)
root.config(menu=topMenu)
subMenu = Menu(topMenu)
topMenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Exit",command=root.quit)
topMenu.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About",command=about)

l = Listbox(root, height=5)
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=0, row=0, sticky=(N,S))
l.grid(column=1, row=0, sticky=(N,W,E,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0, weight=1)
for x in countries:
    l.insert('end', '%s' % x)


p = ttk.Progressbar(root, orient=VERTICAL, length=200, mode='determinate', value=10)
p.grid(column=3,row=0, sticky=(N,S))
submit = ttk.Button(root, text="Submit", command=submitbtn)
clear = ttk.Button(root, text="Clear", command=clearbtn)
submit.grid(column=2, row=0)
clear.grid(column=2, row=1)
descriptionlbl = ttk.Label(root, text="Description")
descriptionlbl.grid(column=0, row=2)
t = Text(root, width=50, height=10)
t.grid(column=0, row=3)





root.mainloop()


