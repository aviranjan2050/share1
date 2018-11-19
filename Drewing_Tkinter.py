from tkinter import *

root = Tk()

canvas = Canvas(root , height = 100 , width = 200)
canvas.pack()

newline = canvas.create_line(0,0,100,200)
otherline = canvas.create_line(1,1,300,400, fill= "green")

oval = canvas.create_oval(5,5,200,300,)

root.mainloop()
