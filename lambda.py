def square(x):
    return x**2

print(square(10))

#alternative way to do it,lambdas are also called nameless functions as they have no name.

print((lambda x:x**2)(10))

print((lambda x:x*(x+5)^2)(5))