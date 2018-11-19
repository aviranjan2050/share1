from tkinter import *

root = Tk()

def add():
    num1 = input("enter first number")
    num2 = input("enter second number")
    print(str(num1) + str(num2))

button1 = Button(root , text="click here" , command = add)
button1.pack()

root.mainloop()