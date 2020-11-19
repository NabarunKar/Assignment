def compare(ls1,ls2):
    num=sum(a==b for a,b in zip(ls1,ls2))
    return num==len(ls1)==len(ls2)

def difference(ls1,ls2):

    print([x for x in ls1 if x not in set(ls2)])


ls1=[18,19,20,21,22,23]
ls2=[20,21,22,23,24,25]

res=compare(ls1,ls2)
if res==False:
    print("The lists are different. Difference:  ")
    difference(ls1,ls2)
else:
    print("Both lists are same!")
