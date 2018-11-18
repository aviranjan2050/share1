class Mydata:
    __hidden = 10

    def add(self,increment):
       self. __hidden+=increment
       print(self.__hidden)

object1 = Mydata()
object1.add(5)
