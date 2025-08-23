# Square of a number 
def square(n):
    ans = n * n
    print("Square of the given number is :", ans)

n = int(input("Enter the number : "))
square(n)

# Output Example:
# Enter the number : 6
# Square of the given number is : 36

# ------------------------------------------------------------------------------------------------------------------

# Function with multiple parameters
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

addition = add(10, 5)
subtraction = subtract(10, 5)
print("Addition of the two numbers is :", addition)
print("Subtraction of the two numbers is :", subtraction)

# Output:
# Addition of the two numbers is : 15
# Subtraction of the two numbers is : 5

# ------------------------------------------------------------------------------------------------------------------

# Polymorphism in functions
def multiply(a, b):
    return a * b

multiply_int = multiply(5, 10)
multiply_string = multiply("Hello ", 2)

print("Multiplication of integers is:", multiply_int)
print("Multiplication of strings is:", multiply_string)

# Output:
# Multiplication of integers is: 50
# Multiplication of strings is: Hello Hello 

# ------------------------------------------------------------------------------------------------------------------

# Function returning multiple values
def calculate(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference

r = float(input("Enter the radius of the circle: "))
area, circumference = calculate(r)
print("Area of the circle is:", round(area, 2))   
print("Circumference of the circle is:", round(circumference, 2))

# Output Example:
# Enter the radius of the circle: 5
# Area of the circle is: 78.5
# Circumference of the circle is: 31.4

# ------------------------------------------------------------------------------------------------------------------

# Function with default parameters
def greet(name="Guest"):
    return "Hello, " + name + "!"

print(greet("Rishabh"))  # Calls the function with a specific name
print(greet())           # Calls the function with default parameter

# Output:
# Hello, Rishabh!
# Hello, Guest!

# ------------------------------------------------------------------------------------------------------------------

# Lambda function
square = lambda x: x * x
print("Square of 5 is:", square(5))

# Output:
# Square of 5 is: 25

# ------------------------------------------------------------------------------------------------------------------

# Function with *args
# Problem -> write a function that takes any number of arguments and returns their sum
def sum_of_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of numbers is:", sum_of_numbers(1, 2, 3, 4, 5))
print("Sum of numbers is:", sum_of_numbers(10, 20, 30))

# Output:
# Sum of numbers is: 15
# Sum of numbers is: 60

# ------------------------------------------------------------------------------------------------------------------

# Function with **kwargs
# Problem -> write a function that takes any number of keyword arguments and returns a dictionary
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(product="Laptop", price=1200, stock=50)

# Output:
# name: Alice
# age: 30
# city: New York
# product: Laptop
# price: 1200
# stock: 50

# ------------------------------------------------------------------------------------------------------------------

# Generator function with yield
# Problem -> Write a generator function that yields even numbers up to a given limit
def even_numbers(limit):
    for num in range(0, limit + 1, 2):
        yield num

for even in even_numbers(10):
    print(even)

# Output:
# 0
# 2
# 4
# 6
# 8
# 10

# ------------------------------------------------------------------------------------------------------------------

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number to calculate its factorial : "))
print("Factorial of", n, "is:", factorial(n))

# Output Example:
# Enter a number to calculate its factorial : 5
# Factorial of 5 is: 120
