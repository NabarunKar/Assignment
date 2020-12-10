List1 = ["Mango","Melon","Barcelona","Cat","Armstrong","Debris","Come","Denver"]
print(List1)
x= input("Enter a starting letter: ")
y=str(x)
for s in List1:
    if s.startswith(y):
        print(s)