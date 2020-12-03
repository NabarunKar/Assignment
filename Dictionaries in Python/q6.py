d = {}
n=int(input("Enter the number of elements: "))
for i in range(1,n+1):
    x=str(input("Enter element: "))
    y=str(input("Enter key: "))
    d[x]=y
if not bool(d):
    print("Dictionary is empty.")
else:
    print("Dictionary is not empty.")
