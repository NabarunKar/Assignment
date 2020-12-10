Birthdays={'Jack':"15/4/2001",
           'Ian':"20/03/2000",
           'Jake': "9/2/2001",
           'Aditya':"1/05/2003",
           'Kate':"24/12/2002",
           'Jerry':'11/08/2001'}

print("Names in sorted order: ")
for key in sorted(Birthdays.keys()):
    print(key)

query = input("Whose birthday do you want to look up? ")
result = Birthdays[query] if query in Birthdays else None
if  result == None:
#    print("Enter the record ?")
    d={}
    for i in range(1):
        keys = input('Enter the name ')
        values = input('Enter the Birthday in DD/MM/YY format: ')
        d[keys] = values
    Birthdays.update(d)
    print("Birthday Added.")
    print("{}'s birthday is {}".format(query, Birthdays[query]))
else:
    print("{}'s birthday is on {}".format(query, Birthdays[query]))