#Identity Operator

a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collection) both c and a lists will have different
#ids where as values are same
print(c is a) #output False
print(c == a) #output True
print( a is not c)


#Bitwise Operator --> we perform bitwise operations over operands
# &(and) , |(or) , ^(XOR) , shifting operators(<<,>>)

#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR

print(5^3) #bitwise XOR

print(5 and 3) #here and is logical operator checks for both existances.
#returns 3 in this case

print(5 or 3) #returns 5 in this case


#Leftshift Operator << , Rightshift Operator >>

print(5<1) #False Comparision
print(5<<1) #leftshift
print(5>>1) #rightshift
print(5<<3)

print(15<<2) #convert 15 to binary and perform 2 times left shifting

print(15>>2) #same 2 times right shifting


# Input Formatting --> input(), int(input()),float(input())
#You Know --> single input
#2 or 3 inputs -->map()
#group of integers -->list(map(int,input().split(','))

names=input("enter names:").split(',')
print(names)

name1,name2=map(str,input("enter the friends names:").split(','))
print(name1,name2)


#Control Block Statements -->control the flow of program -> when to execute, how to execute
#Conditional Statements -->if,els,elif(rely on condition to be executed)
#Repetition  Statements(Loops)--> for, while

#Conditional Statements --> if usage


Syntax:

if <condition>:
    statement(s)...
    .....


#age=15
age=int(input("enter your age:"))
if age==20:
    print("Your age is:",age)



age=int(input("enter your age:"))
if age>=20 and age in [19,25,30]:
    print("Your age is:",age)


#else keyword-->if-else

else:
    statement(s)...

if-else usage as below:
#Syntax:

if <condition>:
    statement(s)...
else:
    statement(s)...
    ....
    


#Vote Eligibility -->To check his/her voter eligibilty and give access..

age=int(input("enter age:"))
if age>=18:
    print("you have voter eligibilty and age is",age)
    print("access granted")
else:
    age=18-age
    print("you are not eligible, you need to wait for more",age,"years")
    

#Same case let's use only nested -->if,else
age=int(input("enter age:"))
if age>0:
    if age>=18:
        print("you have voter eligibilty and age is",age)
        print("access granted")
    else:
        age=18-age
        print("you are not eligible, you need to wait for more",age,"years")
else:
    print("you have entered -ve values/zero enter only +ve")
    

'''
Task: Student marks and grade analyzer
90-100 -->'A'
80-89 -->'B'
70-79 -->'C'
60-69 -->'D'
<60 --> 'Fail'
# also -ve cases should not be entered and marks should not greater tahn 100














