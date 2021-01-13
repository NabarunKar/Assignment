import random
import math

def dieroll(number):
    lst= [0]*7

    for i in range(0,number):
        freq=int(random.randint(1,6))
        lst[freq]+=1

    return lst



res=dieroll(6000)
result= res[1:]

print("Frequency distribution: ")
print("Face  Number of Times")
for idx, val in enumerate(result):
    print(str(idx+1) + "    :    "+ str(val))