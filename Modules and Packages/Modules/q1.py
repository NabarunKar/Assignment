import calendar

def leap(Year):
        
    if(calendar.isleap(Year)):
        print(str(Year) + " is a leap year.")
    else:
        print(str(Year) + " is not a leap year.")





Year=int(input("Enter the year: "))

leap(Year)
print("Leap years between 1900 and 2021 are: ")
for i in range(1900,2022):
    if(calendar.isleap(i)):
        print(i)
