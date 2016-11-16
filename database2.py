#Ryan Blaschke
#Advanced Computer Programming
#11/4/16
#database2.py
#Version .2

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
root.title(string="Database")

#function for about button
def about():
    messagebox.showinfo(title="Version.2", message="database program for ordering and shipping items")


#function for writing file when clicking submit
def filewrite():
    if povar.get():
        if firstnamevar.get():
            if lastnamevar.get():
                if streetvar.get():
                    if streetnametwovar.get():
                        if statevar.get():
                            if cityvar.get():
                                if zipvar.get():
                                    if pricevar.get():
                                        if shipdaysvar.get():
                                            if monthvar.get():
                                                if dayvar.get():
                                                    if yearvar.get():
                                                        shipdays = shipdaysvar.get()
                                                        newtotalvar = 5 - shipdays
                                                        newtotalcostlabel = ttk.Label(root, text="$", textvariable=newtotalvar)
                                                        newtotalcostlabel.grid(column=6, row=3, sticky=W)
                                                        a = open('fileorder.csv', 'a')
                                                        a.write(povar)
                                                        a.write(firstnamevar)
                                                        a.write(lastnamevar)
                                                        a.write(streetvar)
                                                        a.write(streetnametwovar)
                                                        a.write(statevar)
                                                        a.write(cityvar)
                                                        a.write(zipvar)
                                                        a.write(pricevar)
                                                        a.write(shipdaysvar)
                                                        a.write(totalvar)
                                                        a.write(monthvar)
                                                        a.write(dayvar)
                                                        a.write(yearvar)
                                                        a.close()
                                                        firstnameentry.insert(0, END)
                                                        lastnameentry.insert(0, END)
                                                        streetnameentry.insert(0, END)
                                                        streetnametwoentry.insert(0, END)
                                                        state.set('')
                                                        citynameentry.insert(0, END)
                                                        zipentry.insert(0, END)
                                                        priceentry.insert(0, END)
                                                        shipdaysentry.set('')
                                                        monthentry.set('')
                                                        dayentry.set('')
                                                        yearentry.set('')
                                                    else:
                                                        messagebox.showinfo(title="Error:No year entered.",message="Please enter the year.")
                                                else:
                                                    messagebox.showinfo(title="Error:No day entered.",message="Please enter the day.")
                                            else:
                                                messagebox.showinfo(title="Error:No month entered.", message="Please enter the month.")
                                        else:
                                            messagebox.showinfo(title="Error:No shipping days entered.", message="Please enter the shipping days.")
                                    else:
                                        messagebox.showinfo(title="Error:No price entered.", message="Please enter the price.")
                                else:
                                    messagebox.showinfo(title="Error:No zip entered.", message="Please enter the zip.")
                            else:
                                messagebox.showinfo(title="Error:No city entered.", message="Please enter the city.")
                        else:
                            messagebox.showinfo(title="Error:No state entered.", message="Please enter the state.")
                    else:
                        if streetvar.get():
                            pass
                        else:
                            messagebox.showinfo(title="Error:No street entered.", message="Please enter the street.")
                else:
                    if streetnametwovar.get():
                        pass
                    else:
                        messagebox.showinfo(title="Error:No street entered.", message="Please enter the street.")
            else:
                messagebox.showinfo(title="Error:No last name entered.", message="Please enter the last name.")
        else:
            messagebox.showinfo(title="Error:No first name entered.", message="Please enter the first name.")
    else:
        messagebox.showinfo(title="Error:No PO number entered.", message="Please enter the PO number.")


#instructions on how to use program
def instructions():
    messagebox.showinfo(title="Instructions", message="Enter all applicable data into the boxes with their corresponding labels, then press submit to wirte your info in, or press retrieve after entering your PO number to autofill your info if you have already put your info in before")


#function for retrieving data previously entered when clicking retrieve, if no PO number is entered than error message box appears
def retrievebtn():
    if not povar.get():
        messagebox.showinfo(title="Error:No PO Number entered.", message="Please enter the PO number.")
    else:
        firstnameentry.setvar(firstnamevar)
        lastnameentry.setvar(lastnamevar)
        streetnameentry.setvar(streetvar)
        streetnametwoentry.setvar(streetnametwovar)
        state.set(statevar)
        citynameentry.setvar(cityvar)
        zipentry.setvar(zipvar)
        priceentry.insert(0, END)
        shipdaysentry.set('')
        monthentry.set('')
        dayentry.set('')
        yearentry.set('')
#menus
##File menu
TopMenu = Menu(root)
root.config(menu=TopMenu)
SubMenu = Menu(TopMenu)
TopMenu.add_cascade(label="File", menu=SubMenu)
SubMenu.add_command(label="Exit", command=root.quit)

#Help Menu
HelpMenu = Menu(TopMenu)
TopMenu.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About", command=about)
HelpMenu.add_command(label="Instructions", command=instructions)

#Creating all variables for later use
povar = IntVar()
firstnamevar = StringVar()
lastnamevar = StringVar()
streetvar = StringVar()
streetnametwovar = StringVar()
statevar = StringVar()
cityvar = StringVar()
zipvar = IntVar()
pricevar = IntVar()
shipdaysvar = IntVar()
totalvar = IntVar()
monthvar = IntVar()
dayvar = IntVar()
yearvar = IntVar()

