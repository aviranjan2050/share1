def function():
    counter = 1

    while counter < 5:
        yield counter
        counter+=1

for x in function():
    print(x)

#generators are basically a set of numbers that are generated to use in our code.

#generators are used to create the list.

#here generating a list of even numbers

def even_numbers(x):
    for i in range(x+1):
        if i%2 ==0 :
            yield i

print(list(even_numbers(20)))