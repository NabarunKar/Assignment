import calendar
year=int(input("Enter a year: "))
print("First Monday dates of each month are: ")
print("Date       Month")
for month in range(1,13):
    cal=calendar.monthcalendar(year,month)
    week1=cal[0]
    week2=cal[1]
    if week1[calendar.MONDAY]!=0:
        day=week1[calendar.MONDAY]
    else:
        day=week2[calendar.MONDAY]
    print(f"  {day}       {calendar.month_name[month]}")