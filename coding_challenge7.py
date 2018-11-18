def product(product_name):
    catalogue = {

        "poatato":100,
        "tomato":200,
        "banana":300,
        "orange":400,
        "grapes":500

    }

    print(catalogue.get(product_name,"product not available"))


product_name = input("enter product")
product(product_name)

#solution
products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
newproduct = input('Enter product name')
if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
