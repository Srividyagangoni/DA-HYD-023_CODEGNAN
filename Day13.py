'''
Mapping --> Dictionary--> Collection of key_value pairs used to store
related data--> JSON,APIs,database records

dict()--> data={}
Dictionary is Mutable, Indexed through keys,Ordered,Heterogenous,
Keys must be Unique (int,strings,float values...)
'''
details={}
print(type(details))

details={'Id':'CGH3991',
         'Name':'Srividya',
         'Gender':'Female',
         'Age':21,
         'Batch':'DA23',
         'Place':'Hyd'}
print(details)
print(len(details))

#Access the data from dictionary
#details[0] #KeyError
'''
print(details.keys()) #it returns keys from the dictionary
print(details.values()) #it returns values from the dictionary
print(details['Id'],details['Name'])
#if key name is not matching/invalid
#print(details['marks']) #KeyError as marks is not present
details['marks']=[]
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)
details['marks'].extend([21,22,23,24])
print(details)

#create a key-value pair of Practice session
details['Practice']=('Tues','Thurs','Sat')
print(details.keys())
print(details.values())

#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day of Practice Session
print(details['Practice'][1])

details['MI']=('Monday','wednesday','Friday')
print(details)
#operations--> mutable,indexing through keys,membership
print('wednesday' in details)
print('MI' in details) #returns True as we have MI as key

for i in details:
    print(i) #returns keys one by one

for i in details.keys():
    print(f'Key = {i}')
    print(f'Value = {details[i]}')

#keys()--> returns keys from the dictionary

for i in details.items(): #returns a key-value pair in tuple
    print(i)

for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')

#update()--> updating the dictionary with key-value pairs
details.update({'marks':[],
                'Practice':('Tues','Thurs','Sat')})
print(details)
details['marks'].extend([24,25,23])
print(details)
marks=list(map(int,input("enter marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

print(details.keys())
print(details.get('Name'))
print(details.get('Branch')) #returns None as we don't have Branch as the key
print(details.keys())

details.setdefault('Branch') #if key is not present it inserts into dict
print(details)
details['Branch']='CSE'
print(details)

print(details.setdefault('Name'))#if key is already present it can't insert into dict
print(details.keys())

print(details.pop('Branch')) #we need to mention key
print(details.keys())

print(details.popitem()) #removes and return a key,value pair as a 2-tuple
print(details.popitem())
print(details.keys())

del details['Id']
print(details.keys())

details.clear() #removes all elements from D
print(details)

#fromkeys()--> creates a dictionary from iterable(lists,tuples,sets,strings)

data=['srividya','jashnavi','vaishnavi']
b=dict.fromkeys(data) #creates a dict but value set to None
print(b)
b['srividya']=31
print(b)
c=dict.fromkeys(['CGH1234','CGH2345'])
print(c)
'''
#Task-1: Create a dictionary with your personal details, similar to your Codegnan Profile

details={'Name':'Gangoni Srividya','Student ID':'CGH3991',
         'Batch No':'DA-HYD-023','Email ID':'srividyagangoni01@gmail.com',
         'Date of Birth':'2005-04-01','Age':21,'Gender':'Female',
         'City':'Hyderabad','State':'Telangana','PhnNo':'xxxxxxxx',
         'Github Link':'https://github.com/Srividyagangoni'}
print(details)










