rate = int(input("Enter rate per hour:"))
time = int(input("Hours worked:"))


if(time > 40):
    pay=rate*40
    newRate = 1.5*rate
    extra = (time-40)*newRate
    grosspay = pay+extra
    print("Gross pay is ", grosspay)
else:
    pay=rate*time
    print("Gross pay is ",pay)
