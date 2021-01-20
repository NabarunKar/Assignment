import filecmp
file1 = "demofile.txt"
file2 = "file2.txt"
comp = filecmp.cmp(file1, file2)
print(comp)
