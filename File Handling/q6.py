f = open("demofile.txt")
c = 0
d = f.read()
l = d.split()
for i in l:
    if i:
        c = c+1
print(" Number of words: ",c)