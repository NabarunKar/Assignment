n = int(input("Enter number of students: "))
d = {}
z = []
for i in range(1, n+1):
    x = input("Enter name: ")
    y = input("Enter class: ")
    z = input("Enter subjects: ").split()
    d[x] = [y, z]
print("Entered data: ")
for key, values in d.items():
    print("Name: ", key, "\nClass :", values[0], "\nSubjects :", values[1])
    print()
d1 = {}
for key, val in d.items():
    if val not in d1.items():
        d1[key] = val
print("After deleting duplicate items: ")
for key, values in d1.items():
    print("Name: ", key, "\nClass: ", values[0], "\nSubjects: ", values[1])
    print()