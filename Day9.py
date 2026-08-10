'''
Strings-->CaseConversions,Searching & finding, String testing methods, Replace, Space Removal

#Searching,Finding,Replacing,Joining..

a='Codegnan'
print(len(a))
print(min(a))
print(max(a))

b=a.index('g') #it returns index position
print(b)
c=a.index('n') #it returns only the first occurance
print(c)
d=a.index('n',6) #it retunrs the next occurance
print(d)
#e=a.index('n',8) #returns ValueError
#print(e)
#f=a.index('t') #ValueError
#print(f)
g=a.index('n',1,4)
print(g)


#rindex()--> returns last occurance
b=a.rindex('g')
print(b)
c=a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8) #it retunrs ValueError
#print(d)

#count--> returns the number of items object is repeating
print('Codegnan'.count('n'))
print('Code'.count('w')) #it returns 0 as we dont have 'w' in 'Code'
print('ertyuifghjasd'.count('a'))

#find()--> first occurance but it avoid error returns -1 if substring is not found
print('Codegnan'.find('r')) #it returns -1
print('codegnan'.find('n'))
print('codegnan'.rfind('n'))

#Example
a='Data'
print(len(a))
for i in a:
    #print(i)


#Replacing,Splitting,Joining

#Strings are Immutable
a='Codegnan'
#a[4]='s'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('wertyuifghjkdfghjk'.replace('w',''))
print(a.replace('x','sri'))
print(a.count(i),a.index(i))

#split()
a='vidya jash vaish'
print(len(a))
b=a.split() #by default if we have space it splits (return list)
print(b)
c='vidya,jash,vaish'
d=c.split()
print(d)
e=c.split(',')
print(e)

#join(iterable)--> concatenate any number of strings
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('@'.join('srividya'))
print(' '.join('srividya'))


#String testing methods(boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....
a='Codegnan123'
print(a.isalnum()) #returns true for alphanumeric strings else false
print(a.isalpha()) #returns false because with both alpha and alphanumeric strings
b='codegnan'
print(b.isalpha()) #returns true only for alphabets
print(b.isalnum())
print(b.isdigit()) #returns true only for digits
print('123456789'.isdigit())
print('12'.isnumeric()) #this has upper edge(numbers,fractions,romans)
#startswith()-->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g'))
print('codegnan'.startswith('g',4))
#endswith()--> how its ending
print('codegnan'.endswith('f'))


print('codegnan'.islower()) #returns True for all lowercase
print('COdegnan'.isupper()) #returns True for all uppercase
print('Codegnan Python'.istitle())

#Space removal--. strip() (removes leading and trailing spaces)
a=' Codegnan '
print(a.strip())
b=input('enter the string:').strip().lower()
print(b)
'''
#zfill() filling with zeroes as per the given numeric string
print('123'.zfill(4))
print('123'.zfill(7))

#center(),ljust(),rjust()-->Alignment of strings(check length and then modify the width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))






























