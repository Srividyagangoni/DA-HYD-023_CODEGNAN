'''
Usage of else with for--> the else keyword will only be executed when the loop is
completely done without any break

'''
#for with else..

work_log=[0,1,1,1,0,1,0]
'''
#result variable-->longest_streak
longest_streak=0 #target variable
current_streak=0
for day in work_log:
    if day==1:
         #print(day)
        current_streak+=1
        
        if current_streak>longest_streak:
            longest_streak=current_streak
            print(longest_streak)
            
            
    else :
        current_streak=0 #streak break
else:
    print(f'Longest Streak is {longest_streak}')

#In this case when the entire loop execution is done we get result of  else block
    
#same progarm with break usage
longest_streak=0 #target variable
current_streak=0
for day in work_log:
    if day==1:
         #print(day)
        current_streak+=1
        
        if current_streak>longest_streak:
            longest_streak=current_streak
            print(f'Longest Streak is {longest_streak}')
            break        
    else :
        current_streak=0 #streak break
else:
    print(f'Longest Streak is {longest_streak}')
print("Execution Done")    


#for else with notifications scenario
notifications=[0,0,0,0]
for notification in notifications:
    if notification==1:
        print('unread notification')
        break
else:
    print("All Caught Up")


#try to take notifications from user--> list of integers
notifications=list(map(int,input("Enter values-->0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification==1:
        print('unread notification')
        break
else:
    print("All Caught Up")
'''

#while--> it relies on Condition, it will be completely executed until the condition is satisfied
'''
Syntax while:

while <condition>:
    statement(s)....
    ........
    ......


while True: #it prints infinite loop we need to press ctrl+c(keyboard interrupt)
    print("YES")

i=0 #initialized statement
while i<=10:
    print(i)
    i=i+1 #counter

#Get counter from 10 to 1
#In reverse order
i=10
while i>=1:
    print(i)
    i=i-1 #decrement

i=0
while i<=10:
    print(10-i)
    i=i+1
'''

#banking scenario -->PIN authentication if more than 3 attempts
#Account locked..

pin="2134"
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    entered_pin=input("Enter ATM PIN:")
    if entered_pin==pin:
        print("Login Successful")
        break
        #continue #it holds for this condition and skips to the next part of the loop
    else:
        print("Entered PIN is wrong, Try again")
        current_attempt+=1
else:
    print("Account Locked, Try after 24hrs")






















