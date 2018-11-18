X=1
odd = [X  for X in range(1,101,2)]
print(odd)

#solution
new_list = list(range(1, 100))

for x in new_list:

    if x % 2 != 0:
        print(x)