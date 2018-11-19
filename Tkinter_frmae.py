from tkinter import *

root = Tk()

frame1 = Frame(root)

frame1.pack()

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button1 = Button(frame1 , text = "click here" , fg = "red")
button2 = Button(frame2 , text = "click here" , fg = "blue")

button1.pack()
button2.pack()

root.mainloop()
