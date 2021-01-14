def f1(x,y):
    if(y>x):
        return 0
    else:
        return (f1(x-y,y)+1)

#print(f1(2,1))

def f2(n,r):
    if(n==0):
        return r
    elif(r==0):
       return r
    else:
        return (f2(n-1,r)+f2(n-1,r-1))
def f3(n):
    if(n<=1):
        return 0
    else:
        return (f3(n/2)+1)
def f4(m,n):
    if(m==0 or (m>=n and m>=1 and n>=1)):
        return 1
    else:
        return (f4(m-1,n)+f4(m-1,n-1))
import math
def f5(m,x):
    if(m>x):
        return math.factorial(m)/(math.factorial(x)*math.factorial(m-x))
    elif((m==0 and x==0) or (m!=0 and x==0)):
        return 1
    else:
        return f5(m,x-1)*((m-x+1)/x)