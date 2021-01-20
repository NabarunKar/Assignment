fin = open("demo.txt", 'r')
fout = open("copy.txt", 'w')
d = fin.read()
for i in d:
    fout.write(i)
fin.close()
fout.close()
print("Content has been copied.")
