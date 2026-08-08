'''
#To find secret pin number
pin="1234"
while True:
    entered_pin=input("enter pin:")
    if entered_pin==pin:
        print('Login successful')
        break
    print("Try again")

#OTP verification
pin="2345"
max_attempts=7
current_attempt=0
while current_attempt<max_attempts:
    enter_pin=input("enter pin:")
    if enter_pin==pin:
        print("OTP verified")
        break
    else:
        print("incorrect OTP, enter another OTP")
        current_attempt+=1
else:
    print("Limit reached")

#To print the count of ordered food
food=input("food items name:")
count=0
while food!="exit":
    count+=1
    food=input("food items name:")
print("total no.of items ordered",count)    
'''

#guessing word
secret="python"
max_chances=3
current_chance=1
while current_chance<=max_chances:
    key=input("enter secret:")
    if key==secret:
        print(f"you won you have {max_chances-current_chance} chances")
        break
    else:
        remaining=max_chances-current_chance
        print(f"wrong guess, you have {max_chances-current_chance} chances")
        current_chance+=1
else:
    print("chances over")
