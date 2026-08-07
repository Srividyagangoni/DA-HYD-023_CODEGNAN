'''
#To print given list in serialno. wise
movies=input("enter movie name:").split()
i=1
for movie in movies:
    print(i,movie)
    i+=1
   
#Fibonacci series
#using for loop
num=int(input("enter values:"))
a=0
b=1
for i in range(num):
    print(a,end=' ')
    c=a+b
    a=b
    b=c

#using while loop
num=int(input("enter values:"))
a=0
b=1
i=0
while i<num:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    i+=1


#write a python program to calculate the innings of a batsman and count the total score,boundaries,dot balls
#list=[4,6,1,0,2,4,0,6]
runs=list(map(int,input("enter no of runs:").split(',')))
boundaries=dotballs=total_score=0
for i in runs:
    total_score+=i
    if i==4 or i==6:
        boundaries+=1
    elif i==0:
        dotballs+=1
    
print('boundaries:',boundaries)
print('dotballs:',dotballs)
print('totalscore:',total_score)
       
#pattern checking
pattern='1234'
max_attempts=5
current_attempt=0
while current_attempt<max_attempts:
    entered_pattern=input("enter pattern:")
    if entered_pattern==pattern:
        print("Unlocked")
        break
    else:
        print("entered pattern is incorrect,Try again")
        current_attempt+=1
else:
    print("Phone Locked, try after 30 seconds")
'''

#ATM pin verification
pin='1234'
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    entered_pin=input("enter pin:")
    if entered_pin==pin:
        print("Login successful")
        break
    else:
        print("entered pin is incorrect,Try again")
        current_attempt+=1
else:
    print("Limit reached, try after 24 hrs..")



















