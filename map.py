def add(x):
    return x+2
newlist = [10,20,30,40,50]

result = list(map(add,newlist))
print(result)

#map function is used here to add 2 to each element of newlist.and result has been typecasted to list.

#we can also use lambda instead of fucntion add.

result1 = list(map(lambda x:x**2,newlist ))
print(result1)