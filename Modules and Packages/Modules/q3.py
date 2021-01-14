import datetime
x = datetime.datetime.now()

print("year: ", x.year)
print("month: " , x.month)
print("day: " , x.day)




print("time: ",x.strftime("%X"))

print("date and time: " , x.strftime("%x") + "," , x.strftime("%X"))