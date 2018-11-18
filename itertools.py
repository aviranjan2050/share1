from itertools import count
from itertools import accumulate,takewhile
for i in count(3):
    print(i)

    if i >= 20:
        break

#count will count from 3 to infinity if no conditions are given

numbers = list(accumulate(range(8)))
print(numbers)
#accumulate accumulates the number along way by adding the next number

print(list(takewhile(lambda x:x<=10 , numbers)))
#takewhile function
