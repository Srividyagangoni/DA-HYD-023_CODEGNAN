#Task-1 --> Create a Nested tuple as above and work on Slicing,Striding and list Functions
'''
names=('codegnan',['hyd','DA'],'DS','DS','AI',[1,2,3])
print(names)
print(len(names))
print(type(names))
print(names[1:4])
print(names[-1:])
print(names[::2])
print(names[1::3])
print(names[1][1:])
print(names[-3][-2])
#append
names[-1].append('Agentics')
print(names)
#index
print(names.index('codegnan'))
#sort
#print(names.sort()) #TypeError
a=[1,-5,0,2,3,5]
a.sort()
print(a)
#count
print(names.count('DS'))
'''
#Task-2--> take a user input as string, do this in two ways..
'''
1) give the count of each repeating character
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]
'''

a=input("enter string:")
count=0
new=[]
for i in a:
    if i not in new:
        new.append(i)
        count=a.count(i)
        if count>1:
            print(f'{i} is repeating {a.count(i)} times')
           
name = input('Enter word:')
word = []
new = []
word.extend(name)
print(word)
for ch in word:
    if ch not in new:
        index = []
        new.append(ch)
        count = word.count(ch)
        if count > 1:
            start = 0
            print(f'{ch} is repeating {count} times')
            #print(f'index = [{word.index(ch)},{word.index(ch,word.index(ch)+1)}]')
            for i in range(count):
                index.append(word.index(ch,start))
                start = word.index(ch,start)+1
            print(f'Index = {index}')            





















