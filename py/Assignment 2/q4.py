ch = input("Enter c for centigrade and f for fahrenheit: ")

if(ch == "c"):
    temp = float(input("enter temp.:"))
    f = ((temp/5)*9)+32
    print("Temp in fahrenheit is ",f)

elif(ch == "f"):
    temp = float(input("enter temp.:"))
    c = ((temp-32)*5)/9
    print("Temp in celcius is ",c)

