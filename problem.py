#Ryan Blaschke
#Advanced Computer Programming
#10/3/16


from tkinter import *
from tkinter import ttk

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_main()

    def create_main(self):
        self.title = ttk.Label(self, text=" Login ")
        self.title.grid(row=0, column=2)

        self.user_entry_label = ttk.Label(self, text="Username: ")
        self.user_entry_label.grid(row=1, column=1)

        self.user_entry = ttk.Entry(self)                        
        self.user_entry.grid(row=1, column=2)

        self.pass_entry_label = ttk.Label(self, text="Password: ")
        self.pass_entry_label.grid(row=2, column=1)

        self.pass_entry = ttk.Entry(self)                        
        self.pass_entry.grid(row=2, column=2)

        self.sign_in_button = ttk.Button(self, text="Sign In")
        self.sign_in_button.grid(row=5, column=2)
        def loggingin(self):
            user_get = self.user_entry.get().lower()
            pass_get = self.pass_entry.get().lower()
            
            if user_get == 'john':
              if pass_get == 'dude':
                self.loginsuccess = ttk.Label(self, text="Login Complete!")
                self.loginsuccess.grid(row=3, column=1)
                pass
              else:
                print("Login failed.")
                pass
            elif user_get == 'jane':
              if pass_get == 'hello':
                print("Login complete.")
                pass
              else:
                print("Login failed.")
                pass
            elif user_get == 'sam':
              if pass_get == 'argh':
                print("Login complete.")
                pass
              else:
                print("Login failed.")
                pass
            elif user_get == 'sally':
              if pass_get == 'woohoo':
                print("Login complete.")
                pass
              else:
                print("Login failed.")
                pass
            else:
              print("Login failed.")
              pass
                    




root = Tk()
root.title("Login")

app = Application(root)
root.mainloop()









 
