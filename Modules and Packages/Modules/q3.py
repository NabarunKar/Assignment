from datetime import date

today = date.today()

# Year
d1 = today.strftime("%Y")
print("year:", d1)

# month	as number
d2 = today.strftime("%m")
print("month: ", d2)

# day
d3 = today.strftime("%d")
print("day: ", d3)

# time	
d4 = today.strftime("%X")
print("time: ", d4)