from tkinter import *
from tkinter import ttk
from tkinter import messagebox

########################
#Ryan Blaschke
#Advanced Computer Programming
#10/12/16
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
root.title("Battle")


def about():
    messagebox.showinfo(title="About", message="battle.py Version .1")
def fight():
    ttk.Label(mainframe, text="Attack:40 ").grid(column=0, row=5, sticky=W)
    ttk.Label(mainframe, text="Defense:50 ").grid(column=0, row=6, sticky=W)
    ttk.Label(mainframe, text="Health:60 ").grid(column=0, row=7, sticky=W)
    ttk.Label(mainframe, text="Attack:20 ").grid(column=2, row=5, sticky=E)
    ttk.Label(mainframe, text="Defense:25 ").grid(column=2, row=6, sticky=E)
    ttk.Label(mainframe, text="Health:30 ").grid(column=2, row=7, sticky=E)
    ttk.Label(mainframe, text="Player 1 Wins!").grid(column=1, row=8)
    ttk.Label(mainframe, text="Player 2 Loses!").grid(column=1, row=9)
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

topMenu = Menu(root)
root.config(menu=topMenu)
topMenu = Menu(root)
root.config(menu=topMenu)
subMenu = Menu(topMenu)
topMenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Exit",command=root.quit)
topMenu.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About",command=about)

player_one_cardnames=('Card 1 P1', 'Card 2 P1', 'Card 3 P1')
player_two_cardnames=('Card 1 P2', 'Card 2 P2', 'Card 3 P2')
card_names_one=StringVar(value=player_one_cardnames)
card_names_two=StringVar(value=player_two_cardnames)
player_one_listbox=Listbox(mainframe, listvariable=card_names_one, height=3)
player_two_listbox=Listbox(mainframe, listvariable=card_names_two, height=3)

player_one_listbox.grid(column=0, row=1, rowspan=3, sticky=W)
player_two_listbox.grid(column=2, row=1, rowspan=3, sticky=E)
ttk.Label(mainframe, text="-------Wins").grid(column=1, row=8, sticky=N)

ttk.Label(mainframe, text="-------Loses").grid(column=1, row=9, sticky=N)

fight=ttk.Button(mainframe, text="Fight", command=fight)
fight.grid(column=1, row=3)

ttk.Label(mainframe, text="Stats").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, text="     ").grid(column=1, row=4)
ttk.Label(mainframe, text="Stats").grid(column=2, row=4, sticky=E)

root.mainloop()
