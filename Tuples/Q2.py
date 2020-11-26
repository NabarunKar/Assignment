def linearsearch(num,n):
    for i in range(len(num)):
        if(num[i]==n):
            return i+1
    return -1
def binarysearch(num,low,high,n):
    
    while(low<=high):
        mid=(low+high)//2
        if(num[mid]==n):
           return mid
        elif(num[mid]>n):
            high=mid-1
        else:
            low=mid+1
    return -1
num=tuple(map(int,input("Enter the elements : ").split()))
n=int(input("Enter element to search : "))
choice=int(input("1. Linear search\n2. Binary search\nEnter choice : "))
if choice==1:
    if(linearsearch(num,n)==-1):
        print(n,"not found")
    else:
        print(n,"found at",linearsearch(num,n),"position")
elif choice==2:
    if(binarysearch(num,0,len(num)-1,n)==-1):
        print(n,"not found")
    else:
        print(n,"found at",binarysearch(num,0,len(num)-1,n)+1,"position")
else:
    print("Wrong choice")
