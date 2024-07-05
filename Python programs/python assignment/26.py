a=int(input("Enter a number = "))

match a:
    case a if (a<=999 and a>=100):
        print("Three digit number")
    case a:
        print("Not a three digit")    