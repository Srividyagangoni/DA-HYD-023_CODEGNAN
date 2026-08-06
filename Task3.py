'''
#To print sum of all prices
price=list(map(int,input("enter cost:").split(',')))
cost=0
for i in price:
    cost=cost+i
print(cost)


#write a code to analyze password as how many uppercase,lowercase,special char,numbers count
password=input("enter password:")
upperl_count=0
lowerl_count=0
digit_count=0
schar_count=0
for i in password:
    if '0'<=i<='9':
        digit_count+=1
    elif 'a'<=i<='z':
        lowerl_count+=1
    elif 'A'<=i<='Z':
        upperl_count+=1
    else :
        schar_count+=1
print("digit:",digit_count)
print("lower:",lowerl_count)
print("upper:",upperl_count)
print("char:",schar_count)               
              
#return the domain of the email
mail=input("enter email:").split()
for i in mail:
    print(i.split("@")[1])
#or
mail=input("enter email:")
print(mail.split("@")[1])
'''

