a = int(input("Enter a number: "))
b = int(input("Enter another no: "))
c = int(input("Enter another no: "))

if(a > b and a > c):
    print(a, " is max")
elif (b > a and b > c):
    print(b, " is max")
else:
    print(c, " is max")


if(a < b and a < c):
    print(a, " is min")
elif (b < a and b < c):
    print(b, " is min")
else:
    print(c, " is min")