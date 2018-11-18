def division(a , b):

    result = 0
    try:

        result = a/b
    except ZeroDivisionError:
        print("division by zero not allowed")
    finally:
        print("this is getting executed no matter what")
    print(result)

division(4,0)

