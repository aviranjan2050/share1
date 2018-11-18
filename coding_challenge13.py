class Multiply:
    def __init__(self,num1):
        print("this is operator overloading")
        self.num1 = num1


    def __mul__(self, other):
        num1 = self.num1 + other.num1
        return num1

Mul1 = Multiply(2)
Mul2 = Multiply(3)

print(Mul1 * Mul2)
