def vol(l=1,b=1,h=1):
    return l*b*h


print("The default box volume in cubic units is: ",vol())
print("\nThe volume of a box with length 10,")
print("width 1 and height 1 in cubic units is: ",vol(10))
print("\nThe volume of a box with length 10,")
print("width 5 and height 1 in cubic units is: ",vol(10,5))
print("\nThe volume of a box with length 10,")
print("width 5 and height 2 in cubic units is: ",vol(10,5,2))