# Basic Calculator

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers, handling division by zero
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Displaying the results
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
