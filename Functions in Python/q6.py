def subject(name, sub):
    print(name, " likes to read: ")
    for i in range(0, len(sub)):
        print(sub[i])


name = input("Enter your name: ")
n = int(input("Enter the number of subjects you like: "))
sub = []
for i in range(0, n):
    sub_name = input("Enter subject name: ")
    sub.append(sub_name)

subject(name, sub)