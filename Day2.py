'''
Tokens-->Variables,Punctuators

Variables--> Named memory location , its a placeholder for data
#Rules


#Multiassignment of Variables

name,age,place='codegnan',7,'hyd'
print(name,age,place)
print(name,age,place,sep=',')


#a,b=2,4,3 #avlue Error as too many values to unpack

#Reassigning variables

name="Codegnan"
a,b=45,1.3
print(a,b)
a,b=b,a
print(a,b,sep=',')

a,b=b,c #NameError as c is not defined
print(a,b)

#Deleting the variables -->del

del a,b
print(a,b)


#Punctuators -->[](Lists),()(tuples),{}(Dict,sets)
name="codegnan";age=7; course="DA"
print(name,age,course,sep=',')

#Datatypes -->Numeric(int,float,complex),boolean,None
            #Sequences-->Lists,tuples,sets,Strings,Frozensets,mappings(dict)

#Numeric type-->int, float,complex
#int datatype-->quantity,age...
age=7
print(age)
print(type(age)) #type -->Returns the datatype of object

print(type(24))

#quantity=03 #it is not not allowed
#print(quantity)

#float datatype-->temp,salary,price
price=20.1;discount=2.4
print(price,discount)
print(type(price))


#complex-->combination of real and imag
i2=4
data=5+i2
print(data)

data=5+2j #j is imag representation
print(data)
print(type(data))


#Boolean--> True/False
valid=True
print(valid)
print(type(valid))

error=False
print(type(error))


#Typecasting -->Converting one type to another
#Python by default follows Implicit type (we need not mention the datatype)

#we will go for Explicit Conversion

#Every built-in datatype is a built-in function
#int,float,complex,bool

#TypeCasting -->int-->float,complex,bool

age=34
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age) #returns True for existing data
print(d)

e=bool(0)
print(e)

#float
price=34.25
print(type(price))
b=int(price)
print(b)
c=complex(price)
print(c)
d=bool(price) #returns True for existing data, 
print(d)
'''

#Complex for TypeCasting -->int,float,bool
ab=2+3j
print(ab)
print(type(ab))
#c=int(ab)
#print(c)
#d=float(ab)
#print(d)
e=bool(ab)
print(e)
print(type(e))

a=int(float(bool(45)))
print(a)

b=bool(int(float(23)))
print(b)


a=45+2.4+2+3j+False
print(a)

a=45+2.4+2+3j+True
print(a)
