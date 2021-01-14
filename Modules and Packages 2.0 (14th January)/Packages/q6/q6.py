import F1
s=0
print("Function list:")
print("1: F(x,y)=F(x-y,y)+1, if y ≤ x")
print("2: F(n,r)=F(n-1,r)+F(n-1,r-1)")
print("3: F(n)=F(n/2)+1 if n>1")
print("4: F(M,N)=1 if M=0, or M ≥N ≥1, and F(M,N)=F(M-1,N)+F(M-1,N-1), otherwise.")
print("5: B(m,x)=m!/(x!(m-x)!) where m>x,B(0,0)=B(m,0)=1 and B(m,x)=B(m,x-1)*[(m-x+1)/x]")
i=int(input("Enter your choice: "))
if(i==1):
    a=int(input("Enter the value of x: "))
    b=int(input("Enter the value of y: "))
    s=s+F1.f1(a,b)
    print("Result: ",s)
elif(i==2):
    n=int(input("Enter the value of n: "))
    r=int(input("Enter the value of r: "))
    s=s+F1.f2(n,r)
    print("Result: ",s)
elif(i==3):
    n=int(input("Enter the value of n: "))
    s=s+F1.f3(n)
    print("Result: ",s)
elif(i==4):
    m=int(input("Enter the value of m: "))
    n=int(input("Enter the value of n: "))
    s=s+F1.f4(m,n)
    print("Result: ",s)
elif(i==5):
    m=int(input("Enter the value of m: "))
    x=int(input("Enter the value of x: "))
    s=s+F1.f5(m,x)
    print("Result: ",s)
else:
    print("Wrong input.")
