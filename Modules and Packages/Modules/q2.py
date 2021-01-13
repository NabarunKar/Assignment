import calendar


year=int(input('Enter the year: '))

print("YEAR: ", year)
print("Dates of the first Monday for each month are: ")
for month in range(1,13):
    mycal=calendar.monthcalendar(year,month)

    week1= mycal[0]
    week2= mycal[1]

    if week1[calendar.MONDAY]!=0:
        Monday=week1[calendar.MONDAY]
    else:
        Monday=week2[calendar.MONDAY]
    
    print("%10s " % calendar.month_name[month] + "        Day: %2d"  % Monday)      