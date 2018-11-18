class Computer:
    def __init__(self,brand):
        print("this is supercomputer")
        self.brand = brand

    def GetSpecs(self):
        self.brand = input("enter brand")

    def DisplaySpecs(self):
        print("brand is "+self.brand)

class Laptop(Computer):
    def __init__(self,weight):
        print("this is laptop")
        self.weight = weight

    def GetWeight(self):
      self.weight = input("enter your weight")

    def DisplayWeight(self):
        print("weight is " +self.weight)

class Desktop(Computer):
    def __init__(self,price):
        print("this is desktop")
        self.price = price

    def GetPrice(self):
        self.price = input("enter your price")

    def DisplayPrice(self):
        print("price is"+self.price)

lap1 = Laptop('')
lap1.GetSpecs()
lap1.DisplaySpecs()
lap1.GetWeight()
lap1.DisplayWeight()


desk1 = Desktop(0)
desk1.GetSpecs()
desk1.DisplaySpecs()
desk1.GetPrice()
desk1.DisplayPrice()