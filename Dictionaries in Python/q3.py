dic1={9:10, 11:20}
dic2={4:30, 7:80}
dic3={5:50,6:60}
print("Our dictionaries: ")
print(dic1)
print(dic2)
print(dic3)
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print("Concatenated dictionary: ")
print(dic4)