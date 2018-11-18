def discount(price):
    return price*90/100

price_list = [10,20,30,40,50]

print(list(map(discount, price_list)))

f = lambda x,y:x+y
print(f(1,1))