from tkinter import *

root = Tk()

label1 = Label(root , text = "hello" , bg = "red" , fg = "white")
label1.pack(fill=X)

label2 = Label(root , text = "hi" , bg ="blue" , fg = "black")
label2.pack(side = LEFT,fill=Y)

root.mainloop()
