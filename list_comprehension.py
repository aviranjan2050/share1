#we can set conditions in list

num = [x**2 for x in range(4)]
#num contains square of numbers from 0 to 3
print(num)

#num1 contains square of number from 0 to 9 who are even

num1 = [X**2 for X in range(9) if X**2 %2 == 0]
print(num1)