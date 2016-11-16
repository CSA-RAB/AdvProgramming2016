from tkinter import *


def donothing():
    print("Ok ok i wont...")

root=Tk()

menu=Menu(root)
root.config(Menu=menu)

subMenu = Menu(menu)
menu.add_cascade(Label="file",menu=subMenu)


root.mainloop()
