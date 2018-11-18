import function_argument

def BMI(W, H):

    BMI = W/(pow(H, 2))

    return BMI

Weight = float(input('enter weight'))
Height = float(input('enter height'))
print(BMI(Weight, Height))
