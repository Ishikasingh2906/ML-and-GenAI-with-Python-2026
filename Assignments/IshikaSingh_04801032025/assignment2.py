a=0
for i in range(1,11):
    a+=i
print("the sum of first 10 natural numbers: ",a)

#Find factorial of a number.
n=int(input("enter the number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("factorial is :",factorial)

#Print Fibonacci Series.
num=int(input("enter the number of terms you want in the series:"))
a,b=0,1
for i in range(1,num+1):
    print(a)
    a,b=b,a+b



#Find largest among 3 numbers.
n1=float(input("enter the first no. :"))
n2=float(input("enter the second no. :"))
n3=float(input("enter the three no. :"))
if n1>=n2 and n1>=n3:
    print(n1,"is the largest number")
elif n2>=n1 and n2>=n3:
    print(n2,"is the largest number")
else:
    print(n3,"is the largest number")

'''#Create Student Result System
Input student details 
Input marks 
Calculate percentage 
Display grade 
Use: 
if-elif-else 
loops 
user input'''

# ==========================================
# Student Result System
# ==========================================

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total_marks = 0
subjects = 5

# Input marks using loop
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks

# Calculate percentage
percentage = total_marks / subjects

# Display grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display Result
print("\n===== STUDENT RESULT =====")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Total Marks:", total_marks)
print("Percentage :", percentage, "%")
print("Grade      :", grade)