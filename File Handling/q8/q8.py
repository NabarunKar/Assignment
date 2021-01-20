f = open("file1.txt", "r")
f1 = open("file2.txt", "w")
for line in f:
    w = line.split()
    w.reverse()
    for w1 in w:
        f1.write(w1)
        f1.write(" ")
f.close()
f1.close()
fp = open("file2.txt", "r")
data = fp.read()
print(data)
