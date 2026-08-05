'''
Sequences--> strings,lists,sets,tuples,mapping(dict)

Strings-->Group of characters, we use single or double or triple quotes
for representation of strings...
Strings are Immutable, Ordered,Indexed Collection


name='Codegnan'
print(name)
print(type(name))
print(len(name)) #len--> returns the number of items in container

#index-->used to fetch the object(position) , starts at 0 and ends at len(obj)
#we use [] representation
print(name[0])
print(name[5])
#print(name[25]) #IndexError--> as it is out of range

#Negative Indexing--> -1 to len(obj)
print(name[-1]) #it returns last character
print(name[-4])
#print(name[-23]) #IndexError--> as it is out of range


#Slicing--> We can access group of characters(objects)
#we use [start:end] #start default-->0, start is included, end is excluded

name='Codegnan'
print(name[:]) #returns entire string
print(name[0:]) #returns entire string
print(name[:4]) #starts at 0th index, ends at before 4th index
print(name[1:5])
print(name[0:6])
'''
'''
name='Python'
print(name[3:7])
print(name[7:3]) #returns empty as strings are immutable
#Slicing is applicable from lower index to higher index
print(name[:45]) #returns till end of the string
print(name[45:])

print(name[-5:])
print(name[-1:-5]) #returns empty string
print(name[-5:-1]) #starts at -5 and ends at -2

#print 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])

#including both +ve and -ve
print(name[1:-2])
print(name[2:-6])

#Striding--> [start:stop:step]

name='DataAnalysis'
print(len(name))
#Data--> result
print(name[:4])
print(name[4:])
print(name[-3:])

print(name[::1]) #returns all characters
print(name[::2]) #includes start to end skipping 1 character
print(name[1:6:3]) #[1:6]-->ataAn-->[1:6:3] -->aA

#tnys
print(name[2::3])
print(name[2:13:3])
print(name[::-1]) #it returns reverse of a string
print(name[::-2])



name='codegnan'
#name[3]='w' #Strings are immutable

#Operations on Strings--> Indexing,Concatination,Repetition
print(name*3)
print('*'*25) #repetition

#Concatenation--> combining strings
data='srividya'+'python'+' '+'database'
print(data)
print('123'*4) #Numeric String
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
#in the above case we get every character line by line

for i in 'codegnan':
    print(i,end='')

name="dataCodegnan"
#Built-in functions-->len(),min(),max(),sorted()
print(len(name))
print(min(name)) #alphabetical order according to ASCII values
print(ord('A')) #prints ASCII value of A->65
print(ord('a')) #prints ASCII value of a->97
print(chr(97)) #gives letter of this ASCII value 97->a
print(max(name))
print(sorted(name)) #returns a list by sorting all elements
'''
#Methods on Strings -->Case-Conversions,Finding/Searching..
name='codegnan data'
#Case-conversions -->upper(),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
#title()--> converts every work first letter to uppercase
c=name.title()
print(c)
#Capitalize()--> converts first letter to uppercase
d=name.capitalize()
print(d)


#task: Workout with all possibilities of slicing and striding on a example
#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z




