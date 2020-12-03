d1={}
d2={}
for i in range(1,int(input("Enter number of items to convert to cm: "))+1):
    x=int(input("Enter length in metres: "))
    d1[x]=x*100
for i in range(1,int(input("Enter number of items to convert to m: "))+1):
    x=int(input("Enter length in centimeters:"))
    d2[x]=x/100
for key,values in d1.items():
    print(key,"m=",values,"cm")
for key,values in d2.items():
    print(key,"cm=",values,"m")