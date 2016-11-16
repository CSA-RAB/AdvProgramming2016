from tkinter import *


def donothing():
    print("Ok ok i wont...")

root=Tk()

topMenu=Menu(root)
root.config(menu=topMenu)

subMenu=Menu(topMenu)
topMenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project..",command=donothing)
subMenu.add_command(label="New...",command=donothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=root.quit)

editMenu=Menu(topMenu)
topMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo",command=donothing)

root.mainloop()
