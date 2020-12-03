dict = {'a':9, 'b':3, 'c': 100}

max = max(dict.keys(), key=(lambda k: dict[k]))
min = min(dict.keys(), key=(lambda k: dict[k]))

print('Maximum Value: ',dict[max])
print('Minimum Value: ',dict[min])
