#Even or Odd
'''
num=int(input("enter number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")



Task: Student marks and grade analyzer
90-100 -->'A'
80-89 -->'B'
70-79 -->'C'
60-69 -->'D'
<60 --> 'Fail'
# also -ve cases should not be entered and marks should not greater than 100

# Using if,elif, else

marks=int(input("Enter marks:"))
if 90<= marks <=100:
    print("Grade:A")
elif 80<= marks <=89 :
    print("Grade:B")
elif 70<= marks <=79:
    print("Grade:C")
elif 60<= marks <=69:
    print("Grade:D")
elif marks<60 and marks>=0:
    print("Fail")
else:
    print("-ve cases should not be entered and marks should not greater than 100")


#Positive or negative value
num=int(input("enter number:"))
if num>=0:
    print("positive number")
else:
    print("negative number")
 

#ATM
amount=int(input("enter amount:"))
if amount>=500:
    print("Withdraw Amount")
else:
    print("Unsuccessfull transaction")



#Grade Checker

marks=int(input("Enter marks:"))
if marks<0 or marks>100:
    print("Invalid marks entered")

elif marks>=90:
    print("Grade:A")
    print("Remark: Outstanding!")
elif marks<=89 and marks>=80:
    print("Grade:B")
    print("Remarks: Excellent!")
elif marks<=79 and marks>=70:
    print("Grade:C")
    print("Remark: Good")
elif marks<=69 and marks>=60:
    print("Grade:D")
    print("Remark: Fair,needs improvement")
elif marks<=59 and marks>=50:
    print("Grade:E")
    print("Remark: Poor,needs serious improvement")
else:
    print("Grade:F")
    print("Remark: Failed,needs to reapper")



#Even or Odd checker(with Twist)

num=int(input("Enter a number:"))
if num==0:
    print("Zero is neither even nor odd")
elif num<0 and num%2==0:
    print("Negative Even number")
elif num<0 and num%2!=0:
    print("Negative Odd number")
elif num%2==0:
    print("Even number")    
else:
    print("Odd number")
'''


#Season Identifier

month=int(input("Enter month number:"))
if month>12 or month<=0:
    print("Invalid month entered:")
elif month==12 or month==1 or month==2:
    print("Season:Winter")
elif month==3 or month==4 or month==5:
    print("Season:Spring")
elif month==6 or month==7 or month==8:
    print("Season:Summer")
else:
    print("Season:Autumn")
