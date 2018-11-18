def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)


x=input("enter number")
print(fact(int(x)))