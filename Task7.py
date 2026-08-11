
#task-1: Text case Converter

a=input("enter string:")
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())
print(a.casefold())


b=input("enter string:")
print(b.upper())
print(b.lower())
print(b.title())
print(b.capitalize())
print(b.swapcase()) 

'''
#Task-2: Username Validator

a=input("enter the string:")
while a!="exit":
    if a.isidentifier():
        print("valid python identifier")
    if a.isascii():
        print('Contains only ASCII characters')
    if a[0].isalpha():
        print("Begins with a letter")
    if a.isalnum():
        print("Does not contain only letters and numbers")    
   
    a=input("enter the string:")   


#Task-3: Formatted Student Report
students = []
for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
        continue

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append((name, marks, grade))

print("\n" + "STUDENT REPORT".center(30))
print("=" * 30)
print(f"{'Name'.ljust(15)}{'Marks'.rjust(5)}{'Grade'.rjust(8)}")

for name, marks, grade in students:
    print(f"{name.ljust(15)}{str(marks).rjust(5)}{grade.rjust(8)}")


#Task-4: Character and text Analyzer
text=input("enter string:")
digit_count=0
letter_count=0
space_count=0
printable_count=0
for i in text:
   if i.isalpha():
       letter_count+=1    
   if i.isdigit():
       digit_count+=1
   if i.isspace():
       space_count+=1
   if i.isprintable():
       printable_count+=1
print("Letters :",letter_count)
print("Digits :",digit_count)
print("Spaces :",space_count)
print("Printable :",printable_count)
print("Title case: ",text.istitle())
print("Upper case: ",text.isupper())
print("Lower case :",text.islower())
'''

 
    






