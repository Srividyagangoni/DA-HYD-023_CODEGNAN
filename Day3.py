#Numeric datatype -->int,float,complex along with boolean

#Input formatting -->Accepting input from the user--> input()

#Accepting integer input from user
#by default input() accepts any input-->str
#int(input())-->will accept only integers

age=int(input("Enter the age:"))
print(age)
print(type(age))

#float(input())-->accepts int ,float
age=float(input("Enter the age:"))
print(age)
print(type(age))

#Accepting string input from user
name=input("Enter the name:")
print(name)
print(type(name))


a=input("enter values:").split()  #by default split() has space
print(a)

#space seperated values
a=input("enter values:").split()  #now you enter spaces in output 
print(a)

#comma seperated values
a=input("enter values:").split(',') 
print(a)


#list of integers
marks=list(map(int,input("Enter the values:").split(',')))
print(marks)

#Now we want to accept 2 values from user
age,salary=map(int,input("Enter the values:").split(','))
print(age)
print(salary)


#Single input-->int(input())
#two inputs-->a,b=map(int,input().split(','))
#any number result as list -->a=list(map(int,input().split(',')))

#float of integers
marks=list(map(float,input("Enter the values:").split(',')))
print(marks)

#group of float values
age,salary=map(float,input("Enter the values:").split(','))
print(age)
print(salary)


#Accepting input from user-->int,float-->input formatting

#Operators --> Operators perform operations between values(operands)
#7 types--> Arithmetic, Assignment, Comparision(Relation), Memebership, Identity, Logical, Bitwise


#Arithmetic Operator-> Arithmetic operations
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3) #float value
print(5%3) #Modulus-->it returns remainder
print(5//3) #Floor division-->it returns quotient
print(5**3) #power exponential      
      
#Task--> Accept integer input as length,breadth-->find the area of rectangle
#Area=length*breadth

a=int(input("enter length:"))
b=int(input("enter breadth:"))
area=a*b
print(area)


length,breadth=map(int,input("enter values:").split(','))
area=length*breadth
print(area)


#Assignment operators-->Assign the values
# =,+=,-=
a=45
print(a)

#update the value of a
a=a+5
print(a)

b=35
b+=a #b=b+a
print(b)

b-=a
print(b)

b*=a
print(b)

b/=a
print(b)

b//=a
print(b)

b%=a
print(b)

b**=a
print(b)


#Comparision Operator -->we compare the values-->boolean
# ==(equal to), !=(not equal to), <(less than), >(greater than),
#  <=(less than or equal to), >=(greater than or equal to)

age=25
print(age==25) #returns boolean output
print(age!=20)
print(age>30)
print(age<40)
print(age<=25)
print(age>=50)


#Membership Operator-->in,not in-->boolean
#it checks for the existance of an object in a collection

marks=[35,37,48]
print(25 in marks)
print(30 not in marks)
print(25 in 255) #Type Error

print('code' in 'codegnan')
print('@' in '@!aj')


#Logical Operator-->logical decision making-->and,or,not
#and-->all conditions to be satisfied
#or-->any one condition to be satisfied

a=(25 in [25,45,65]) and 45<65
print(a)

b=45>56 or 25<=45
print(b)

c=not(True)
print(c)



#Identity Operator-->check for identity of an object-->id()
# is , is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)

a=[2,3,7,5]
print(id(a))
c=a
print(id(c))
print(c is a)
