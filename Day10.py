'''
Sequences-->Strings,Lists,Tuples,Sets
Mapping-->Dictionary

#Lists--> Collection of heterogenous elements(items)
#List--> Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data

marks=[35,25,45,65]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#Operations :Indexing,Slicing,Striding,Membership,Merging,Repetition


#Nested Lists--> A list inside another list
names=['Codegnan',23,4.5,[23,24,25,26],'DA23',34]

print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4])#it returns Code
print(names[0][4:])

#get the output as Cdga
print(names[0][::2])
names[0]=names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,Slicing--> Mutable
names[2]='Python'
print(names)
#By indexing if we change the elements,length of collection will remain same
names[4]=['codegnan','PFS','JFS']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][1:])
print(names[4][0][4:])

names[2:4]='Srividya','jash','vaish','harshitha'
print(names)
#In Slicing whatever elements you passnas per the logic length keeps on increase

names[3:6:2]='Python','Java'
print(names)
'''
#Created a nested list with strings,lists and work on Indexing, Slicing,Striding
#added advantage if u could add string functions also to it
#Lists Functions -->append(),insert(),extend(),pop(),remove(),clear(),index(),count(),
#copy(),sort(),reverse()

names=['codegnan','srividya']
#append()-->inserts single element to the end of the list
names.append('data')
print(names)
#names.append('analysis','agents')   #Type Error
names.append(['analysis','agents'])
print(names)
#append will always increment the length of list by 1
#print(names[3])
print(names[3].append('chatgpt')) #it returns None as append is applicable on list not print
print(names[3])
print(names)
'''
#extend--> inserts multiple elements to the end of list
names.extend('analysis') #string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([34,23,45,21])
print(names)
#names.extend(34,23,45,21) #Type Error
#print(names)

#insert(index,object)--> inserts given object before index
names.insert(1,'Python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b']) #Syntax Error
#print(names)
names.insert(-1,'AAA')
print(names)
names.insert(-2,'S')
print(names)
'''
#pop(),remove(),clear()
#pop() by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)

#remove() we can removea specific value
names.extend([23,14,13])
print(names)

names.remove(14)
print(names)
#names.remove(14) #it raises ValueError
del names[1:3] #del keyword will apply permanent changes
print(names)
names.clear() #clear() will remove all elements and returns empty list
print(names)

#data=['codegnan','srividya','python','java'] #input
#output should be as follows
'''
0 : codegnan
1 : srividya
2 : python
3 : java
'''
name=['codegnan','srividya','python','java']
for i in range(len(name)):
    print(i, ":", name[i])





























