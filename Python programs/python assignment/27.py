a=int(input("Enter a number = "))
match(a):
    case a if (a<0):
        print("Negative")
    case a if(a>0):
        print("Positive")
    case a:
        print("Zero")  