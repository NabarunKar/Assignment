def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def pro(a, b):
    return a*b


def div(a, b):
    return a/b


def expo(a, b):
    return a**b


while True:
    c = int(input("Enter first number: "))
    d = int(input("Enter second number: "))
    
    print("1.Add\t2.Subtract\t3.Multiply\n4.Divide\t5.Exponent\t6.Exit")
    p = int(input("Enter your choice: "))

    if(p == 1):
        print("Sum is: ", add(c, d))
    elif(p == 2):
        print("Difference is: ", sub(c, d))
    elif(p == 3):
        print("Product is: ", pro(c, d))
    elif(p == 4):
        print("Quotient is: ", div(c, d))
    elif(p == 5):
        print("Result: ", expo(c, d))
    elif(p == 6):
        break
    else:
        print("Incorrect input.")