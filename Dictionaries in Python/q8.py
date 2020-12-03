old_dict={}
n=int(input("Enter the number of elements: "))
for i in range(1,n+1):
    x=str(input("Enter key: "))
    y=str(input("Enter number: "))
    old_dict[x]=y
new_dict = dict([(value, key) for key, value in old_dict.items()])  
print ("Original dictionary: ") 
print(old_dict)    
print()  
print ("Dictionary after swapping:  ")  
print("Keys : Values") 
for i in new_dict: 
    print(i, "  :  ", new_dict[i])