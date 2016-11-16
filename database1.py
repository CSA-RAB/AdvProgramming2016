#Ryan Blaschke
#9/22/16
#Advanced Computer Programming




from tkinter import *
from tkinter import ttk

def filewrite(*args):
    csvfile=open('database.csv','a')
    csvfile.write(firstnamevar,lastnamevar,radiovar,statevar)
    csvfile.close()
    
    
    
root = Tk()
root.title("Entry Form")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

firstnamevar = StringVar()
first_name_entry = ttk.Entry(mainframe, width=7, textvariable=firstnamevar)
ttk.Label(mainframe, text="First:").grid(column=1, row=1, sticky=W)
first_name_entry.grid(column=2, row=1, sticky=(W, E))
lastnamevar = StringVar()
last_name_entry = ttk.Entry(mainframe, width=7, textvariable=lastnamevar)
ttk.Label(mainframe, text="Last:").grid(column=1, row=2, sticky=W)
last_name_entry.grid(column=2, row=2, sticky=(W, E))

radiovar = StringVar()
business = ttk.Radiobutton(root, text='Business', variable=radiovar, value='business')
business.grid(column=1, row=3)
resident = ttk.Radiobutton(root, text='Resident', variable=radiovar, value='resident')
resident.grid(column=2, row=3)
other = ttk.Radiobutton(root, text='Other', variable=radiovar, value='other')
other.grid(column=3, row=3)

statevar = StringVar()
state = ttk.Combobox(root, textvariable=statevar)
state.grid(column=1, row=4, sticky=W)
state['values'] = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachussetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
ttk.Label(mainframe, text="State").grid(column=2, row=4, sticky=W)

var=IntVar()
yeschk=ttk.Checkbutton(mainframe, text="Yes", variable=var, onvalue="yes")
yeschk.grid(column=1, row=5)
ttk.Label(mainframe, text="Accept Policy").grid(column=1, row=6, sticky=W)


ttk.Button(mainframe, text="Submit", command=filewrite).grid(column=2, row=6, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

first_name_entry.focus()
root.bind('<Return>', filewrite)

root.mainloop()