#P.O Entry
poentry = ttk.Entry(root, width=20, textvariable=povar)
poentry.grid(column=0, row=0, sticky=E)
polabel = ttk.Label(root, text="P.O")
polabel.grid(column=1, row=0, sticky=W)

#First name entry
firstnameentry = ttk.Entry(root, width=20, textvariable=firstnamevar)
firstnameentry.grid(column=0, row=1, sticky=E)
firstnamelabel = ttk.Label(root, text="First")
firstnamelabel.grid(column=1, row=1, sticky=W)

#Last name entry
lastnameentry = ttk.Entry(root, width=20, textvariable=lastnamevar)
lastnameentry.grid(column=0, row=2, sticky=E)
lastnamelabel = ttk.Label(root, text="Last")
lastnamelabel.grid(column=1, row=2, sticky=W)

#Street name entry
streetnameentry = ttk.Entry(root, width=20, textvariable=streetvar)
streetnameentry.grid(column=0, row=3, sticky=E)
streetnamelabel = ttk.Label(root, text="Street")
streetnamelabel.grid(column=1, row=3, sticky=W)

#Street name two entry(not required as it is only for business locations)
streetnametwoentry = ttk.Entry(root, width=20, textvariable=streetnametwovar)
streetnametwoentry.grid(column=0, row=4, sticky=E)
streetnametwolabel = ttk.Label(root, text="Street(2)")
streetnametwolabel.grid(column=1, row=4, sticky=W)

#State combobox entry
state = ttk.Combobox(root, textvariable=statevar)
state.grid(column=0, row=5, sticky=E)
state['values'] = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'D.C', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachussetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
statelabel = ttk.Label(root, text="State")
statelabel.grid(column=1, row=5, sticky=W)

#City name entry
citynameentry = ttk.Entry(root, width=5, textvariable=cityvar)
citynameentry.grid(column=2, row=5, sticky=E)
citynamelabel = ttk.Label(root, text="City")
citynamelabel.grid(column=3, row=5, sticky=W)

#Zip code entry
zipentry = ttk.Entry(root, width=20, textvariable=zipvar)
zipentry.grid(column=0, row=6, sticky=E)
ziplabel = ttk.Label(root, text="Zip")
ziplabel.grid(column=1, row=6, sticky=W)

#Box for list of purchases
t = Text(root, width=20, height=10)
t.grid(column=0, row=7, sticky=E)
descriptionlbl = ttk.Label(root, text="Description")
descriptionlbl.grid(column=1, row=7, sticky=W)

#Price entry
pricelabel = ttk.Label(root, text="Price")
pricelabel.grid(column=5, row=0, sticky=E)
priceentry = ttk.Entry(root, width=10, textvariable=pricevar)
priceentry.grid(column=6, row=0, sticky=W)

#Tax label and its amount label
taxlabel = ttk.Label(root, text="Tax")
taxlabel.grid(column=5, row=1, sticky=E)
taxamountlabel = ttk.Label(root, text="8.25%")
taxamountlabel.grid(column=6, row=1, sticky=W)

#Shipping days entry
shipdayslabel = ttk.Label(root, text="Shipping Days")
shipdayslabel.grid(column=5, row=2, sticky=E)
shipdaysentry = ttk.Combobox(root, textvariable=shipdaysvar)
shipdaysentry.grid(column=6, row=2, sticky=E)
shipdaysentry['values'] = ('1', '2', '3', '4', '5')

#Total label
totallabel = ttk.Label(root, text="Total")
totallabel.grid(column=5, row=3, sticky=E)
totalcostlabel = ttk.Label(root, text="$")
totalcostlabel.grid(column=6, row=3, sticky=W)

#Month label
monthslabel = ttk.Label(root, text="Month")
monthslabel.grid(column=5, row=4, sticky=E)

#Day label
daylabel = ttk.Label(root, text="Days")
daylabel.grid(column=6, row=4, sticky=E)

#Year label
yearlabel = ttk.Label(root, text="Year")
yearlabel.grid(column=7, row=4, sticky=E)

#Month entry combobox
monthentry = ttk.Combobox(root, textvariable=monthvar)
monthentry.grid(column=5, row=5, sticky=E)
monthentry['values'] = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

#Day entry combobox
dayentry = ttk.Combobox(root, textvariable=dayvar)
dayentry.grid(column=6, row=5, sticky=E)
dayentry['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')

#Year entry combobox
yearentry = ttk.Combobox(root, textvariable=yearvar)
yearentry.grid(column=7, row=5, sticky=E)
yearentry['values'] = ('2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040')

#Submit and Retrieve buttons
ttk.Button(root, text="Submit", command=filewrite).grid(column=5, row=6, sticky=E)
ttk.Button(root, text="Retrieve", command=retrievebtn).grid(column=5, row=7, sticky=E)

#Bind Enter key to Submit button
root.bind('<Return>', filewrite)


#Run whole loop
root.mainloop()
