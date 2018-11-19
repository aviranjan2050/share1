from tkinter import *

import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("title", "this is first message")
response = tkinter.messagebox.askquestion("question1","Do you like coffee?")

if response == "yes":
    print("here is your coffee")

root.mainloop()