from tkinter import Tk, Label, Button

# Tkinter uses python classes. First we define out application as MyFirstGUI
class MyFirstGUI:
    def __init__(self, master):
        # self.master = master assigns the window to a variable that we can use
        self.master = master

        # master.title refers to the window's title
        master.title("My first GUI")

        # Add a label with some text
        self.label = Label(master, text="Look mom, I made a windows app!")
        self.label.pack()

        # Add a button. When clicked it will fire the 'greet' function
        self.greet_button = Button(master, text="PING!", command=self.greet)
        self.greet_button.pack()

        # Add a button. When clicked it will close the appliction due to master.quit
        self.close_button = Button(master, text="Close App", command=master.quit)
        self.close_button.pack()

    # greet function. When fired, it will print in the console the following message
    def greet(self):
        print("Congrats, you built your first GUI using python!")

# The following code allows our application to stay open by contantly running a loop
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

# Thomas Boccinfuso - www.tboccinfuso.com / www.twitter.com/BoccinfusoT