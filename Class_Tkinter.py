from tkinter import *

class MyButtons:

    def __init__(self,rootone):

        frame = Frame(rootone)
        frame.pack()
        self.button1 = Button(frame , text = "clickhere" , command = self.printMessage)
        self.button1.pack()
        self.button2 = Button(frame , text = "Exit" , command = frame.quit)
        self.button2.pack(side=LEFT)


    def printMessage(self):
        print("this is a classic tkinter")



root = Tk()
Mybutton1 = MyButtons(root)
root.mainloop()
