a=int(input("Enter year number = "))
if(a%100==0):
    if(a%400==0):
        print("leap year")
    else:
        print("Not a leap year")
else:
    if(a%4==0):
        print("Leap year")
    else:
        print("Not a leap year")     