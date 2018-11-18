class student:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        self.name = input("enter your name")
        self.contact = input("enter your contact")

    def putdata(self):
        print("name is:"+self.name,"contact is :"+self.contact)

class scienceStudent(student):
    def __init__(self,age):
        self.age = age

    def science(self):
        print("i am a science student")

obj1 = scienceStudent(20)
obj1.science()
obj1.getdata()
obj1.putdata()