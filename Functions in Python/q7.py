def SI(p, t, ch):
    print('The principal is: ', p)
    print('The time period is: ', t)
    if(ch=='y'):
        r=12
        print("The interest rate is:  " + str(r) + "%")
    elif(ch=='n'):
        r=10
        print("The interest rate is:  " + str(r) + "%")
    si = (p * t * r) / 100

    print('The Simple Interest is Rs', si)



p=int(input("Enter the principal amount: "))
t=int(input("Enter the time period in years: "))

ch=input("Press Y if you are a senior citizen and N if not  ")
ch=ch.lower()
SI(p,t,ch)