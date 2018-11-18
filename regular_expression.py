import re

pattern = r"avinash"

if re.match(pattern , "avinashranjansunny"):  #returns true only if string starts with pattern
    print("match found")

else:
    print("match not found")

pattern = r"sunny"


if re.search(pattern ,"avinashranjansunny"): #returns true if pattern is found anywhere
    print("match found")

else:
    print("match not found")

print(re.findall(pattern , "sunnyranjansunnyavinash")) #prints all the string that are present in given string