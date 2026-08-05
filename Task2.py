'''
num=list(map(int,input("Enter numbers:").split(',')))
result=0
for i in range(6):
    result=result+i
print(result)
'''

#task: Workout with all possibilities of slicing and striding on a example

#Slicing
name='Srividya'
print(name[:]) 
print(name[0:]) 
print(name[:4]) 
print(name[1:8])
print(name[0:6])
print(name[3:7])
print(name[7:3])
print(name[:45]) 
print(name[45:])
print(name[-4:])
print(name[-6:-1])
print(name[-1:-7])

#Striding
name='CodegnandataAnalysis'
print(len(name))
print(name[:15])
print(name[6:])
print(name[-7:])
print(name[::1]) #returns all characters
print(name[::4])
print(name[1:20:3])


#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z

for i in range(65,91):
    print(chr(i),end=' ')
    































