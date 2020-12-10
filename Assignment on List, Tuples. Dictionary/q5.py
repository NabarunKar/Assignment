n = [7,8,9,10,12,(14,28,36,37),41,52]
print("Given list: ",n)
count = 0
for i in n:
    if isinstance(i, tuple):
        break
    count=count+1
print("Number of elemnts before tuple: ",count)