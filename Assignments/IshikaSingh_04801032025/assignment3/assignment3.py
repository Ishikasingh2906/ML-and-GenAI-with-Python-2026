#Create a function to print first 10 natural numbers.
for i in range(1,11):
    print(i)
#Create a function to calculate sum of first N natural numbers.
n=int(input("enter your number:"))
sum=0
for a in range(1,n+1):
    sum+=a
print(sum)

#Create a function to reverse a number.
num=int(input("enter your number:"))
rev=0
while num>0:
    remainder=num%10
    rev=rev*10+remainder
    num=num//10
print(rev)
    
#Create a function to count digits in a number.
def count_digits(num):
    digits = list(str(abs(num)))  # creates a list of digit characters
    print(digits)
    return len(digits)

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))


#Create a function to check palindrome number. # type: ignore
n1=int(input("Enter the number to check: "))
orig=n1
rev=0
while n1>0:
    remainder=n1%10
    rev=rev*10+remainder
    n1=n1//10
print(rev)
    
if rev==orig:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
#Create a function to generate Fibonacci series.
term=int(input("Enter the number of terms: "))
a,b=0,1
for i in range(1,term+1):
    print(a ,end=",")
    a,b=b,a+b
"""Calculator Using Functions that contains the following features;
	-	User selects operation 
	-	Program performs calculation 
	-	Display result"""
# Functions for calculations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


# Menu
print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    result = "Invalid choice!"

print("Result:", result)

#Create a text file and store student details. 
# Create a file and store student details

file = open("student.txt", "w")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write("Student Details\n")
file.write("----------------\n")
file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved successfully!")
#Read data from a file. 
# Read data from the file

file = open("student.txt", "r")

data = file.read()

print("\nData stored in file:")
print(data)

file.close()
#Handle division by zero using exception handling. 
# Handle division by zero using exception handling

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

print("Program ended.")
#Create a Student class with name and marks. 
# Create a Student class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter student name: ")
marks = int(input("Enter marks: "))

student1 = Student(name, marks)

student1.display()
