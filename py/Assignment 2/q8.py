hrs = input("Enter no.of hrs worked: ")
rate = input("Enter the rate per hour: ")

try:
    hrs = int(hrs)
    rate = int(rate)
    print("Total wage: ", hrs*rate)
except:
    print('Please enter a numeric value.')
