from tkinter import *

def function1():
    print("this is manu")

def setting():
    print("rebooting.....")

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File" , menu = submenu)

submenu.add_command(label="Project" , command = function1)
submenu.add_command(label = "save" , command = function1)
submenu.add_command(label = "settings" , command = setting)

submenu.add_separator()

submenu.add_command(label = "Exit" , command =root.quit)

newmenu = Menu(mymenu)

mymenu.add_cascade(label="view" , menu = newmenu)
newmenu.add_command(label = "pagelayout" , command = function1)

#creating a tool bar
toolbar = Frame(root , bg = "pink")
button1 = Button(toolbar, text = "insert Files" , command = function1)
button1.pack(side = LEFT , padx =2 , pady = 3)
button2 = Button(toolbar , text = "delete Files" , command = function1)
button2.pack(side=LEFT , padx =2 , pady =3)

toolbar.pack(side=TOP , fill = X)
#creating a status bar
status = Label(root , text ="your status...." , bd =1 , anchor = W , relief = SUNKEN)
status.pack(side = BOTTOM , fill =X)



root.mainloop()