#Ryan Blaschke
#9/29/16

from tkinter import *


def donothing():    #default function
    print("Ok ok i wont...")

root=Tk()

topMenu=Menu(root)

#create menus and submenus

root.config(menu=topMenu)

subMenu=Menu(topMenu)
topMenu.add_cascade(label="Exit",menu=subMenu)
topMenu.add_cascade(label="Forgot password")
editMenu=Menu(topMenu)
topMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo",command=donothing)

#toolbar

toolbar=Frame(root,bg="blue")
insertBtn=Button(toolbar, text="Insert Image", command=donothing)
insertBtn.pack(side=LEFT,padx=2,pady=2)
printBtn=Button(toolbar,text="Print",command=donothing)
printBtn.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

root.mainloop()
