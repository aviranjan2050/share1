def divison(dividend , divisor):
    try:
        print(dividend/divisor)

    except ZeroDivisionError:
        print("division by zero is not allowed")

dividend = float(input("enter dividend"))
divisor = float(input("enter divisor"))
divison(dividend, divisor)