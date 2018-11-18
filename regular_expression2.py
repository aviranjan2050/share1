import re

string = "hello ! my name is rob , hi rob "
pattern = r"rob"
newstring = re.sub(pattern , "John" , string)#finds the old string and replace with new one
print(newstring)