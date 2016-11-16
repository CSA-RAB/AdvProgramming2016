#Ryan Blaschke
#9/12/16
#Adv. Comp. Prog.

from tkinter import *
from tkinter import ttk


root=Tk()
root.title("Yes No")




def hi():
  ttk.Label(mainframe, text="Hi").grid(column=3, row=1, sticky=W)


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

var=IntVar()
yeschk=ttk.Checkbutton(mainframe, text="Yes", variable=var)
yeschk.grid(column=1, row=1)
var_two=IntVar()
nochk=ttk.Checkbutton(mainframe, text="No", variable=var_two)
nochk.grid(column=1, row=2)
hi_button=ttk.Button(mainframe, text="Hi", command=hi,state=DISABLED).grid(column=3, row=3, sticky=E)



if var.get() == 1:
  hi_button(['!disabled'])
  var_two=0
elif var_two.get() == 1:
  hi_button.state(['disabled'])
  var=0
  

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>',hi)
root.mainloop()




