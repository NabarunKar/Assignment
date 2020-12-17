def factorial(n):
    res =1
    for i in range(1 , n +1):
        res*=i

    return res
n=int(input("Enter value of n: "))
r=int(input("Enter value of r: "))

ncr= int((factorial(n)/(factorial(n-r)*factorial(r) )))

print("Result: ",ncr)