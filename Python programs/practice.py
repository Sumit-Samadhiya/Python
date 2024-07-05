''' 
a=int(input("Enter first number : "))
b=int(input("Enter the Second Number : "))
c=a+b
print("Sum of = ",c)   

Output : 
Enter first number : 12
Enter the Second Number : 13
Sum of =  25 '''






'''  
a=int(input("Enter Number = "))
b=a**2
print("Squre = ",b)

Output :
Enter Number = 13
Squre =  169    '''




''' 

a=int(input("Enter Value = "))
b=int(input("Enter Value = "))
c=a/b
print("Bhagfal = ",c)
c=a%b
print("Remender = ",c)
c=a//b
print("Bhagfal(int) = ",c)

Output :
Enter Value = 14
Enter Value = 2
Bhagfal =  7.0
Remender =  0
Bhagfal(int) =  7     '''



'''   

a=int(input("Enter Value = "))
b=int(input("Enter Value = "))
c=a<b
print("Less than = ",c)
c=a>b
print("Greater than = ",c)
c=a==b
print("Equle = ",c)
c=a<=b
print("Less than equal = ",c)
c=a>=b
print("Greater than equal = ",c)

Output :
Enter Value = 12
Enter Value = 13
Less than =  True
Greater than =  False
Equle =  False
Less than equal =  True
Greater than equal =  False     '''



'''  

age= int(input("Enter Your age = "))
if(age<=25 and age>=18) :
    print("eligibal ")
else :
    print("Not eligibal ")

Output :
Enter Your age = 14
Not eligibal
Enter Your age = 24
eligibal     '''




'''  

a=input("Enter First name = ")
b=input("Enter last name = ")
c=a+" "+b
print("Your name = ",c)

Output :
Enter First name = Sumit
Enter last name = Samadhiya
Your name =  Sumit Samadhiya     '''



'''  

a=input("Enter :- ")
b=int(input("How-Many times you want to Print = "))
print("Repeat string :- ", a*b) 

Output :-
Enter :- Sumit Samadhiya
How-Many times you want to Print = 5
Repeat string :-  Sumit Samadhiya  Sumit Samadhiya  Sumit Samadhiya  Sumit Samadhiya  Sumit Samadhiya   '''



'''  

a=int(input("Enter Value :- "))
b=int(input("Enter Value :- "))
c=a+b
print("Sum of",a," and ",b, "is ",c)

Output:- 
Enter Value :- 100
Enter Value :- 20
Sum of 100  and  20 is  120    '''



'''   

a=100
b=200
c=a+b
print(a,b,c, sep=",")

Output:-
100,200,300    '''


''' 
a=100
b=200
c=a+b
print(a,b,c, sep="\n")

Output :-
100
200
300   '''


''' 

a=10000
b=200
c=a+b
print(" %d %d %d" %(a,b,c))

Output :-
10000 200 10200     '''



'''  
a=10000
b=500
c=50
d=a+b+c
print(" %10d\n %10d\n %10d\n-----------------\n %10d"%(a,b,c,d))

Output :-
      10000
        500
         50
-----------------
      10550          '''


'''  

print("Hello")
print("Hi")
print("Bye")

Output :-
Hello
Hi
Bye           '''



'''  

print("Hello", end=' ')
print("Hi", end=' ')
print("Bye")

Output :-
Hello Hi Bye           '''




'''   

# Control Statement :-

rate=int(input("Enter rate = "))
qut=int(input("Enter quatity = "))
amt=rate*qut
print("Amount :- " , amt)
if(amt>=10000) :
    dis=amt*10/100
    net=amt-dis
    print("Discount[10%] = ",dis, "\nNet Amount = ", net)
else :
    dis = amt*5/10
    net=amt-dis
    print("Discount[5%] = ",dis, "Net Amount = ",net)  

Output :- 
Enter rate = 2000
Enter quatity = 23
Amount :-  46000
Discount[10%] =  4600.0
Net Amount =  41400.0       '''



''' 

rate=int(input("Enter the Rate = "))
qut=int(input("Enter the Quantity = "))
amt= rate * qut
print("Amount = ", amt)
if(amt>=100000) :
    dis=amt*30/100
    net=amt-dis
    print("Discount[30%] = ",dis, "Net Amount = " ,net)
elif(amt>=80000) :
    dis=amt*25/100
    net=amt-dis
    print("Discount[25%] = ",dis, "Net Amount = " ,net)
elif(amt>=50000)  :
    dis=amt*15/100
    net=amt-dis
    print("Dicount[15%] = ",dis, "Net Amount = ",net)
elif(amt>=20000)  :
    dis=amt*10/100
    net=amt-dis
    print("Dicount[10%] = ",dis, "Net Amount = ",net)
elif(amt>=10000)  :
    dis=amt*5/100
    net=amt-dis
    print("Dicount[5%] = ",dis, "Net Amount = ",net)
else :
    print("Dicount[0%] ", "Total Amount = ",amt)

    
Output :- 
Enter the Rate = 2000
Enter the Quantity = 4
Amount =  8000
Dicount[0%]  Total Amount =  8000

Enter the Rate = 125000
Enter the Quantity = 1
Amount =  125000
Discount[30%] =  37500.0 Net Amount =  87500.0     '''



''' 

marks=int(input("Enter Your Marks : "))

if(marks>=100) :
    print("Excelent")
elif(marks>=80 and marks<100):
    print("Topper")
elif(marks>=60 and marks<80):
    print("Good")
elif(marks>=33 and marks<60):
    print("Passing Marks")
elif(marks>=0 and marks<33):
    print("Failed")
else:
    print("Invailid Instrucsion")

Output :
Enter Your Marks : 86
Topper                            '''



# loops :-
''' '''


i=1
while(i<5) :
    print("Sumit")
    i=i+1


x=10