num = 0
total = 0.0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        num1 = float(number)
    except:
        print('Invalid Input')
        continue
    num = num+1
    tot = total + num1
print('All done')
print("Total = ", total)
print("Count = ", num)
print("Average = ", total/num)