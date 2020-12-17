def gcd(x, y):
    while(y):
        x, y = y, x % y

    return x


arr = []
n = int(input("Enter the limit: "))

for i in range(0, n):
    num = int(input("Enter the number: "))
    arr.append(num)

num1 = arr[0]
num2 = arr[1]
result = gcd(num1, num2)

for i in range(2, len(arr)):
    result = gcd(result, arr[i])

print("GCD: ",result)