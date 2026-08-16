'''
Sequences-->Strings,Lists,Tuples,Set,Frozenset
Mapping-> Dictionary

#Sets--> A set is a Unique Collection of objects,Unordered,Mutable,Hashing,
#Unindexed,Unique,Heterogenous
#set(),{}
#a={} its an empty dictionary
a=set()
print(type(a))
st_ids={123,234,345,456,234}
print(st_ids)
print(type(st_ids))
print(len(st_ids))
#print(st_ids[2]) #TypeError

print(234 in st_ids)
#print(st_ids*2) #TypeError Set can't be repeated
#print(st_ids + st_ids) #Two sets cannot merge


#data={12,3,4,5,[12,3,4],'srividya'}
#print(data) #No lists inside a Set (hashing technique) Lists are Mutable

data={12,3,4,5,(12,3,4),'srividya'}
print(data)
print(len(data))
for i in data:
    print(i)


#Methods on sets-->add(),update(),remove(),discard(),pop()
names={'sri','vidya','jash','vaish'}
print(len(names))
#add() will insert an element into the set (it can be anywhere but only unique values)
names.add('python')
print(names)
#names.add('vidya','poll') #error add() only one argument
#print(names)
names.add(('poll','abc'))
print(names)
'''
'''
da_names={'ab','bc','sri'}
print(da_names)

#update() we can update multiple elements (set)
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))

#remove(),discard(),pop(),clear()
#remove() removes an element from the set (it must be a member)
da_names.remove('sri')
print(da_names)
#da_names.remove('Sri') #KeyError
#discard() will remove an element if its present else it ignores
da_names.discard('vidya')

da_names.pop()
print(da_names)
print(da_names.pop()) #removes and returns an arbritrary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('srividya')
print(da_names)
da_names.add('jashnavi')
print(da_names)
da_names.update(['vidya','sri'])
print(da_names)

#copy() #creates a shallow copy of set (independent of each other)
d=da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''
'''
#mathematical operations--> union(),intersection(),difference(),symmetric_diff(),
#issubset(),issuperset(),isdisjoint()

da_23={1,2,3,4,5}
da_24={2,7,4,8}
da_25={4,6,9,0}
#event=da_23.union(da_24)
#event=da_23.union(da_24,da_25)
event=da_23 | da_24  # | union()
print(event)
print(len(event))
#common=da_23.intersection(da_24)
common=da_23 & da_24 # & intersection()
print(common)
print(len(common))

common=da_23.intersection_update(da_24)
print(common) #it returns None
print(da_23) #common elements are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and prints remaining elements from first set
diff=da_23.difference(da_24)
print(diff)
a=da_23 - da_24
print(a)
differ=da_23.difference_update(da_24)
print(differ) #it returns None
print(da_23) #common elements are finally stored

#symmetric_difference() -->removes common elements and prints all remaining elements from
#two sets
symm=da_23.symmetric_difference(da_24)
print(symm)
b=da_23 ^ da_24
print(b)

#issubset()--> checks for all elements to be present in other set
da_24.remove(2)
da_24.remove(4)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))
'''






