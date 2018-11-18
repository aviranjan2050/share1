newlist = [1,3,5,7,9,10,2]
#filtering the even number from the list
result = list(filter(lambda x:x%2==0 , newlist))
print(result)